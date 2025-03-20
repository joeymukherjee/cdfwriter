API
===

.. autosummary::
   :toctree: generated

   cdfwriter

Class Description and Methods
-----------------------------
For reference, in each of the qualified names below:

::

  cdfwriter is the name of the Python package
  interface is the name of the Python source file
  CDFWriter is the name of the class defined
  
  and the text after the last period (.) is the name 
  of the method defined for the CDFWriter class

Class Description:

* :py:class:`cdfwriter.interface.CDFWriter`

Class Constructor:

* :py:func:`cdfwriter.interface.CDFWriter.__init__`  
  
The constructor is not usually called directly as named above, but rather like this:

newcdf = cdfwriter.CDFWriter(prefix, outputdir)

Methods Description:

* :py:func:`cdfwriter.interface.CDFWriter.add_constant`
* :py:func:`cdfwriter.interface.CDFWriter.add_constant_data`
* :py:func:`cdfwriter.interface.CDFWriter.add_global_attribute`
* :py:func:`cdfwriter.interface.CDFWriter.add_plot_variable_attributes`
* :py:func:`cdfwriter.interface.CDFWriter.add_support_variable_attributes`
* :py:func:`cdfwriter.interface.CDFWriter.add_variable`
* :py:func:`cdfwriter.interface.CDFWriter.add_variable_attribute`
* :py:func:`cdfwriter.interface.CDFWriter.add_variable_data`
* :py:func:`cdfwriter.interface.CDFWriter.clone_variable`
* :py:func:`cdfwriter.interface.CDFWriter.close`
* :py:func:`cdfwriter.interface.CDFWriter.close_record`
* :py:func:`cdfwriter.interface.CDFWriter.get_last_cdf_filename`
* :py:func:`cdfwriter.interface.CDFWriter.make_new_file`
* :py:func:`cdfwriter.interface.CDFWriter.set_do_not_split`
* :py:func:`cdfwriter.interface.CDFWriter.set_output_directory`
* :py:func:`cdfwriter.interface.CDFWriter.set_version_number`
* :py:func:`cdfwriter.interface.CDFWriter.set_file_naming_convention`

Coding Example
--------------
To help get one started, the developer is referred to the :ref:`example program <example_code>` developed to create
CDF data files based upon data contained in a CSV file.
