# -*- coding: utf-8 -*-
import sys
import os

unicode_line="│   "
unicode_cont="├── "
unicode_end= "└── "
space_sign="    "

#this function goes along a folder in the root and prints it (or summons itself to print a directory in it)
#https://www.tutorialspoint.com/python/os_listdir.htm
def tree_print(path, shape, count):
    dir_list=os.listdir(path)
    
    #remove files or directories
    dir_list=list(filter(lambda key: not key.startswith('.'), dir_list))
    dir_list=sorted(dir_list, key=sub_me)

    #iterate over all of the files and directories in this one
    for file_name in dir_list:

        #extract the path name for this file in prep for recursion
        full_path = path + '/' + file_name

        #if this is the last file (an index loop might be more sensible? had bugs with that)
        if file_name == dir_list[len(files)-1]:
            print(shape+unicode_end+file_name)
            next_shape=space_sign

        else: #if not, print the cont_shape and assign the next shape as line
            print(shape+unicode_cont,file_name)
            next_shape=unicode_line
            
        if os.path.indir(full_path): #if this is a directory, count it in the dict and apply the function to it
            count['directories']+=1
            tree_print(file_name,shape+next_shape,count)

        else: #if not a dir, just count files for final printout
            count['files']+=1

#this function helps the sorting in the tree_print function    
def sub_me(dir_name):
    #if the first character is a letter, return it in lower case
    if dir_name[0].isalpha:
        return dir_name.lower()
    #if it's not, find the first character that is, and return it lower case
    else:
        for i in range(len(dir_name)):
            if dir_name[i].isalpha():
                former=dir_name[:i]
                rest_of=dir_name[i:].lower()
                ret=former+rest_of
                return ret
            else:
                continue
    
if __name__ == '__main__':
    count = {'directories':0, 'files':0}
    
    if len(sys.argv==1)
        sys_path='.'
    elif len(sys.argv==2):
        sys_path=sys.argv[1]
    else:
        print ('invalid path')
        sys.exit(0)
        
    print (sys_path)
    tree_print(sys_path, "", count)
    
    print(str(count['directories']), ' directories, ', str(count['files']), ' files ')