import os
import re

def rename_files(directory):
    # List all files in the directory
    files = os.listdir(directory)
    directory_name = directory.split('\\')[-1]

    print(f"Processing directory: {directory_name}")

    frame_numbers = []

    # Extract frame numbers to find min for normalization
    for filename in files:
        # pattern = frame_word(dir)_wordNo.jpg
        match = re.match(rf"(\d+)_{directory_name}_(\d+)\.jpg", filename)
        if match:
            frame_number = int(match.group(1))
            if frame_number not in frame_numbers:
              frame_numbers.append(frame_number)

    if not frame_numbers:
        return
    
    print(f"Found {len(frame_numbers)} files with frame numbers: {frame_numbers}")

    for frame_number in frame_numbers:
      pattern = re.compile(rf"{frame_number}_{directory_name}_(\d+)\.jpg")
      matching_files = [f for f in files if pattern.match(f)]
      
      # Sort files based on the numeric part
      matching_files.sort(key=lambda x: int(pattern.search(x).group(1)))
      
      # Rename files sequentially
      for index, filename in enumerate(matching_files, start=1):
          new_filename = f"{frame_number}_{directory_name}_{index}.jpg"
          old_file = os.path.join(directory, filename)
          new_file = os.path.join(directory, new_filename)
          
          # Rename the file
          os.rename(old_file, new_file)
          print(f"Renamed '{old_file}' to '{new_file}'")

# Example usage:
root = './sultani-dataset'

for root, dirs, files in os.walk(root):
    for dir in dirs:
        rename_files(os.path.join(root, dir))