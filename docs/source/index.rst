.. cdfwriter documentation master file, created by
   sphinx-quickstart on Mon Dec 11 18:34:37 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to cdfwriter's documentation!
=====================================

**cdfwriter** is a Python package developed at Southwest Research Institute that aims to provide a simple and efficient solution to generating CDF files.
It uses a high level Object-Oriented interface method that allows for the definition of a common set of CDF files that are similar.

The cdfwriter package uses `SpacePy.pycdf <https://spacepy.github.io/pycdf.html>`_
to write a common set of CDFs and makes use of the `NumPy <https://numpy.org/>`_ package.  **SpacePy** is a package for Python, targeted at the space sciences,
that aims to make basic data analysis, modeling and visualization easier. It builds on the capabilities of NumPy and MatPlotLib packages.

The documentation for **cdfwriter** describes the IO interface for writing CDF data in Python and is hosted on Read the Docs.

Refer to the :doc:`usage` section for further information, including how to :ref:`install <installation>` the project.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   usage
   api
   history

Indices
=======

* :ref:`genindex`
