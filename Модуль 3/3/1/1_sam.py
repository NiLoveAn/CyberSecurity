import shutil
import os

def backup_files(source_dir, destination_dir):
    shutil.copytree(source_dir, destination_dir)
    print("Backup DONE!")

def restore_files(backup_dir, destination_dir):
    shutil.rmtree(destination_dir)
    shutil.copytree(backup_dir, destination_dir)
    print("Restore SUCCESS!")

backup_dir = "C:/Users/bushum/Desktop/Module_3/test_backup"
destination_dir = "C:/Users/bushum/Desktop/Module_3/test"
restore_files(backup_dir, destination_dir)