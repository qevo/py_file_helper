Welcome to file_helper's documentation!
=======================================

.. toctree::
    :name: mastertoc
    :hidden:

    file_helper
    tests
    changelog
    sphinx
    sphinx.conf
    sphinx.makefile
    package.setup
    pandoc

This helper module is a simple set of functions that make some file related activities easier.

Install
-------
.. code-block:: bash

    pip install git+git://github.com/qevo/py_file_helper.git

.. note:: Retrieve a copy of the source from `the GitHub repo <https://github.com/qevo/py_file_helper>`_.

Features
--------
Manage files
````````````
* List files and/or directories in a branch directory

  * recursive or non-recursive
  * recursion depth

* Find files

  * simple wildcard search
  * regular expressions search

File operations
```````````````
* Get the hash of a file's contents
* Read a file in binary mode, allowing for a given read length from a given position
* Slice a file
* Write a file in binary mode, allowing for a given start position anywhere in the file

  * Allows for appends, insertions, and overwrites

Dependencies
------------
* data_helper
    * `Documentation <http://py-data-helper.readthedocs.org/>`_
    * `Git repo <https://github.com/qevo/py_data_helper/>`_

API Documentation
-----------------
.. important:: Read the :doc:`change log <changelog>`.

.. toctree::
    file_helper
    tests

Notes
-----
* This project uses :doc:`Sphinx <sphinx>` and :doc:`Pandoc <pandoc>` for its documentation generation.
    .. toctree::
        :titlesonly:

        sphinx.conf
        sphinx.makefile
        package.setup
        pandoc

License
-------
The MIT License (MIT)

Copyright (c) 2015 Qevo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
