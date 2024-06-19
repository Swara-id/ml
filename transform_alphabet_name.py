import os
import shutil

root = "./ml/alphabets/alphabet-dataset-resize"

dirs = os.listdir(root)

i = 1

for dir in dirs:
    # rename the file to D_{i}.ext
    if not os.path.isdir(os.path.join(root, dir)):
        continue
    className = dir
    for file in os.listdir(os.path.join(root, dir)):
        fileExt = file.split(".")[-1]
        old_file = os.path.join(root, dir, file)
        # the new file in new directory
        # copy the old file to the new directory

        new_file = os.path.join(root, f"D_{i}.{fileExt}")

        print(f"Renamed '{old_file}' to '{new_file}'")
        i += 1
