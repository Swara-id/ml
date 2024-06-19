import os, sys


def count_file(directory):
    file_count_per_class = {}
    total_files = 0

    for root, dirs, files in os.walk(directory):
        class_name = root.split(os.sep)[-1]
        count = sum(
            1 for file in files if file.endswith(".png") or file.endswith(".jpg")
        )

        if count > 0:
            file_count_per_class[class_name] = count
            total_files += count

    for class_name, count in file_count_per_class.items():
        print(f"{class_name}: {count}")

    print(f"Total Dataset: {total_files}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python count_files.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]
    count_file(directory)
