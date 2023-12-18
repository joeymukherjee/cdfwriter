Developer's Guide
=================

Welcome to the Developer's Guide for the **cdfwriter** python package.  The online documentation attempts to outline 
the steps necessary to begin generating python code to create CDF data files on a linux system using **cdfwriter**.

.. _installation:

Installing for development
--------------------------

Since **cdfwriter** makes use of the **SpacePy** and **NumPy** packages, install them using pip, in the following order:::

   $ pip install numpy
   $ pip install spacepy

then install **cdfwriter** using pip:::

   $ pip install cdfwriter

The final step involves installing the `Common Data Format (CDF) <https://cdf.gsfc.nasa.gov/>`_ software from the Space Physics Data Facility at Goddard Space Flight Center.
Instructions on how to download the software and the documentation are provided at https://cdf.gsfc.nasa.gov/html/sw_and_docs.html.

.. _code_std:

Standards and Conventions
-------------------------

A developer should be aware of the following standards / conventions needed in order to successfully utilize the **cdfwriter** package.

Language Standard
^^^^^^^^^^^^^^^^^^

* All code must be compatible with Python 3.6 and later.

Coding conventions
^^^^^^^^^^^^^^^^^^

* Some of the modules defined in the **cdfwriter** package are designated as private, meaning that they are only to be used internally, and are
  identified as such thru the use of the underscore (_) as the first character in their name, e.g., _this_function_is_private.  For the sake
  of this online documentation, the private members **are not** made visible.

* In the developer's python code, the following conventions must be observed:

  * According to `SpacePy.pycdf <https://spacepy.github.io/pycdf.html>`_ notes, the CDF C library must be properly installed.  If pycdf has trouble finding the library, try setting CDF_LIB before importing **cdfwriter**, e.g.

    | ``import os``
    | ``os.environ["CDF_LIB"] = "/SDDAS/hapi_src_build/_deps/cdffetch-src/lib"``
    | ``import cdfwriter``

  * Use **import** to include **pycdf**

    | ``from spacepy import pycdf``

Documentation
-------------

**cdfwriter** is a self-documented python package which makes use of **NumPy** style docstrings to generate this online html documentation.
Docstrings are present for all public classes and methods.  Here is a list of what is provided for each type:

* For the **CDFWriter** class

  * A description of the class
  * A definition of each variable associated with the class
  * The data type for each variable

* For the methods 

  * The calling sequence for the method
  * A description of what the method does
  * A description of each parameter, including its data type, indicating any default value that may be defined
  * A list of any exception that may be raised by the method
  * If the method is a function, a description of the return value, including its data type

