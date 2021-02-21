import numpy as np
import xrf_package.xrf_package as xrf

# Call extract_info.py to get the headers and data lists.
header_list, spectrum_data = xrf.extract_info(True, "EDS_1.emsa")

# Locate "#XPERCHAN" and "#OFFSET".
XPERCHAN = xrf.locate_header_info(header_list, "#XPERCHAN")
OFFSET = xrf.locate_header_info(header_list, "#OFFSET")

# Print results.
print("Header: ", XPERCHAN[0], "has value : ", XPERCHAN[1])
print("Header: ", OFFSET[0], "has value : ", OFFSET[1])