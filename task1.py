import os
import shutil
import argparse


def copy_files(source_dir, dest_dir):
    try:
        for entry in os.scandir(source_dir):
            if (entry.is_dir()):
                # recursion
                copy_files(entry, dest_dir)
            elif (entry.is_file()):
                extension = entry.name.split(".")[1].lower()
                dest_subdir = os.path.join(dest_dir, extension)
                # create dir if needed
                os.makedirs(dest_subdir, exist_ok=True)

                try:
                    dest_file = os.path.join(dest_subdir, entry.name)
                    shutil.copy2(entry, dest_file)
                    print(f"Copied {entry.name} to {dest_file}")
                except Exception as e:
                    print(f"Copying of {entry.name} failed:", e)
    except Exception as e:
        print(f"Reading of {source_dir} failed:", e)


def get_dirs_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=str)
    parser.add_argument("destination", type=str, default="dest", nargs='?')
    args = parser.parse_args()

    return args.source, args.destination


def main():
    source_dir, dest_dir = get_dirs_args()
    copy_files(source_dir, dest_dir)


if __name__ == "__main__":
    main()

# to test run python3 task1.py dir_to_copy_path dir_where_to_copy_path(optional)
