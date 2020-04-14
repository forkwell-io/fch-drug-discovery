- **drugbank.csv**
  - approved drugs from DrugBank
- **drugcentral.csv**
  - approved drugs from DrugCentral
- **drugbank_prediction.csv**
  - approved drugs from DrugBank with predicted pK<sub>d</sub>
- **drugcentral_prediction.csv**
  - approved drugs from DrugCentral with predicted pK<sub>d</sub>
- **final_checked_result.csv**
  - combined top twenty from two datasets are combined and their binding affinities are checked using pyrx, top ten are in this file

there is one dataset which is too large to be committed here, **featured_bindingdb** (output of ../../feature_engineering.ipynb), it is a pickle dumped file containing the features and label, its google drive link is https://drive.google.com/open?id=14W_0rxSD_9DvHtU0cXZUR94R_JdJtOa7
