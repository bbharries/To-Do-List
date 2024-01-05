#!/usr/bin/env python3
import pickle
import os
#from tdldir import read_list
from entry import Entry


running = True

while running:
    print('Select an option via integer:')
    print('1. See/Modify To-Do List')

    user = input()

    if( user == '1'):
        try:
            with open('data.pk1', 'rb') as file:
                loaded_entries = pickle.load(file)
                for entry in loaded_entries:
                    print(entry)

        except FileNotFoundError:
            print(f"File not found: data.pk1" )
        except Exception as e:
            print(f"Error reading file: {e}")
        
    running = False

