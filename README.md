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

To run the all stages mentioned in dvc.yaml
```
dvc repro
```

adding stages to the dvc.yaml file
```
stages:
    stage_name(v):
        cmd:  ...........(command in command line to be run)
        deps:- .....   (mention dependent packages)
            - .....
        outs: 
            - .....  (mention what is the output from above commands)

```


To show the metrics
```
dvs mterics show
```

To know the difference in metrics for present and previous run
```bash
dvc metrics diff
```


pytest commands
```
pytest -v
```

setup.py command
```
pip install -e .
```

command for create wheel file of package
``` 
python setup.py sdist bdist_wheel
```