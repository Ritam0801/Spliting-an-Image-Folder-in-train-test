# In this code i'm using a root folder (covid images), containing two sub-folders (COVID , non-COVID)

import os 
import random
from shutil import copyfile  

# root folder directory, it must be a String
img_source_dir = '/home/ritam/Desktop/covid images' 

train_size = 0.8 # float

# Randomly splits images over a train and validation folder, while preserving the folder structure
def img_train_test_split(img_source_dir, train_size):
    
    # Checks if we are passing the directory path as a string or not, if not then it will rise an error
    if not (isinstance(img_source_dir, str)): 
        raise AttributeError('img_source_dir must be a string')
        
    if not os.path.exists(img_source_dir):
        raise OSError('img_source_dir does not exist')
        
    # Checks if we are passing training size as a float or not
    if not (isinstance(train_size, float)):
        raise AttributeError('train_size must be a float')
    
    # Creates a folder 'data'
    if not os.path.exists('data'):
        os.makedirs('data')
    else:
        if not os.path.exists('data/train'):
            os.makedirs('data/train')
        if not os.path.exists('data/validation'):
            os.makedirs('data/validation')
            
    # Get the subdirectories in the main 'covid image' folder
    subdirs = [subdir for subdir in os.listdir(img_source_dir) if os.path.isdir(os.path.join(img_source_dir, subdir))]

    for subdir in subdirs:
        subdir_fullpath = os.path.join(img_source_dir, subdir)
        if len(os.listdir(subdir_fullpath)) == 0:
            print(subdir_fullpath + ' is empty')
            break

        train_subdir = os.path.join('data/train', subdir)
        validation_subdir = os.path.join('data/validation', subdir)

        # Create subdirectories in train and validation folders
        if not os.path.exists(train_subdir):
            os.makedirs(train_subdir)

        if not os.path.exists(validation_subdir):
            os.makedirs(validation_subdir)
            
        train_counter = 0
        validation_counter = 0

        # Randomly assign an image to train or validation folder
        for filename in os.listdir(subdir_fullpath):
            if filename.endswith(".jpg") or filename.endswith(".png"): 
                fileparts = filename.split('.')

                if random.uniform(0, 1) <= train_size: # Checks if the training size is valid or not i.e. in between the range (0,1) or not
                    copyfile(os.path.join(subdir_fullpath, filename), os.path.join(train_subdir, str(train_counter) + '.' + fileparts[1]))
                    train_counter += 1
                else:
                    copyfile(os.path.join(subdir_fullpath, filename), os.path.join(validation_subdir, str(validation_counter) + '.' + fileparts[1]))
                    validation_counter += 1
                    
        print('Copied ' + str(train_counter) + ' images to data/train/' + subdir)
        print('Copied ' + str(validation_counter) + ' images to data/validation/' + subdir)
        

if __name__=="__main__":
	img_train_test_split(img_source_dir,train_size)
	

"""
Output :
Copied 1009 images to data/train/COVID
Copied 243 images to data/validation/COVID
Copied 982 images to data/train/non-COVID
Copied 247 images to data/validation/non-COVID

"""
