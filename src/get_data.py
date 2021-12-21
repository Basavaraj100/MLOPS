#  reading parameters
#  process the data
#  return the dataframe

import os
import yaml
import pandas as pd
import argparse
import json

def read_params(config_path):
    with open (config_path) as yaml_file:
        config=yaml.safe_load(yaml_file)
    return config


#  -------------------trying with json file--------------
# def read_params(config_path):
#     with open (config_path) as json_file:                                   # it works
#         config=json.load(json_file)
#     return config

# -----------------------------------------------------------

def get_data(config_path):
    config=read_params(config_path)
    # print(config)
    data_path=config["data_source"]["s3_source"]
    df=pd.read_csv(data_path,sep=',',encoding='utf-8')
    return df



if __name__ == '__main__':
    args=argparse.ArgumentParser()
    args.add_argument('--config',default='params.yaml')
    # args.add_argument('--config',default='params.json')   # trying with json file
    parsed_args=args.parse_args()
    data=get_data(config_path=parsed_args.config)