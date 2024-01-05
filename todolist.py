#!/usr/bin/env python3
import pickle
import os
#from tdldir import read_list
from entry import Entry
import read_list
import main_menu

running = True

while running:

    print('Select an option via integer:')
    print('1. See/Modify To-Do List')
    print('2. See Reminders')
    print('3. Search')
    print('4. Statistics')
    print('5. Exit')

    user = input()

    if( user == '5' ):
        print('Now exiting...')
        running = False

    elif( user == '1' ):
        running_menu = True
        
        file_path = 'data.pk1'
    
        with open('data.pk1', 'rb') as file:
            loaded_entries = pickle.load(file)


        while running_menu:
            print("-----------------------------------------")
            for index,  entry in enumerate(loaded_entries, start=1):
                print(f"{index}. {entry}")
            print("-----------------------------------------\n")
        
            print('Select an entry from the list')
            print("'s' to select, 'a' to add, 'q' to quit")
            menu = input()


            if(menu.lower() == 'q'):
                with open(file_path, 'wb') as file:
                    pickle.dump(loaded_entries, file)

                print('Now exiting...')
                running_menu = False

            elif( menu.lower() == 'a' ):
                title = input('Please enter title:\n')
                description = input('Please enter description:\n')
                due_date = input('Please enter due date:\n')
                priority = input('Please enter priority:\n')

                entry = Entry( title, description, due_date, priority )
                loaded_entries.append( entry )

                with open('data.pk1', 'wb') as file:
                    pickle.dump( loaded_entries, file )

            elif( menu.lower() == 's'):
                selection = int(input('Please select an entry (int):'))
                entry = loaded_entries[selection-1]
                entry_menu_running = True

                print(f"You selected: {entry}")
                print("'d' for details, 'e' for edit, 'r' to remove, 'q' to exit")
                entry_menu = input()

                if( entry_menu.lower == 'q' ):
                    print('Now exiting...')
                    entry_menu_running = False

                elif( entry_menu.lower == 'r' ):
                    loaded_entries.remove(entry)

                elif( entry_menu.lower() == 'd' ):
                    print(entry.title)
                    print(entry.description)
                    print(entry.due_date)
                    print(entry.priority)
                    print(entry.complete)

                elif( entry_menu.lower() == 'e' ):
                    edit_menu_running = True

                    print("'d' to change description")
                    print("'t' to change due date")
                    print("'p' to change priority")
                    print("'c' to complete")
                    print("'q' to exit")
                    edit_menu = input()

                    if( edit_menu.lower == 'q' ):
                        print('Now exiting...')
                        edit_menu_running = False

                    elif( edit_menu.lower == 'd' ):
                        print('Enter new description:')
                        description = input()

                        entry.change_description( description )

                    elif( edit_menu.lower == 't' ):
                        print('Enter new due date:')
                        due_date = input()

                        entry.change_due_date( due_date )

                    elif( edit_menu.lower == 'p' ):
                        print('Enter new prioirty:')
                        priority = input()

                        entry.change_priority( priority )

                    elif( edit_menu.lower == 'c' ):
                        entry.complete = True

                    else:
                        print("Invalid entry.")

