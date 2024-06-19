import os
import shutil
import sys

def move_files_to_root(root_directory):
    for dirpath, dirnames, filenames in os.walk(root_directory):
        if dirpath == root_directory:
            continue

        for filename in filenames:
            src_path = os.path.join(dirpath, filename)
            dst_path = os.path.join(root_directory, filename)

            if os.path.exists(dst_path):
                base, ext = os.path.splitext(filename)
                counter = 1
                while os.path.exists(dst_path):
                    new_filename = f"{base}_{counter}{ext}"
                    dst_path = os.path.join(root_directory, new_filename)
                    counter += 1

            shutil.move(src_path, dst_path)
            print(f"Moved '{src_path}' to '{dst_path}'")


if __name__ == "__main__":
  if len(sys.argv) != 2:
      print("Usage: python move_files_to_root.py <root_directory>")
      sys.exit(1)

  root_directory = sys.argv[1]

  if not os.path.isdir(root_directory):
      print("Error: Root directory not found.")
      sys.exit(1)

  move_files_to_root(root_directory)
