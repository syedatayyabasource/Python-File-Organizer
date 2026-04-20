import os
import shutil

def organize_files(target_directory):
    # Check if directory exists
    if not os.path.exists(target_directory):
        print("Path not found!")
        return

    # Get list of all files in the folder
    files = [f for f in os.listdir(target_directory) if os.path.isfile(os.path.join(target_directory, f))]

    for file in files:
        # Get extension and remove the dot
        extension = os.path.splitext(file)[1][1:].lower()
        
        if not extension:
            extension = "others"

        # Create folder path
        folder_path = os.path.join(target_directory, extension)
        
        # Create folder if it doesn't exist
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # Move file
        try:
            shutil.move(os.path.join(target_directory, file), os.path.join(folder_path, file))
            print(f"Moved {file} to {extension}/")
        except Exception as e:
            print(f"Error moving {file}: {e}")

if __name__ == "__main__":
    folder_path = input("Enter the full path of the folder you want to organize: ")
    organize_files(folder_path)