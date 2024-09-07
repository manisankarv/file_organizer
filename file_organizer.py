import os
import shutil

def organize_files(directory):
   
    
    if not os.path.isdir(directory):
        print(f"The directory '{directory}' does not exist.")
        return


    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Skip directories; we only want to organize files
        if os.path.isdir(file_path):
            continue

        # Get the file extension
        _, file_extension = os.path.splitext(filename)
        file_extension = file_extension.lower()  # Convert to lowercase

        # Define folder name based on the file extension
        if file_extension:
            folder_name = file_extension[1:]  # Remove the dot from the extension
        else:
            folder_name = 'no_extension'  # Handle files with no extension

        # Create the folder if it doesn't already exist
        folder_path = os.path.join(directory, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # Move the file to the appropriate folder
        shutil.move(file_path, os.path.join(folder_path, filename))
        print(f"Moved '{filename}' to '{folder_path}'")

if __name__ == "__main__":
    # Prompt the user to enter the path of the directory to organize
    target_directory = input("Enter the path of the directory to organize: ")
    organize_files(target_directory)
