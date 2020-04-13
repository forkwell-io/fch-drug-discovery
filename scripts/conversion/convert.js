const fs = require('fs');

console.log("Processing for file " + process.argv[2]);

var file = fs.readFileSync(process.argv[2], 'utf8');
const regex = new RegExp(/(MODEL .*)|(REMARK VINA.*)/g);

const ligand = process.argv[2].replace(".\\input\\", "").replace(".pdbqt_out", "");

var output = [];

let m;
while ((m = regex.exec(file)) !== null){
    if (m.index === regex.lastIndex){
        regex.lastIndex++;
    }

    m.forEach((match, groupIndex) => {
        if(groupIndex > 0){
            if(match != undefined){
                output.push(match);
            }
        }
    })
}

var outputString = "";
output.forEach((value, index) => {
    if(!(index % 2)){
        // Uncomment if you want to include the mode number
        // outputString = outputString.concat(index / 2, ",");
    } else {
        var res = value.split("     ");
        outputString = outputString.concat("6LU7_" + ligand + "," + res[1] + "," + res[2] + "," + res[3] + "\n");
    }
});

// console.log(outputString);

try {
    fs.appendFileSync("./results.csv", outputString);
} catch (err) {
    console.log(err);
}