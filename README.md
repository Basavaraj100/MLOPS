creating environment
```bash
conda create -n wineq python=3.7 -y
```
Activate environment
```
conda activate wineq
```

Install the required libraries
```
pip install -r requirements.txt
```

Steps after creating all template

git init

dvc init

dvc add data_given/wine_quality.csv

git add .

git commit -m "first commit"


