import os
import shutil

source_folder = r'from path' + '\\'
target_folder = r'to path' + '\\'


def move_files(sourceFolder, targetFolder):
    try:
        for path, dir, files in os.walk(sourceFolder):
            if files:
                for file in files:
                    if not os.path.isfile(targetFolder + file):
                        os.rename(path + '\\' + file, targetFolder + file)              
        print('All files moved')
    except Exception as e:
        print(e)

move_files(source_folder, target_folder)
