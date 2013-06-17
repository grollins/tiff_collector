import os, sys
import glob

'''
Run like this: "python the_culling_of_the_files.py"
Assumes: the tif files are in subfolders of the current directory.
'''

file_list = glob.glob("*/*.tif")
for f in file_list:
    file_name = os.path.basename(f)
    dir_name = os.path.dirname(f)
    new_file = "%s_%s" % (dir_name, file_name)
    os.system("cp %s %s" % (f, new_file))
    print "Copied %s to %s" % (f, new_file)
