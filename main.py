import xrf_package.xrf_package as xrf

# Call extract_info.py to get the headers and data lists.
header_list, spectrum_data = xrf.extract_info(True, "EDS_1.emsa")

# Print headers.
for i in range(len(header_list)):
     print(header_list[i][0], header_list[i][1])

# Print data from spectrum_data.
for i in spectrum_data:
    print(i)