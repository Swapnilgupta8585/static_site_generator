import os
import shutil


def remove_public_dir_content(public_dir): 
    # if path exists
    if os.path.exists(public_dir) and os.path.isdir(public_dir):
    # Remove the directory and its contents
        try:
            shutil.rmtree(public_dir)
        except Exception as e:
            print(f"Can't remove {public_dir}. Error:{e}")
    # Recreate the directory
        try:
            os.mkdir(public_dir)
            print(f"All contents of {public_dir} have been deleted, and the directory has been recreated.")  
        except Exception as e:
            print(f"Can't recreate {public_dir}. Error:{e}")
    else:
        print(f"The directory {public_dir} does not exist or is not a directory")


def copy_static(file_path, public_dir):
    # Check if the source directory exists
    if os.path.exists(file_path):
        # Iterate through each item (file or directory) in the source directory
        for item in os.listdir(file_path):
            item_path = os.path.join(file_path, item)
            destination_path = os.path.join(public_dir, item)
            
            # If it's a file, copy it to the destination directory
            if os.path.isfile(item_path):
                print(f"Copying file: {item_path} to {destination_path}")
                try:
                    shutil.copy(item_path, destination_path)
                    print(f"File copied successfully")
                except Exception as e:
                    print(f"Failed to copy {item_path}. Error: {e}")
            
            # If it's a directory, recursively call the function to copy its contents
            elif os.path.isdir(item_path):
                # Create the directory in the destination if it doesn't exist
                if not os.path.exists(destination_path):
                    os.makedirs(destination_path)
                # Recursively copy the contents of the subdirectory
                copy_static(item_path, destination_path)
    else:
        print(f"Source directory '{file_path}' does not exist.")




