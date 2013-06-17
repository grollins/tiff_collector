import nose.tools
import os
import random
import shutil
import glob
import fnmatch
import subfolder_tiff_collector

@nose.tools.istest
def tiff_files_copied_from_subdirs_to_execution_dir():
    # 1. create a temporary directory for the test
    temp_dir_path = 'my_test_dir%d' % random.randint(1, 1000)

    # 2. copy test data and tiff script to test directory
    shutil.copytree('test_data', temp_dir_path)
    shutil.copy('subfolder_tiff_collector.py', temp_dir_path)
    os.chdir(temp_dir_path)

    # 3. run the script
    subfolder_tiff_collector.main()

    # 4. check that the tif files have been copied
    tifs_in_exec_dir = glob.glob('*.tif')
    for dirpath, dirnames, files in os.walk('.'):
        if dirpath is '.':
            continue
        else:
            for f in fnmatch.filter(files, '*.tif'):
                dirname = os.path.basename(dirpath)
                expected_filename = '_'.join([dirname, f])
                error_msg = "In %s, %s does not appear to have been copied"\
                            " to execution directory as %s."\
                            % (dirpath, f, expected_filename)
                nose.tools.ok_(expected_filename in tifs_in_exec_dir,
                               error_msg)

    # 5. delete the temporary directory
    os.chdir('..')
    shutil.rmtree(temp_dir_path)

@nose.tools.istest
def tiff_files_not_copied_from_subsubdirs_to_execution_dir():
    # 1. create a temporary directory for the test
    temp_dir_path = 'my_test_dir%d' % random.randint(1, 1000)

    # 2. copy test data and tiff script to test directory
    shutil.copytree('test_data2', temp_dir_path)
    shutil.copy('subfolder_tiff_collector.py', temp_dir_path)
    os.chdir(temp_dir_path)

    # 3. run the script
    subfolder_tiff_collector.main()

    # 4. check that the tif files have been copied
    tifs_in_exec_dir = glob.glob('*.tif')
    subsubdir_filename = '01_sub01_img_005.tif'
    error_msg = "Did not expect %s to be copied"\
                " to execution directory as %s."\
                % ('01/sub01/img_005.tif', subsubdir_filename)
    nose.tools.ok_(not subsubdir_filename in tifs_in_exec_dir, error_msg)

    # 5. delete the temporary directory
    os.chdir('..')
    shutil.rmtree(temp_dir_path)
