#  load the train and test files
#  train the algorithm
#  save the metrics and parameters

import os
import warnings
import sys
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
from get_data import read_params
import argparse
import joblib
import json


def eval_metrics(y_actual,y_pred):
    rmse=mean_squared_error(y_actual,y_pred)**0.5
    mae=mean_absolute_error(y_actual,y_pred)
    r2=r2_score(y_actual,y_pred)
    return rmse,mae,r2


def train_and_evaluate(config_path):
    config=read_params(config_path)
    model_path=config["model_dir"]
    train_data_path=config["split_data"]["train_path"]
    test_data_path=config["split_data"]["test_path"]
    random_state=config["base"]["random_state"]
    l1_ratio=config["estimators"]["ElasticNet"]["params"]["l1_ratio"]
    alpha=config["estimators"]["ElasticNet"]["params"]["alpha"]
    target=[config["base"]["target_col"]]   # it will help while droping the column


    train=pd.read_csv(train_data_path,sep=',')
    test=pd.read_csv(test_data_path,sep=',')


    train_y=train[target]
    test_y=test[target]


    train_x=train.drop(target,axis=1)
    test_x=test.drop(target,axis=1)


    model=ElasticNet(alpha=alpha,l1_ratio=l1_ratio,random_state=random_state)

    model.fit(train_x,train_y)

    predicted_qualities=model.predict(train_x)

    (rmse,mae,r2)=eval_metrics(train_y,predicted_qualities)

    print('rmse',rmse)
    print('mae',mae)
    print('r2_score',r2)

    scores_file=config["report"]["scores_path"]

    with open(scores_file,'w') as f:
        scores={
            'rmse':rmse,
            'mae':mae,
            'r2_score':r2
                }
        json.dump(scores,f,indent=4)
    params_file=config["report"]["params_path"]
    with open(params_file,'w') as f:
        params={
            'alpha':alpha,
            'l1_ratio':l1_ratio
                 }
        json.dump(params,f,indent=4)

        
    #  saving the model

    os.makedirs(model_path,exist_ok=True)
    model_save_path=os.path.join(model_path,'model.joblib')

    joblib.dump(model,model_save_path)






if __name__ == '__main__':
    args=argparse.ArgumentParser()
    args.add_argument('--config',default='params.yaml')
    # args.add_argument('--config',default='params.json')   # trying with json file
    parsed_args=args.parse_args()
    train_and_evaluate(config_path=parsed_args.config)