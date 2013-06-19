What is tiff_collector?
-----------------------

**tiff_collector** is a script for managing TIFF files. It looks for files with extension `\*.tif` or `\*.tiff` in subdirectories and copies them to the current directory. The script recursively scans subdirectories, but there's a limit to the recursion: it won't copy any files that are more than two levels deep.

For example, ``./a/img_001.tif`` would be copied to ``./a_img_001.tif`` and ``./a/b/img_002.tif`` would be copied to ``./a_b_img_002.tif``, but ``./a/b/c/img_001.tif`` will not be copied because it's three levels deep.


tiff_collector structure
------------------------

Currently tiff_collector consists of the following files and directories:

  README.rst
    (this document)

  subdir_tiff_collector.py
    the script that does the actual TIFF file wrangling

  test_tiff_collector.py
    a few simple test scenarios

Web sites
---------

Binary versions of the script are available at
    http://geoffrollins.com/code.html


License information
-------------------

See the file "LICENSE" for information terms & conditions for usage and a DISCLAIMER OF ALL WARRANTIES.

