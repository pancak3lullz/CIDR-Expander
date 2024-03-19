import ipaddress

def expand_cidr_ranges(input_file_path, output_file_path):
    """
    Expand CIDR ranges from the input file and write each IP address to the output file.

    Args:
    input_file_path (str): The path to the file containing CIDR ranges, one per line.
    output_file_path (str): The path to the file where individual IP addresses will be written.
    """
    with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
        for cidr_range in input_file:
            cidr_range = cidr_range.strip()  # Clean up whitespace
            if not cidr_range:  # Skip empty lines
                continue
            try:
                network = ipaddress.ip_network(cidr_range, strict=False)  # Expand the CIDR range
                for ip in network.hosts():  # Write each IP address to the output file
                    output_file.write(str(ip) + '\n')
            except ValueError as e:  # Handle invalid CIDR ranges
                print(f"Skipping invalid CIDR range '{cidr_range}': {e}")

# Prompt the user for the input and output file paths
input_file_path = input("Enter the path to the input file containing the CIDR ranges: ")
output_file_path = input("Enter the path to the output file for the individual IP addresses: ")

expand_cidr_ranges(input_file_path, output_file_path)
