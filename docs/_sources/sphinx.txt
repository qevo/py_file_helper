Sphinx
======

.. toctree::
    :hidden:

    sphinx.conf
    sphinx.makefile

What Sphinx Is
--------------
Sphinx is a Python application for generating documentation. It uses reStructuredText as its markup language.

Visit the `Sphinx <http://sphinx-doc.org/>`_ website `<http://sphinx-doc.org/>`_


Why Sphinx is Used
------------------
* To generate API documentation from source code docstrings.
* To generate HTML pages from the reStructuredText files.

How Sphinx is Used
------------------
#. Create valid docstrings for code
#. `Install Sphinx <http://sphinx-doc.org/latest/install.html>`_
#. Create a docs folder
#. Navigate to the docs folder
#. Put a copy of the modified :doc:`Sphinx Makefile <sphinx.makefile>`
#. Put a copy of the modified :doc:`Sphinx Config <sphinx.conf>` (conf.py)
#. Create an index file: *index.rs\_*

    * This is the main page of the documentation and must include a table of contents
    * The file extension is required for non-code based files to work with the modified :doc:`Sphinx Makefile <sphinx.makefile>`

#. Generate the documenation
    .. code-block:: bash

        make html
