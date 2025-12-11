# Wild Bee Foraging and Flower Visitation Analysis 

## Overview

This project investigates the relationship between pollen load carried by bees and their flower visitation patterns. By integrating pollen_load_data with flower_visitation_data, the analysis uncovers insights into pollinator efficiency, flower preferences, and foraging behavior to inform conservation and land management strategies. 

## Project Structure 

.
├── data/
│   ├── pollen_load_data.csv
│   ├── flower_visitation_data.csv
├── scripts/
│   ├── build_database.py
│   ├── analysis_helpers.py
│   └── download_data.py
├── analysis.ipynb
├── requirements.txt
├── README.md
All files use relative paths for cross-platform compatibility.


## Setup Instructions 

1.	Clone the repository:
2.	git clone https://github.com/your-username/wild-bee-foraging-analysis.git
3.	cd wild-bee-foraging-analysis

4.	Create and activate a virtual environment:
    o	Windows:
    o	python -m venv venv
    o	venv\Scripts\activate
    o	Mac/Linux:
    o	python3 -m venv venv
    o	source venv/bin/activate
5.	Install dependencies:
6.	pip install -r requirements.txt

7.	Run Jupyter Notebook:
8.	jupyter notebook
    Open analysis.ipynb and follow the workflow.

9.	Data/scripts usage:
    o	Data files are in the data/ directory.
    o	Use scripts/download_data.py to retrieve or refresh source datasets.


## Data Sources 

    •	Pollen Load Data:
    Bee and flower abundance and diversity and bee pollen foraging data from farms in England (https://datasetsearch.research.google.com/search?src=2&query=Bee%20and%20flower%20abundance%20and%20diversity%20and%20bee%20pollen%20foraging%20data%20from%20farms%20in%20England&docid=L2cvMTFqbnltZjJwbQ%3D%3D)
    Wood, T.J., Holland, J.M., & Goulson, D.
    •	Flower Visitation Data:
    Data from On-farm Wildflower Plantings Generate Opposing Reproductive Outcomes for Solitary Bees (https://catalog.data.gov/dataset/data-from-on-farm-wildflower-plantings-generate-opposing-reproductive-outcomes-for-solitar)
    U.S. Department of Agriculture

All sources are cited according to dataset documentation.
________________________________________


## requirements.txt 

pandas
numpy
matplotlib
seaborn
sqlite3
jupyter

Install all dependencies with:
pip install -r requirements.txt


## Key Findings 

•	Data cleaning ensured accurate integration and analysis by addressing missing values, duplicates, and type inconsistencies.
•	Exploratory analysis revealed significant differences in pollen load across flower species and bee species, highlighting optimal plant-bee combinations for conservation.
•	Bee species exhibit distinct flower preferences, and higher visitation frequencies correlate with increased pollen loads.
•	The constructed relational database enables advanced queries into bee-flower-pollen interactions, supporting ecological research and management decisions.
