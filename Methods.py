import  os
import shutil
def create_folder(folder_path:str):
    try:
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Folder created at: {folder_path}")
        else:
            print(f"Folder already exists at: {folder_path}")
    except Exception as e:
        print(f"Error creating folder: {e}")

def delete_folder(folder_path:str):
    try:
        if os.path.exists(folder_path):
            shutil.rmtree(folder_path)
            print(f"Folder deleted at: {folder_path}")
        else:
            print(f"Folder does not exist at: {folder_path}")
    except Exception as e:
        print(f"Error deleting folder: {e}")
def copy_folder(source_path: str, destination_path: str):
    try:
        if os.path.exists(source_path):
            shutil.copytree(source_path, destination_path)
            print(f"Folder copied from {source_path} to {destination_path}")
        else:
            print(f"Source folder does not exist: {source_path}")
    except Exception as e:
        print(f"Error copying folder: {e}")
def move_folder(source_path: str, destination_path: str):
    try:
        if os.path.exists(source_path):
            shutil.move(source_path, destination_path)
            print(f"Folder moved from {source_path} to {destination_path}")
        else:
            print(f"Source folder does not exist: {source_path}")
    except Exception as e:
        print(f"Error moving folder: {e}")
