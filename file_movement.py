from os import listdir, mkdir, stat, path
from datetime import date
from shutil import move


class FileMover:

    def __init__(self, folder_path, file_formats, file_age):
        self.file_formats = file_formats
        self.file_age = file_age
        self.path_extractor(folder_path)

    def path_extractor(self, dir_path):
        print('path_extractor')
        print(dir_path)
        for item in listdir(dir_path):
            path_item = dir_path + item
            #print(path_item)
            #print(path.isfile(path_item))
            if path.isfile(path_item):
            #    print('if')
                self.file_move(path_item)
            # elif path.islink(path_item):
            #     print('elif')
            #     file_move(path_item)
            else:
                print('else')
                self.path_extractor(path_item+'/')

    def file_move(self, file_path):
        #print('file_move and file_path', file_path)
        print(path.splitext(file_path))
        pass
