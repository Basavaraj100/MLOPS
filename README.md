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

git init        ( to initialise empty git repo)

dvc init        (to initialise dvc)

dvc add data_given/wine_quality.csv   (to track the data)

git add .   (to add to staging are of git)

git commit -m "first commit"  ( mention the name of each stage)

Add new repository in git hub without license then only it shows info


git remote add origin https://github.com/Basavaraj100/MLOPS.git

git branch -M main

git push origin main
