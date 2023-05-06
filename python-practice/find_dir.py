#!/usr/bin/python3
import os
"""
module searching for
a directory in a given
path
"""


class DirectorySearcher:
    def find(self, path, dir):
        try:
            os.chdir(path)
        except OSError:
            return
        current_dir = os.getcwd()
        for entity in os.listdir('.'):
            if entity == dir:
                print(os.getcwd() + '/' + dir)
            self.find(current_dir + '/' + entity, dir)

directory_searcher = DirectorySearcher()
dir_name = str(input("Enter the directory name to be navigate: "))
path_name = str(input("Enter the path name: "))
directory_searcher.find(path_name, dir_name)
