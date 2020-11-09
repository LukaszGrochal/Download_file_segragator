from file_movement import FileMover

from os import listdir, mkdir, stat, path
from datetime import date
from shutil import move


folder_path = 'C:/Users/Grochal/Downloads/'
# files = listdir(folder_path,)
# for f in files:
#     print(f)
#     print(date.fromtimestamp(path.getctime(folder_path + f)))
#     time_calc = date.fromtimestamp
#     stats = stat(folder_path + f)
#     print(f'st_atime={time_calc(stats.st_atime)}, st_mtime={time_calc(stats.st_mtime)}, st_ctime={time_calc(stats.st_ctime)}')
#     print(stats)

# print(path.isfile('C:/Users/Grochal/Downloads/.ipynb_checkpoints/wum3z_Grochal_Łukasz_s10612 (1)-checkpoint.ipynb'))





if __name__ == '__main__':
    file_formats = {'pdf': ['pdf'], 'image': ['img', 'jpg', 'png'], 'video': [], 'audio': ['mp3'],
                    'text': ['txt', 'doc', 'xdoc'], 'csv': ['csv'], 'excel': ['xslx'], 'other': []}
    file_age = {'': 'this week old'}#

    FileMover(folder_path, file_formats, file_age)




