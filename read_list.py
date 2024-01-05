#!/usr/bin/env python3
import os
import pickle
from entry import Entry

def load_entries(file_path):
    try:
        with open('data.pk1', 'rb') as file:
            loaded_entries = pickle.load(file)
            for loaded_entry in load_entries:
                print(loaded_entry)

            return loaded_entries
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []
    except Exception as e:
        print(f"Error reading file: {e}")
        return []

if __name__ == "__main__":
    file_path = "data.pk1"
    entries_list = load_entries(file_path)
    print(entries_list)

    for entry in entries_list:
        print(entry)
        
