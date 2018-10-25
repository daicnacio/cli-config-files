'''
Created on Oct 19, 2018

@author: david
'''
import json
import sys

def test_load_config_file(argv=None):
    if argv is None:
        argv=sys.argv
    print("loading config file {}".format(argv[1]))

def test_read_config(argv=None):
    if argv is None:
        argv=sys.argv
    print("reading current config values")
    with open('config.json', 'r') as f:
        config = json.load(f)
        print(config['Centrales'])
