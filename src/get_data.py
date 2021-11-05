
# read params

## process

## return the dataframe

import pandas as pd
import yaml
import os
import argparse

'''
Reading the params.yaml ile by loading it. safe_load is the method present in yaml library. It
parses the given stream and returns a Python object constructed from for the first document in the stream.
'''

def read_params(config_path):
    with open(config_path) as yaml_file:
        config=yaml.safe_load(yaml_file)
    return config

'''
get_data will call read_params method, and it will take the python object of yaml file. Then from the python object
the data_source can be read using the key value pair, and converted into the dataframe.
'''

def get_data(config_path):
    config=read_params(config_path)
   # print(config)        ## It will print the entire params.yaml file
    data_path=config["data_source"]["s3_source"]
    dataframe=pd.read_csv(data_path)
    print(dataframe.head())

if __name__=='__main__':
 #   os.chdir("C:/Users/atulkumarrai/PycharmProjects/Ineuron practice/Ineuron_practice/Wineq_With_MLops")
    args=argparse.ArgumentParser()
    # print("The current directory is",os.getcwd())
    args.add_argument("--config",default='params.yaml')

    parsed_args=args.parse_args()
    get_data(config_path=parsed_args.config)