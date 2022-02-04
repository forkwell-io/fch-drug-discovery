# Forkwell Coronavirus Hack: Drug Discovery
<hr>

## Introduction
<div style="text-align: justify">
Drug development is generally arduous, costly, and the success rate is dauntingly low. Thus, the identification of drug-target interactions (DTIs) has become a crucial step in early stages of drug discovery. Experimental confirmation of new DTIs is not an easy task, as in vitro experiments are laborious and time-consuming. Even if a confirmed DTI has been used for developing a new drug, the approval for human use of such new drugs can take many years and estimated cost may run over a billion US dollars (Dimasi et al., 2003). Hence, we developed a deep learning model to predict the pK<sub>d</sub> of drug-target pair to make a fast scan through currently approved drugs to discover candidate drugs for nCoV-19. Validating the readily available and approved drugs is more practical to curb the harsh situation in the meantime of waiting for development of de novo drugs.
</div>

## Directory Description
<u>Folders</u>
- **data**
  - the datasets or intermediary data for training and prediction
- **figure**
  - images used for report writing
- **model**
  - trained models will be output to here
- **mypackages**
  - modules to be imported

<u>Files</u>
- **report.ipynb**
  - the final report describing the steps and our findings
- **report.html**
  - the report rendered in html format
- **approved_drugs_validation.ipynb**
  - scanning of approved drugs from DrugCentral and DrugBank to find candidate drugs
- **data_cleaning_and_munging**
  - cleaning and transforming DTBA data from BindingDB into good shape
- **feature_engineering.ipynb**
  - vectorizing SMILES and target protein chain
- **protvec_training.ipynb**
  - training protvec for protein sequence representation
- **purple_teletubbies_training.ipynb**
  - training the regressor for pK<sub>d</sub> prediction
- **smilesvec_training1.ipynb**
  - training smilesvec for ligand representation (we use kaggle notebook and there is limited time quota, so we split it into two training)
- **smilesvec_training2.ipynb**
  - online training of smilesvec from smilesvec_training1.ipynb output

## Requirements
gensim
```sh
conda install gensim
```
pytorch
```sh
conda install -c pytorch pytorch
```
rdkit
```sh
conda install -c conda-forge rdkit
```
deepsmiles
```sh
pip install deepsmiles
```
biovec
```sh
pip install biovec
```

## Acknowledgement
We would like to thank the organizer and committees of this event for bringing us an extraordinary and fun hackathon. We have learnt a lot from this hackathon and the mentors are very helpful.

## Team members
Tan Yong Keat tyk9079@gmail.com<br>
Luar Yong Ting yongtingluar@gmail.com<br>
Nathaniel Ong Yii Tak hinathanielong@gmail.com<br>
Tan Guan Yu <br>
Alvin Wong Guan Sheng <br>

## Challenges
- pyrx takes so long to check even one DTBA
- the sdf files generated using rdkit is different from the ones from online, yielding different results
- lacking domain knowledge

## References
- https://arxiv.org/abs/1811.00761
- https://arxiv.org/abs/1503.05140
- https://www.frontiersin.org/articles/10.3389/fchem.2019.00782/full
