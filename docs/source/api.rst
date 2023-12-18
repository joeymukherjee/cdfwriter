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

* :py:func:`cdfwriter.interface.CDFWriter.addConstant`
* :py:func:`cdfwriter.interface.CDFWriter.addConstantData`
* :py:func:`cdfwriter.interface.CDFWriter.addGlobalAttribute`
* :py:func:`cdfwriter.interface.CDFWriter.addPlotVariableAttributes`
* :py:func:`cdfwriter.interface.CDFWriter.addSupportVariableAttributes`
* :py:func:`cdfwriter.interface.CDFWriter.addVariable`
* :py:func:`cdfwriter.interface.CDFWriter.addVariableAttribute`
* :py:func:`cdfwriter.interface.CDFWriter.addVariableData`
* :py:func:`cdfwriter.interface.CDFWriter.cloneVariable`
* :py:func:`cdfwriter.interface.CDFWriter.close`
* :py:func:`cdfwriter.interface.CDFWriter.closeRecord`
* :py:func:`cdfwriter.interface.CDFWriter.getLastCDFFilename`
* :py:func:`cdfwriter.interface.CDFWriter.makeNewFile`
* :py:func:`cdfwriter.interface.CDFWriter.setDoNotSplit`
* :py:func:`cdfwriter.interface.CDFWriter.setOutputDirectory`
* :py:func:`cdfwriter.interface.CDFWriter.setVersionNumber`

Coding Example
--------------
To help get one started, the developer is referred to the :ref:`example program <example_code>` developed to create
CDF data files based upon data contained in a CSV file.
