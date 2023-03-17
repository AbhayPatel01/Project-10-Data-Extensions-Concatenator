# Idea 1:
# Using Data libraries and OOP principles.

import numpy as np
import pandas as pd
import os
import functools 
import sys
import collections
import argparse
import textwrap

extensions = ('.json', '.csv','.tsv','.xml','.xlsx')
sys.tracebacklimit = 0

# Initialise Argment Parser & add arguments.
argparser = argparse.ArgumentParser(
    prog="Concat",
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=textwrap.dedent(
        """\
            Concater Data Extensions
          --------------------------------
            Creates concatenated file from various file extensions:
                + json 
                + csv 
                + tsv 
                + xml (use with adequate understanding, of conversion.)
                + xlsx (to be compeleted)


            > Examples: 
                1. Converting between json, xml, tsv, csv, xslx(): 

                    python3 concater_data_extensions.py -o  sales_data.json -file sales_data.csv

                    python3 concater_data_extensions.py -o  product_info.xml -file product_info.tsv
                    
                    python3 concater_data_extensions.py -o  product_info.json -file log_data.json 


                2. Concatenate Horizontally.  

                    python3 concater_data_extensions.py -o  concatenated_data.json -file data1.json ../dir1/data2.json data3.json 
                    
                    python3 concater_data_extensions.py -o  concatenated_data.csv -file data1.xml dir2/subdir/dir1/data2.csv data3.tsv data4.json /users/name/desktop/data5.json

         """
    ),
)
argparser.add_argument(
    "-orient",
    "--orientation",
    help="Choose Vertical or Horizontal Concatenation",
    default="h",
)


argparser.add_argument("-show", help="Display n Lines Above & Below of File(s)")
# Add a subparser (to be done, next version )

# subparsers = argparse.add_subparsers(title = 'Orientation Selector', help='Concatenation Based on Orientation: Vertical or Horizontal ')
# subparsers.add('v',help='Joins Vertically, like Relational/SQL Joins; see Join type for merging specification')
# subparsers.add('h',help='Joins Horizontally, like unix/linux cat/SQL Union; see join type for merging specification')

argparser.add_argument("-jt", "--join-type", help="Merge files")
argparser.add_argument("-r",help="Allow for Repeated File Names",action='store_false')

reqargs = argparser.add_argument_group("Required Args")
reqargs.add_argument(
    "-file", nargs="+", required=True, help="file type(s)", action="extend"
)
reqargs.add_argument(
    "-o",
    "-out",
    "--output",
    type=argparse.FileType("w"),
    help="Output File for Concatenation",
    required=True,
)

args = argparser.parse_args()

# 1. Attain File Names/path.
# 2. Check exsistance of file path/name in folder. 
    #  Repeated File Name
# 3. Attain File Extension.

# Input Validation. 
def expand_arguments(function):
    """Takes Function that can take a single argument, turns it into a multiple argument function; not a pure function"""
    if function.__code__.co_varnames.__len__() == 1:
        @functools.cache
        def function_1(*args):
            out = []
            for x in args:
                out.append(function(x))
            return out

        return function_1
    return -1

os_paths_exists = expand_arguments(os.path.exists)

def file_path_checking(): 
    if not all(os_paths_exists(*args.file)):
        raise Exception( [ f"❌ Path: '{path_}' Doesn't Exist!" for path_, truth_value in zip(args.file,os_paths_exists(*args.file)) if not truth_value ][0] )

def file_existing_check():
    for file_ in args.file: 
        if not os.path.isfile(file_):
            raise Exception(f"❌ File Not Found: '{file_}' Isn't A File!")

if args.r:
    args.file = list(set(args.file))

files = []

def suitable_extension_check():
    for file_ in args.file + [args.output.name]: 
        file_name, file_extension = os.path.splitext(os.path.basename(file_))
        if file_extension not in extensions: 
            raise Exception(f"❌ Program Extension '{file_extension}'.\nFor File: '{file_name}' Not Applicable; See suitable extensions via: `-h` ")

def to_dataframe(initial_name):
    '''file to dataframe'''
    inital_extension = os.path.basename(initial_name).split('.')[1]
    sheet_name = None 

    if inital_extension == 'xlsx':
        sheet_name = input('Please Specity Sheet Name: ')

    converter_input = {
        'json':pd.read_json,
        'csv': pd.read_csv,
        'tsv': functools.partial(pd.read_csv,sep='\t'),
        'xml': pd.read_xml,
    }
    converter_input['xlsx'] = functools.partial(pd.read_excel , sheet_name)
    df = converter_input[inital_extension](initial_name)
    return df

def convert_extension(initial_name ,final_name , return_df = False):
    ''' Simple Conversion function from dataframe''' 
    
    if type(initial_name) is not str:
        df = initial_name
    else: 
        df = to_dataframe(initial_name)

    final_extension =  os.path.basename(final_name).split('.')[1]
    converter_output = { 
        'json': df.to_json,
        'csv': df.to_csv,
        'tsv': functools.partial(df.to_csv,sep='\t'),
        'xml': df.to_xml,
        'xlsx': df.to_excel 
    }
    converter_output[final_extension](final_name)

# Using input flags and number of arguments to create a concatenated or file extnesion coversion. 
conv_ext = functools.partial(convert_extension, final_name = args.output.name)
# Refer to readme for scenarios. 
# Scenario 1. 

# Next version: 
# Calcuate the threshold for using threading; multiprocessing; async/await. 
# Best practices for threading/multiprocessing using core developer ideas and methods. 

# Scenario set 1. 
if __name__ == '__main__':
    file_existing_check()
    file_path_checking() 
    suitable_extension_check()

    if len(args.file) == 1: 
        conv_ext(args.file[0])
    # Scnario 2 
    elif len(args.file) > 1 and args.orientation == 'h': 
        try:
            df = ( 
                    pd.concat([ to_dataframe(file_) for file_ in args.file  ],ignore_index= True)
                    .rename(columns={'Unnamed: 0': 'Col1'}) 
                )
        except:
            pass
        print(df)
        conv_ext(df)
