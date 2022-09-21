import os
import shutil

target_folder = r'C:\Users\Justin\Desktop\Freelance\Nick Kurz- Gifford Monument\03_PRODUCTION\Assets\Monument Images From Client\Monument_Images' + '\\'
source_folder = r'C:\Users\Justin\Desktop\Freelance\Nick Kurz- Gifford Monument\03_PRODUCTION\Assets\Monument Images From Client\Custom' + '\\'

# for path, dir, files in os.walk(source_folder):
#     if files:
#         for file in files:
#             if not os.path.isfile(target_folder + file):
#                 os.rename(path + '\\' + file, target_folder + file)


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