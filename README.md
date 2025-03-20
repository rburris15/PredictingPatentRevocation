# PredictingPatentRevocation
This project predicts the likelihood of patent revocation using data from the European Patent Office (EPO).

It leverages machine learning techniques to analyze patent characteristics, legal events, and citation networks to identify factors influencing revocation outcomes. The repository includes data preprocessing scripts, feature engineering methods, model training pipelines, and evaluation metrics for assessing predictive performance.

## Installation


Clone the repository:
```sh
git clone https://github.com/rburris15/PredictingPatentRevocation.git
cd PredictingPatentRevocation

##Requirements
users can install all requirements by running the requirements file. pip install -r requirements.txt
a new environment is recommended.

python -m venv new_env
source epo_env/bin/activate  # On Windows, use new_env\Scripts\activate
.\epo_env\Scripts\Activate  #in PowerShell
pip install -r requirements.txt
