import os
import shutil
from ci_test_config import ci_config


class Prepare_result_class(ci_config):
    def __init__(self):
        super().__init__()


    def remove_files(self, file):
        os.remove(file)
        print(f'Remove file: {file}')

    def prepare_data_path(self, path):
        try:
            if not os.path.exists(path):
                print(f'Create path: {path}')
                os.makedirs(path)
            else:
                print(f'Path "{path}" exist.')
        except FileExistsError:
            print(f'Find no folder')
            pass

    def prepare_data_files(self, file_path_dict):
        for file in file_path_dict:
            print(file)





if __name__ == '__main__':

    pass