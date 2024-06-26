import os

folder_count = 0

folder_items = os.listdir('.')
for item in folder_items:
    if os.path.isdir(item) and item[0].isalpha():
        folder_count += 1

print(f'There are {folder_count} folders in the current directory.')