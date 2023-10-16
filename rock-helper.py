import os
import time
import shutil

#https://ignition4.customsforge.com/

def move_psarc_files(source_path, destination_path):
    # Check if both source and destination directories exist
    if not os.path.exists(source_path):
        print(f"Source path {source_path} does not exist.")
        return

    if not os.path.exists(destination_path):
        print(f"Destination path {destination_path} does not exist.")
        return

    # List files in source directory
    for file in os.listdir(source_path):
        if file.endswith('.psarc'):
            source_file = os.path.join(source_path, file)
            destination_file = os.path.join(destination_path, file)
            
            # Move the file from source to destination
            shutil.move(source_file, destination_file)
            print(f"Moved {file} to {destination_path}")

def main():
    source_path = input("Enter the source path: ")
    destination_path = input("Enter the destination path: ")

    while True:
        move_psarc_files(source_path, destination_path)
        time.sleep(10)  # Sleep for 10 seconds before checking again

if __name__ == "__main__":
    main()
