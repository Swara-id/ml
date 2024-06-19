# for every image in a folder X change the name of the file to X_index.jpg
import os

def transform_image_name(image_folder):
    for folder in os.listdir(image_folder):
        print(f"Processing {folder}")
        folder_path = os.path.join(image_folder, folder)
        for idx, image in enumerate(os.listdir(folder_path)):
            image_path = os.path.join(folder_path, image)
            ext = image.split(".")[-1]
            new_image_name = f"{folder}_{idx}.{ext}"
            new_image_path = os.path.join(folder_path, new_image_name)
            os.rename(image_path, new_image_path)
            print(f"Renamed {image} to {new_image_name}")

if __name__ == "__main__":
    image_folder = "./bismillah-alphabet-dataset-resize/"
    transform_image_name(image_folder)