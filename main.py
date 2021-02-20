import xrf_package.init as xrf

# Call read function.
line = xrf.read_emsa_file("EDS_1.emsa")

# Print line list to check the data is there.
for i in line:
    print(i)