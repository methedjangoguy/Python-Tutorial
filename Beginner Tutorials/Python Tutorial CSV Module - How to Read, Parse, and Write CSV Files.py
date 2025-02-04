# Import the csv module to handle CSV file operations
import csv

# Open the input CSV file in read mode
with open('names.csv', 'r') as csv_file:
    # Create a CSV reader object to read data from the input file
    csv_reader = csv.reader(csv_file)
    # # Skip the header row if needed
    # next(csv_reader)
    # # Print the email column (3rd column) from each row
    # for line in csv_reader:
    #     print(line[2])

    # Open a new CSV file in write mode to store the transformed data
    with open('new_names.csv', 'w') as new_file:
        # Create a CSV writer object that will use tabs as delimiters instead of commas
        csv_writer = csv.writer(new_file, delimiter='\t')

        # Copy each row from the input file to the output file
        for line in csv_reader:
            csv_writer.writerow(line)


# Reopen the input file to process it using dictionary-based CSV handling
with open('names.csv', 'r') as csv_file:
    # Create a DictReader object that will automatically use the header row as keys
    csv_reader = csv.DictReader(csv_file)
    # Open the output file for writing the processed data
    with open('new_names.csv', 'w') as new_file:
        # Specify the column names for the output file
        fieldnames = ['first_name', 'last_name', 'email']
        # Create a DictWriter object that will write data using dictionary keys
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')
        # Write the column headers to the output file
        csv_writer.writeheader()
        # Process each row from input and write to output using dictionary format
        for line in csv_reader:
            csv_writer.writerow(line)

# Congatulations! You have compeleted CSV Module.
