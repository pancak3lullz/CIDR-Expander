# CIDR-Expander
A quick python script for expanding a list of CIDR ranges into individual IP addresses within the specified subnets.

## How to Use the Script
This script processes each CIDR range, one per line, from the input file. It expands each range into the individual IP addresses that it encompasses and writes these addresses to the output file, one address per line. Make sure that the input file is correctly formatted, with one CIDR range per line, for the script to function properly.
1. When prompted, enter the full path to your input file that contains the CIDR ranges, one per line.
2. When prompted, enter the full path to the output file where you want the individual IP addresses to be saved.
3. Run the script in a Python 3 environment. The script will read each CIDR range from the input file, expand it into its constituent IP addresses, and write those addresses to the output file.
