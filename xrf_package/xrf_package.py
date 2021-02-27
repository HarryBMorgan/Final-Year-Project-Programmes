# -----------------------------------------------------------------------------
# xrf_package.py

# -----------------------------------------------------------------------------
# Final Year Project - XRF Analysis
# Harry Morgan

# -----------------------------------------------------------------------------
# PROGRAMME DESCRIPTION
# This module holds all the XRF package modules for convinient importing.

# -----------------------------------------------------------------------------
# IMPORT
# Import the modules and name them accordingly for use in the main.py.

# Import extract_headers function.
from xrf_package.read_emsa_file import read_emsa_file
from xrf_package.extract_info import extract_headers, extract_data
from xrf_package.locate_header_info import locate_header_info