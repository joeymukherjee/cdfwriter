.. _example_code:

Example Program
---------------
To help get one started, the python code below shows an example that reads information from
a CSV data file and generates a CDF file using the data read plus some pre-known information
relevant to the data set being processed.  In some cases, the python module is listed but
not all code is provided as this is to serve as somewhat as an outline.  Developers are
free to use this as a guide. ::

    import sys
    import csv
    import socket
    from datetime import datetime

    import os
    os.environ["CDF_LIB"] = "/SDDAS/hapi_src_build/_deps/cdffetch-src/lib"
    import cdfwriter
    from spacepy import pycdf

    #------------------------------------------------------------------------------------- 
    def createCDFWriter ():

        prefix = "ELSSCIH"          # name of data set being processed
        outputdir = "./"

        newcdf = cdfwriter.CDFWriter(prefix, outputdir)
        newcdf.set_version_number ("1.0.0")
        newcdf.set_do_not_split (True)
        newcdf.set_file_naming_convention ("%Y%m%d%H%M%S")
        return newcdf

    #-------------------------------------------------------------------------------
    def setGlobalAttributes (cdf):

        cdf.add_global_attribute ("Discipline", "Space Physics>Magnetospheric Science")
        cdf.add_global_attribute ("Source_name", "Venus_Express")
        cdf.add_global_attribute ("Descriptor", "ELSSCIH>ELS")
        cdf.add_global_attribute ("Data_type", "M1>Modified Data 1")

        # add more calls for other required/recommended CDF global attributes
        # Example of an attribute we define (user-defined) to describe data quality flags included 
        # in the data.

        dqual_keys = ['0: Good Data', '1: Questionable Data', '2: Invalid Data', '3: Bad Data', '4: Unknown State']
        cdf.add_global_attribute ("DQUAL_KEY", dqual_keys)

    #-------------------------------------------------------------------------------
    def setTiming (cdf, start_times, end_times):

        # convert strings read from CSV file to time stamps

        times_list = []
        numValues = len(start_times)
        for i in range(numValues):
            date_btime = datetime.strptime (start_times[i], '%Y:%j:%H:%M:%S.%f')
            times_list.append (date_btime)

        # Just use defaults for rest of the arguments for the Epoch variable.

        cdf.add_variable ("Epoch", pycdf.const.CDF_TIME_TT2000)
        validMin = datetime.strptime ("1990-01-01T00:00:00.000000", '%Y-%m-%dT%H:%M:%S.%f')
        validMax = datetime.strptime ("2050-01-01T00:00:00.000000", '%Y-%m-%dT%H:%M:%S.%f')
        cdf.add_support_variable_attributes ("Epoch", "Time Line", "Start Time for the record in nanoseconds", "ns",
                                             "E14.8", validMin, validMax, "Epoch", "1.0e-9>s", "linear")
        cdf.add_variable_attribute ("MONOTON","Epoch", "INCREASE")
        cdf.add_variable_attribute ("TIME_BASE","Epoch", "J2000")
        cdf.add_variable_attribute ("DELTA_MINUS_VAR", "Epoch", "Epoch_Start")
        cdf.add_variable_attribute ("DELTA_PLUS_VAR",  "Epoch", "Epoch_End")
        cdf.add_variable_data ("Epoch", times_list, True)

        # Epoch_Start variable does not change - set to 0

        recordVariance = False
        cdf.add_variable ("Epoch_Start", pycdf.const.CDF_REAL8, None, None, recordVariance)
        cdf.add_support_variable_attributes ("Epoch_Start", "Time Resolution", "Start time of record = Epoch - value",
                                             "ns", "E14.8", 0.00000000e+00, 3.16224000e+16, "dt", "1.0e-9>s", "linear")
        cdf.add_variable_data ("Epoch_Start", 0.0, True)

        # Now add a measurement (in nanoseconds), which will be the time to add to generate timetag that 
        # represents the end of this sample YYYY:DOY:HH:MM:SS.XXX

        my_delta_t = []
        for i in range(numValues):
            date_btime = datetime.strptime (start_times[i], '%Y:%j:%H:%M:%S.%f')
            date_etime = datetime.strptime (stop_times[i], '%Y:%j:%H:%M:%S.%f')
            time_diff = (date_etime - date_btime).total_seconds()
            time_diff = time_diff * 1e9
            my_delta_t.append (time_diff)

        sizes = [1]
        dimVariances = ['T']
        dimVariances = [0]
        cdf.add_variable ("Epoch_End", pycdf.const.CDF_REAL8)
        cdf.add_support_variable_attributes ("Epoch_End", "Time Resolution", "End time of record = Epoch + value",
                                             "ns", "E14.8", 0.00000000e+00, 3.16224000e+16, "dt", "1.0e-9>s", "linear")
        cdf.add_variable_data ("Epoch_End", my_delta_t, True)

    #-------------------------------------------------------------------------------
    def setDataVariables (cdf, sensor_names, units_labels, data_values_list, numRecords):

        str1 = "Data for ELSSCIH sensor "
        numSensors = len (sensor_names)
        for i in range (numSensors):
            sensor_name = sensor_names[i]
            cat_desc_str = str1 + sensor_name

            # Get the list of data values for the sensor in question

            sensor_data = []
            for idx in range (numRecords):
                index_val = (idx * numSensors) + i;
                data_row = data_values_list[index_val]
                numValues = len (data_row)
                sensor_data_numeric = [float(s) for s in data_row]
                sensor_data.append (sensor_data_numeric)

            # Define this sensor variable and add the data for this sensor
    
            sizes = [numValues]
            cdf.add_variable (sensor_name, pycdf.const.CDF_DOUBLE, sizes)
            validMin = -3.0e+38
            validMax = 3.0e+38
            cdf.add_plot_variable_attributes (sensor_name, sensor_name, cat_desc_str, "spectrogram", units_labels[i], "E13.6",
                                              units_labels[i], pycdf.const.CDF_DOUBLE, validMin, validMax, "log", False)
            fillValue = -3.4e+38
            cdf.add_variable_attribute ("FILLVAL", sensor_name, fillValue)
            cdf.add_variable_data (sensor_name, sensor_data, True)

    #-------------------------------------------------------------------------------
    def read_input_file(input_csv_filename):

        with open(input_csv_filename) as csvfile:
            # Read in csv data.
            try:
                datareader = csv.reader(csvfile, delimiter=',')
            except Exception as e:
                print (str(e))
                print ("Can't open csv data file: ", input_csv_filename)
                return -1

            # Skipping code to read the CSV file but showing what is returned to calling module,
            # which are vectors of start times, stop times, sensor names, units labels and the 
            # actual data values for each sensor

            for row in datareader:
                ....

            return input_vector_stime, input_vector_etime, input_vector_sensor_name, input_vector_units_label, input_vector_data_values_list

    #-------------------------------------------------------------------------------

    if __name__ == '__main__':

        start_times, stop_times, sensor_names, units_labels, data_values_list = read_input_file ("ELSSCIH20093170000_V1.0.CSV")
        num_time_tags = len (start_times)

        # The CDF file naming convention will be as follows:
        # ELSSCIH_YYYYMMDDHHMMSS_v1.0.0.cdf - if this file already exists from a previous run of this
        # program, a runtime error will be generated indicating this situation so the user must remove
        # the CDF file if repeated runs are made using the same input CSV file.

        # Now create a CDFWriter object and begin filling in the data retrieved from the CSV file.

        myCDF = createCDFWriter (output_fname_prefix)
        setGlobalAttributes (myCDF)

        setTiming (myCDF, start_times, stop_times)
        setDataVariables (myCDF, sensor_names, units_labels, data_values_list, num_time_tags)
        myCDF.close ()
        sys.exit ()
