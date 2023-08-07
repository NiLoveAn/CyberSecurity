import shutil
import os
def backup_directory(source_dir, destination_dir):
    try:
        shutil.copytree(source_dir, destination_dir)
        print("Backup DONE!")
    except shutil.Error as e:
        print(f"Backup error: {e}")
    except OSError as e:
        print(f"OS Error: {e}")

source_dir = "C:/Users/bushum/Desktop/Module_3/test"
destination_dir = "C:/Users/bushum/Desktop/Module_3/test_backup"
backup_directory(source_dir,destination_dir)