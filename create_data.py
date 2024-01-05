#!/usr/bin/env python3
import os
import pickle
from entry import Entry

example_entry = Entry(title="Example Title", description="Example Description", due_date="2022-12-31", priority=3)

example_entry2 = Entry(title="Example Title", description="Example Description", due_date="2022-12-31", priority=3)

entries_list = [example_entry, example_entry2]


with open('data.pk1', 'wb') as file:
    pickle.dump(entries_list, file)

with open('data.pk1', 'rb') as file:
    loaded_entries = pickle.load(file)
    for loaded_entry in loaded_entries:
        print(loaded_entry)

