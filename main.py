import xrf_package.xrf_package as xrf

# Call read_emsa_file.py.
lines = xrf.read_emsa_file("EDS_1.emsa")

# Call extract_headers.py.
xrf.extract_headers(lines)