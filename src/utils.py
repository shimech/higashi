import os
import shutil


class Utils:
    @staticmethod
    def make_dir(dirname):
        if os.path.isdir(dirname):
            pass
        else:
            os.makedirs(dirname)
        return dirname

    @staticmethod
    def remove_dir(dirname):
        shutil.rmtree(dirname, ignore_errors=True)
