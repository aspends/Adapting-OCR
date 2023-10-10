import os
import random
import shutil

# Define the paths for the source folder and the destination folders
source_folder = "/Users/stashakkarainen/Desktop/Machine Learning/Assignment/Adapting-OCR/plates"
train_folder = "/Users/stashakkarainen/Desktop/Machine Learning/Assignment/Adapting-OCR/plates_1/Train"
test_folder = "/Users/stashakkarainen/Desktop/Machine Learning/Assignment/Adapting-OCR/plates_1/Test"

# Create the train and test folders if they don't exist
os.makedirs(train_folder, exist_ok=True)
os.makedirs(test_folder, exist_ok=True)

# List all the image files in the source folder
image_files = [f for f in os.listdir(source_folder) if f.endswith(('.jpg', '.png', '.jpeg', '.gif'))]

# Set the random seed for reproducibility
random.seed(42)

# Shuffle the image files randomly
random.shuffle(image_files)

# Calculate the split index
split_index = int(0.8 * len(image_files))

# Split the images into train and test sets
train_images = image_files[:split_index]
test_images = image_files[split_index:]

# Copy the train images to the train folder
for image in train_images:
    src = os.path.join(source_folder, image)
    dst = os.path.join(train_folder, image)
    shutil.copy(src, dst)

# Copy the test images to the test folder
for image in test_images:
    src = os.path.join(source_folder, image)
    dst = os.path.join(test_folder, image)
    shutil.copy(src, dst)

print(f"Total images: {len(image_files)}")
print(f"Train images: {len(train_images)}")
print(f"Test images: {len(test_images)}")
