import os
import shutil
import sys
# # Add the Dataset path to access labels data
# sys.path.append('/home/prairie/Documents/PSLD/stable-diffusion/Dataset')

# Path of directory needing labels
PATH = 'samples'

# Create labels directory if needed
if not os.path.exists('labels'):
    os.makedirs('labels')
# Get all synthetic images generated

images = os.listdir("samples")
print(images)
for image in images:
    name, _ = os.path.splitext(image)

    sub_name, _ = os.path.splitext('_'.join(name.split('_')[:-1]))

    # Generate sample path
    sample_path = os.path.join('/home/prairie/Documents/PSLD/stable-diffusion/Dataset/train/labels/', sub_name + '.txt')

    # print(os.path.abspath(sample_path))
    # Check if the sample label exists
    if os.path.exists(sample_path):
        print(name)
        # Copy sample path into labels folder
        shutil.copy(sample_path, os.path.join('labels', name + '.txt'))