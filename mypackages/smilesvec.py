import deepsmiles
import gensim
import rdkit
from rdkit import Chem
import tqdm

letters = ["D" ,"E", "J", "R", "L", "M", "T", "Z" ,"X", "d", "e", "j", "r", "m", "t", "z", "x"]

ELEMENTS = ["\[.*?\]", "He", "Li", "Be", "Ne", "Na", "Mg", "Al", "Si", "Cl", "Ar", "Ca",  "Ti", "Cr", "Mn", "Fe",  
            "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Zr", "Nb", "Tc", "Ru", "Rh", 
            "Pd", "Ag", "Cd", "Sb", "Te", "Xe",  "Ba", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", 
            "Dy", "Er", "Tm", "Yb", "Lu", "Hf", "Ta", "Re",  "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", 
            "At", "Rn", "Fr", "Ra", "Ac", "Th", "Pa", "Np", "Pu", "Am",  "Bk",  "Es", "Fm", "Md", 
            "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Uut", "Fl", "Uup", "Lv", "Uus", "Uuo"]

deepsmiles_converter = deepsmiles.Converter(rings=True, branches=True)

def split_ngrams(smiles, n):
    lingoList = []
    
    smiles = deepsmiles_converter.encode(smiles)
    reps, upsmi = modifySMILES(smiles)

    if len(upsmi) < n:
        while len(upsmi) < n:
            upsmi = upsmi + "_"

    for index in range(len(upsmi)-(n-1)):
        lingo = upsmi[index:index+n]
        if containsFromList(lingo):
            for index in range(len(reps)):
                symbol, letter = reps[index].split(",")
                lingo = lingo.replace(letter,symbol)
            lingoList.append(lingo)
            
    return lingoList

def modifySMILES(smiles):
    replacements = {}
    matched = 0

    for el in ELEMENTS:
        p = re.compile(el)
        m = p.findall(smiles)
        for found in set(m):
            smiles = smiles.replace(found, letters[matched])
            replacements[matched] = found + "," + letters[matched]
            matched = matched +1
            
    return replacements, smiles

def containsFromList(smitext):
    for el in letters:
        if smitext.find(el):
            return True
    return False

def generate_corpus(smiles_file, output_corpus_file, n):
    with open(output_corpus_file, 'w+') as out_file:
        with open(smiles_file, 'r') as in_file:
            for smiles in tqdm.tqdm(in_file):
                lingos = split_ngrams(smiles, n)
                out_file.write(' '.join(lingos)+'\n')

class SMILESVec2(gensim.models.Word2Vec):
    def __init__(self, smiles_file, output_corpus_file, n=8):
        self.n = n
        generate_corpus(smiles_file, output_corpus_file, n)
        corpus = gensim.models.word2vec.Text8Corpus(output_corpus_file)
        gensim.models.Word2Vec.__init__(self, corpus, size=100, window=25, min_count=1, sample=1e-4, negative=5, iter=20, sg=1, hs=0, workers=4)

    def online_train(self, smiles_list=None, smiles_file=None, output_corpus_file=None):
        '''
        smiles_list <- a list of smiles
        smiles_file <- file name of the file containing smiles
        output_corpus_file <- smiles splitted into ngrams will be output to this file
        '''
        if smiles_file:
            if not output_corpus_file:
                print('online training failed, "output_corpus_file" not provided')
                return
            generate_corpus(smiles_file, output_corpus_file, self.n)
            corpus = gensim.models.word2vec.Text8Corpus(output_corpus_file)
        elif smiles_list:
            corpus = [split_ngrams(smiles, self.n) for smiles in smiles_list]
        else:
            print('online traning failed, either "smiles_file" or "smiles_list" has to be provided')
        self.build_vocab(corpus, update=True)
        self.train(corpus, epochs=self.epochs, total_examples=self.corpus_count, total_words=self.corpus_total_words)
    
    def has_vocab(self, smiles):
        for v in split_ngrams(smiles, self.n):
            if v not in self.wv.vocab:
                return False
        return True
    
    def to_vec(self, smiles):
        ngram = split_ngrams(smiles, self.n)
        return sum(self.wv[ngram])