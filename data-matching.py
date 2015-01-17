# -*- coding: utf-8 -*-
"""
Created on Sat Jan 17 14:58:11 2015

@author: sahluwalia
"""

#!/usr/bin/env python

import csv


def read_file(filename):
    with open('filename', 'r') as input_file:
        reader = csv.DictReader(input_file, delimiter = '|')
        data = []
        for row in reader:
            data.append(row)
    return data

data_set = {}
data_files =['name-address.psv', 'name-bank-email.psv']
    
    for filename in data_files:
        contents = read_file(filename)
        data_set[filename] = contents
        print contents