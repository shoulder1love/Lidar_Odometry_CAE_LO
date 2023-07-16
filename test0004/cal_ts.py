
# Define the paths for the input and output files
input_file_path = "ts_modi.txt"
output_file_path = "ts_modi_s.txt"

# Read the input file
with open(input_file_path, "r") as input_file:
    lines = input_file.readlines()

# Convert each line to scientific notation and create the result
result = []

for line in lines:
    number = float(line.strip())
    scientific_notation = "{4f:.2e}".format(number)
    result.append(scientific_notation)

# Save the result to the output file
with open(output_file_path, "w") as output_file:
    output_file.write("\n".join(result))
exit()
input_file_path = "ts.txt"
output_file_path = "ts_modi.txt"

# Read the input file
with open(input_file_path, "r") as input_file:
    lines = input_file.readlines()

# Perform subtraction on each line and create the result
result = []
previous_number = None

for line in lines:
    number = float(line.strip())
    
    if previous_number is not None:
        difference = number - previous_number
        result.append(str(difference))
    
    previous_number = number

# Save the result to the output file
with open(output_file_path, "w") as output_file:
    output_file.write("\n".join(result))