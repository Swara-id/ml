import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
import tensorflow as tf
from tensorflow.keras.preprocessing.image import (
    ImageDataGenerator,
    img_to_array,
    array_to_img,
    load_img,
)
import sys

import numpy as np


def augment_images(directory, num_augmentations):
    # Define the augmentation
    datagen = ImageDataGenerator(
        rotation_range=3,
        width_shift_range=0.1,
        height_shift_range=0.1,
        shear_range=0.1,
        zoom_range=0.1,
        horizontal_flip=True,
        fill_mode="nearest",
    )
    # Iterate through the directory

    for root, dirs, files in os.walk(directory):
        for file in files:
            # print(file)
            if file.lower().endswith(("png", "jpg", "jpeg")):
                img_path = os.path.join(root, file)
                img = load_img(img_path)
                x = img_to_array(img)
                x = np.expand_dims(x, axis=0)

                # Generate augmentations
                i = 0
                for batch in datagen.flow(x, batch_size=1):
                    aug_img = array_to_img(batch[0])
                    aug_img.save(os.path.join(root, f"augmentasi{i}_{file}"))
                    i += 1
                    if i >= num_augmentations:
                        break


def remove_augmentations(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.startswith("augmentasi"):
                os.remove(os.path.join(root, file))


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Please provide a folder name")
        print("Example: python3 image_augment.py Suka")
        sys.exit(1)

    folder = sys.argv[1]

    if not os.path.exists(os.path.join("./", folder)):
        print(f"Folder {folder} does not exist")
        sys.exit(1)

    choice = input("Do you want to remove any existing augmentations? (y/n): ").lower()

    if choice == "y":
        print(f"Removing augmentations in {folder}")
        remove_augmentations(os.path.join("./", folder))

    input("Press Enter to start augmenting images")

    print(f"Augmenting images in {folder}")
    augment_images(os.path.join("./", folder), 5)
