import os
import io

# Specify the directory
dir_path = 'train/labels'

# Get a list of all files in the directory
files = os.listdir(dir_path)

# Initialize a counter for files with more than one line
count = 0

# Iterate over each file
for file in files:
    # Check if the file is a text file
    if file.endswith('.txt'):
        # Open the file
        with io.open(os.path.join(dir_path, file), 'r', encoding='utf8') as f:
            # Read the lines in the file
            lines = f.readlines()
            # If the file has more than one line, increment the counter
            if len(lines) > 1:
                count += 1

print(f'There are {count} text files with more than one line in the directory.')
