"""
Copyright (c) 2013, Geoff Rollins
All rights reserved.
"""

import os
import fnmatch
import shutil

CUTOFF_DEPTH = 2  # won't copy files from subdirs deeper than this value
TEST_MODE = True  # if running tests with nosetests, set to True

def copy_tiffs_from_subdirs_to_exec_dir(noisy=False):
    """
    Recursively iterate through the subfolders of the execution directory
    and copy .tif and .tiff files to the execution directory.
    Subdirectories at a level deeper than `CUTOFF_DEPTH` will be ignored.
    """
    for dirpath, dirnames, files in os.walk('.'):
        if dirpath is '.':
            # don't process files that are already in the execution directory
            continue
        elif dirpath.count(os.sep) > CUTOFF_DEPTH:
            del dirnames[:]
            continue
        else:
            copy_files_with_name_pattern(dirpath, files, '*.tif', noisy)
            copy_files_with_name_pattern(dirpath, files, '*.tiff', noisy)

def copy_files_with_name_pattern(dirpath, files, pattern, noisy=False):
    """
    Copy the files in `files` from directory `dirpath` that match `pattern`
    to the current directory.

    Parameters
    ----------
    dirpath : string
        The path to the directory that contains `files`.
    files : list
        A list of files located in the directory given by `dirpath`.
    pattern : string
        Copy files that match this naming pattern string,
        e.g. `*.tif` or `*.txt`
    """
    for f in fnmatch.filter(files, pattern):
        basename = os.path.basename(f)
        old_file_path = os.path.join(dirpath, basename)
        prefix_list = make_prefix_list(dirpath)
        new_file_prefix = '_'.join(prefix_list)
        new_file_path = new_file_prefix + '_' + basename
        shutil.copy(old_file_path, new_file_path)
        if noisy:
            print "Copied %s to %s" % (old_file_path, new_file_path)

def make_prefix_list(dirpath):
    """
    Split `dirpath` into a list of subdir names.
    
    Parameters
    ----------
    dirpath : string

    Example
        input `'./a/b/c'`
        output `['a', 'b', 'c']`
    """
    done = False
    current_path = dirpath
    prefix_list = []
    i = 0
    while not done and i < CUTOFF_DEPTH:
        split_path = os.path.split(current_path)
        current_path = split_path[0]
        prefix_list.append(split_path[1])
        if current_path is '':
            done = True
        i += 1
    try:
        prefix_list.remove('.')
    except ValueError:
        pass
    prefix_list.reverse()
    return prefix_list

def main():
    if TEST_MODE:
        pass
    else:
        __location__ = os.path.realpath(
                        os.path.join(os.getcwd(), os.path.dirname(sys.argv[0])))
        os.chdir(__location__)
        print os.getcwd()
    copy_tiffs_from_subdirs_to_exec_dir(noisy=True)

if __name__ == '__main__':
    main()
