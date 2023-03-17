import pandas as pd 
import numpy as np 
import seaborn as sns 
import collections
import random
import os
import string

#Creating Some Dattasets.
def data_load(n:int, path:str,file_name:str) -> None:
    '''Creating datasets, no error checking'''
    c1 = collections.deque()
    for dataset in sns.get_dataset_names():
        c1.append(sns.load_dataset(dataset))

    while n > 0:  
        val_df = random.choice(c1)
        last_char = file_name[-1]
        if last_char in string.digits:
            last_char  = str(int(last_char) + 1)
            file_name = file_name[:-1] + last_char
            
        else: 
            file_name += '1'
        cwd = os.getcwd()
        os.chdir(path)
        val_df.to_csv(file_name + '.csv') # the extension could have been random, concat utility does this for users. 
        os.chdir(cwd)
        
        n -= 1

# data_load(2, '../../','Data')
# data_load(2, '.','otherData')
# data_load(5, './Data', 'different_data')