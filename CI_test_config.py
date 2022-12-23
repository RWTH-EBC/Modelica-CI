import argparse
import os
import pathlib
import shutil
import toml


class CI_config(object):

    def __init__(self):
        """
        Don't change the self.<name>. But you can change the paths and file name
        [Whitelist_files]
        [Config_files]
        [templates for plots]
        [interact ci lists]
        [Folder]
        [Dymola_Python_Tests] + Parser Commands
        """
        toml_files = sorted(pathlib.Path('.').glob('**/**/config.toml'))
        toml_file = f'Dymola_python_tests{os.sep}config.toml'
        if len(toml_files) > 0:
            for l in toml_files:
                toml_file = l
                break
        else:
            toml_file = f'..{os.sep}Dymola_python_tests{os.sep}config.toml'
        data = toml.load(f'{toml_file}')
        self.dymola_ci_test_dir = data["CI_dir"]["dymola_ci_test_dir"].replace("/", os.sep)
        self.dymola_python_test_dir = data["CI_dir"]["dymola_python_test_dir"].replace("/", os.sep)
        # [Whitelist_files]
        self.wh_ci_dir = f'{self.dymola_ci_test_dir}{os.sep}{data["whitelist"]["wh_ci_dir"].replace("/", os.sep)}'
        self.wh_model_file = f'{self.wh_ci_dir}{os.sep}{data["whitelist"]["wh_model_file"].replace("/", os.sep)}'
        self.wh_simulate_file = f'{self.wh_ci_dir}{os.sep}{data["whitelist"]["wh_simulate_file"].replace("/", os.sep)}'
        self.wh_html_file = f'{self.wh_ci_dir}{os.sep}{data["whitelist"]["wh_html_file"].replace("/", os.sep)}'
        self.wh_ref_file = f'{self.wh_ci_dir}{os.sep}{data["whitelist"]["wh_ref_file"].replace("/", os.sep)}'
        # [Config_files]
        self.config_ci_dir = f'{self.dymola_ci_test_dir}{os.sep}{data["config_ci"]["config_ci_dir"].replace("/", os.sep)}'
        self.config_ci_exit_file = f'{self.config_ci_dir}{os.sep}{data["config_ci"]["config_ci_exit_file"].replace("/", os.sep)}'
        self.config_ci_new_ref_file = f'{self.config_ci_dir}{os.sep}{data["config_ci"]["config_ci_new_ref_file"].replace("/", os.sep)}'
        self.config_ci_new_create_ref_file = f'{self.config_ci_dir}{os.sep}{data["config_ci"]["config_ci_new_create_ref_file"].replace("/", os.sep)}'
        self.config_ci_changed_file = f'{self.config_ci_dir}{os.sep}{data["config_ci"]["config_ci_changed_file"].replace("/", os.sep)}'
        self.config_ci_ref_file = f'{self.config_ci_dir}{os.sep}{data["config_ci"]["config_ci_ref_file"].replace("/", os.sep)}'
        self.config_ci_eof_file = f'{self.config_ci_dir}{os.sep}{data["config_ci"]["config_ci_eof_file"].replace("/", os.sep)}'
        # [templates for plots]
        self.chart_dir = f'{self.dymola_ci_test_dir}{os.sep}{data["plot"]["chart_dir"].replace("/", os.sep)}'
        self.temp_chart_dir = f'{self.dymola_python_test_dir}{os.sep}{data["plot"]["temp_chart_dir"].replace("/", os.sep)}'
        self.temp_chart_file = f'{self.temp_chart_dir}{os.sep}{data["plot"]["temp_chart_file"].replace("/", os.sep)}'
        self.temp_index_file = f'{self.temp_chart_dir}{os.sep}{data["plot"]["temp_index_file"].replace("/", os.sep)}'
        self.temp_layout_file = f'{self.temp_chart_dir}{os.sep}{data["plot"]["temp_layout_file"].replace("/", os.sep)}'
        # [interact ci lists]
        self.ci_interact_dir = f'{self.dymola_ci_test_dir}{os.sep}{data["interact_ci_list"]["ci_interact_dir"].replace("/", os.sep)}'
        self.ci_interact_show_ref_file = f'{self.ci_interact_dir}{os.sep}{data["interact_ci_list"]["ci_interact_show_ref_file"].replace("/", os.sep)}'
        self.ci_interact_update_ref_file = f'{self.ci_interact_dir}{os.sep}{data["interact_ci_list"]["ci_interact_update_ref_file"].replace("/", os.sep)}'
        # [Folder]
        self.artifacts_dir = f'{self.dymola_ci_test_dir}{data["artifcats"]["artifacts_dir"].replace("/", os.sep)}'
        self.library_ref_results_dir = f'{data["artifcats"]["library_ref_results_dir"].replace("/", os.sep)}'
        self.library_resource_dir = f'{data["artifcats"]["library_resource_dir"].replace("/", os.sep)}'
        # [Dymola_Python_Tests]
        self.dymola_python_test_url = f'{data["Dymola_Python_Tests"]["dymola_python_test_url"]}'
        # [result folder]
        self.result_dir = f'{self.dymola_ci_test_dir}{os.sep}{data["result"]["result_dir"].replace("/", os.sep)}'
        self.result_whitelist_dir = f'{self.result_dir}{os.sep}{data["result"]["result_whitelist_dir"].replace("/", os.sep)}'
        self.result_config_dir = f'{self.result_dir}{os.sep}{data["result"]["result_config_dir"].replace("/", os.sep)}'
        self.result_plot_dir = f'{self.result_dir}{os.sep}{data["result"]["result_plot_dir"].replace("/", os.sep)}'
        self.result_syntax_dir = f'{self.result_dir}{os.sep}{data["result"]["result_syntax_dir"].replace("/", os.sep)}'
        self.result_regression_dir = f'{self.result_dir}{os.sep}{data["result"]["result_regression_dir"].replace("/", os.sep)}'
        self.result_interact_ci_dir = f'{self.result_dir}{os.sep}{data["result"]["result_interact_ci_dir"].replace("/", os.sep)}'
        self.result_ci_template_dir = f'{self.result_dir}{os.sep}{data["result"]["result_ci_template_dir"].replace("/", os.sep)}'
        self.result_check_result_dir = f'{self.result_dir}{os.sep}{data["result"]["result_check_result_dir"].replace("/", os.sep)}'
        # [Color]

        self.CRED = '\033[91m'
        self.CEND = '\033[0m'
        self.green = '\033[0;32m'
        self.yellow = '\033[33m'
        self.blue = '\033[44m'

    def check_arguments_settings(self, argument_list: list):
        if len(argument_list) > 0:
            for arg in argument_list:
                if arg is None:
                    print(f'{self.CRED}Error:{self.CEND} {arg} is missing!')
                    exit(1)
                else:
                    print(f'Setting:  {arg}')

    @staticmethod
    def check_path_settings(path_list: list):
        if len(file_list) > 0:
            for path in path_list:
                if os.path.isdir(path) is True:
                    print(f'Setting path: {path}')
                else:
                    print(f'Cannot find  path {path}')
                    exit(1)

    @staticmethod
    def check_file_settings(file_list: list):
        if len(file_list) > 0:
            for file in file_list:
                if os.path.isfile(file) is True:
                    print(f'Setting path: {file}')
                else:
                    print(f'Cannot find  path {file}')
                    exit(1)

    def prepare_data(self, path_list: list, file_path_dict: dict, del_flag=False):
        """
            Args:
            path_list (): path where files are saved
            file_path_dict (): {dst:src,}
            del_flag (): True: delete file, False dont delete file
        """
        print(f'\n{self.blue}**** Prepare Data ****{self.CEND}\n')
        if len(path_list) > 0:
            self.prepare_data_path(path_list=path_list)
        if len(file_path_dict) > 0:
            self.prepare_data_files(file_path_dict=file_path_dict)
            if del_flag is True:
                self.remove_files(file_path_dict=file_path_dict)
        print(f'\n{self.blue}**********************{self.CEND}\n')

    def check_ci_file_structure(self, files_list):
        """
        Args:
            files_list ():
        """
        print(f'\n**** Create file structure ****\n')
        for file in files_list:
            if os.path.exists(file):
                print(f'{file} does exist.')
            else:
                print(f'File {file} does not exist. Create a new one under {file}')
                write_file = open(file, "w+")
                if file is self.config_ci_eof_file:
                    write_file.write(f'y\ny\ny\ny\ny\ny\ny\ny\ny\ny\ny\ny\ny\ny\ny\ny\ny\ny\ny\n')
                write_file.close()
        print(f'\n**********************\n')

    def check_ci_structure(self, files_list, folders_list):
        self.check_ci_folder_structure(folders_list=folders_list)
        self.check_ci_file_structure(files_list=files_list)

    @staticmethod
    def prepare_data_path(path_list):
        for path in path_list:
            try:
                if not os.path.exists(path):
                    print(f'Create path: {path}')
                    os.makedirs(path)
                else:
                    print(f'Path "{path}" exist.')
            except FileExistsError:
                print(f'Find no folder')
                pass

    @staticmethod
    def remove_files(file_path_dict):
        for file in file_path_dict:
            if os.path.exists(file):
                if os.path.isfile(file) is True:
                    os.remove(file)
                    print(f'Remove file: {file}')
                else:
                    print(f'File {file} does not exist')
            if os.path.isdir(file) is True:
                os.rmdir(file)
                print(f'Remove folder: {file}')

    @staticmethod
    def prepare_data_files(file_path_dict):
        for src in file_path_dict:
            if os.path.isfile(src) is True:
                file = src[src.rfind(os.sep) + 1:]
                dst = f'{file_path_dict[src]}{os.sep}{file}'
                shutil.copyfile(src, dst)
                print(f'Result file {src} was moved to {dst}')
                continue
            if not os.path.exists(f'{file_path_dict[src]}'):
                if os.path.isdir(src) is True:
                    print(f'Result Folder {src} was moved to {file_path_dict[src]}')
                    shutil.copytree(src, f'{file_path_dict[src]}')
                    continue
            else:
                print(f'File {src} not found')

    @staticmethod
    def return_file_list():
        """
        Returns:
        """
        files_list = []
        file_dic = (vars(CI_config()))
        for file in file_dic:
            if file.find("_file") > -1:
                files_list.append(file_dic[file])
        return files_list

    @staticmethod
    def return_file_dir():
        dir_list = []
        dir_dic = (vars(CI_config()))
        for dirs in dir_dic:
            if dirs.find("_dir") > -1:
                dir_list.append(dir_dic[dirs])
        return dir_list

    @staticmethod
    def check_ci_folder_structure(folders_list):
        """
        Check CI Structure
        """
        for folder in folders_list:
            if not os.path.exists(folder):
                print(f'Create path:{folder}')
                os.makedirs(folder)
            else:
                print(f'Path exist: {folder} ')

    @staticmethod
    def create_folder(path):
        """
        Args:
            path ():
        """
        try:
            if not os.path.exists(path):
                print(f'Create path: {path}')
                os.makedirs(path)
            else:
                print(f'Path "{path}" exist.')
        except FileExistsError:
            print(f'Find no folder')
            pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Set files or dictionaries")
    check_test_group = parser.add_argument_group("Arguments to build files or folders")
    check_test_group.add_argument("-CM", "--changed-model", default=False, action="store_true")
    check_test_group.add_argument("--ci-interactive", default=False, action="store_true")
    check_test_group.add_argument("--create-ref", default=False, action="store_true")
    check_test_group.add_argument("--create-whitelist", default=False, action="store_true")
    args = parser.parse_args()
    conf = CI_config()
    folder_list = list()
    file_list = list()
    if args.changed_model is True:
        folder_list = [conf.config_ci_dir]
        file_list = [conf.config_ci_changed_file, conf.config_ci_exit_file]
        pass
    if args.ci_interactive is True:
        folder_list = [conf.config_ci_dir]
        file_list = [conf.config_ci_eof_file, conf.config_ci_changed_file]
        pass
    if args.create_ref is True:
        folder_list = [conf.config_ci_dir]
        file_list = [conf.config_ci_eof_file, conf.config_ci_exit_file, conf.config_ci_new_create_ref_file]
        pass
    if args.create_whitelist is True:
        folder_list = [conf.dymola_ci_test_dir, conf.wh_ci_dir]
        file_list = [conf.wh_model_file, conf.wh_simulate_file, conf.wh_html_file, conf.wh_ref_file]
        pass
    conf.check_ci_folder_structure(folders_list=folder_list)
    conf.check_ci_file_structure(files_list=file_list)
