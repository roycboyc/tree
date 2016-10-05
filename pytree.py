# -*- coding: utf-8 -*-
import sys
import os

unicode_line = "│   "
unicode_cont = "├── "
unicode_end = "└── "
space_sign = "    "

# this function goes along a folder in the root and prints it (or summons itself to print a directory in it)
# https://www.tutorialspoint.com/python/os_listdir.htm
def tree_print(path, shape, count):
    dir_list = os.listdir(path)
           
    # remove files or directories
    dir_list = list(filter(lambda key: not key.startswith('.'), dir_list))
    dir_list = sorted(dir_list, key = lambda x: x.lower())   # removed key = sub_me to test

    # iterate over all of the files and directories in this one
    for file_name in dir_list:

        # extract the path name for this file in prep for recursion
        full_path = str(path) + '/' + str(file_name)

        # if this is the last file
        if file_name == dir_list[len(dir_list) - 1]:
            print(shape + unicode_end + file_name)
            next_shape = space_sign
        else:   # if not, print the cont_shape and assign the next shape as line
            print(shape + unicode_cont, file_name)
            next_shape = unicode_line   # the line(s) will be printed once the next file in this folder is called
        # if this is a directory, count it in the dict and apply the function to it
        if os.path.isdir(full_path):
            count['directories'] += 1
            tree_print(file_name, shape + next_shape, count)
        # if not a dir, just count files for final printout
        else:   
        	count['files'] += 1
    
if __name__ == '__main__':
    count = {'directories': 0, 'files': 0}
    
    if len(sys.argv) > 2:
    	print('invalid path')
    	sys.exit(0)
    elif len(sys.argv) == 2:
		sys_path = sys.argv[1]
    elif len(sys.argv) == 1:
    	sys_path = '.'
    elif len(sys.argv) == 0:
    	print('idk')
    	sys.exit(0)

    print (sys_path)
    tree_print(sys_path, '', count)

    print
    print("%s directories, %s files" (count['directories'], count['files']))
