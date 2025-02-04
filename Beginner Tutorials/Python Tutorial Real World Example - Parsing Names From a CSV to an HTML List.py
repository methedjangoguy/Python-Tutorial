# Use CSV Module to parse names from csv file and convert to HTML list format
import csv

# First pass using basic CSV reader
basic_contributor_names = []  # List to store contributor names from basic reader
basic_html_content = ''  # String to store HTML output from basic reader

with open('patrons.csv', 'r') as data_file:
    csv_data = csv.reader(data_file)
    # Skip the header row containing column names
    next(csv_data)
    # Skip the blank row after header
    next(csv_data)

    # Process each row until 'No Reward' is found
    for row in csv_data:
        if row[0] == 'No Reward':
            break
        basic_contributor_names.append(f"{row[0]} {row[1]}")

# Generate initial HTML with contributor count
basic_html_content += f'<p>There are currently {len(basic_contributor_names)} public contributors. Thank you!</p>'

# Generate HTML list of contributors
basic_html_content += '\n<ul>'
for contributor in basic_contributor_names:
    basic_html_content += f'\n\t<li>{contributor}</li>'
basic_html_content += '\n</ul>'
print(basic_html_content)

# Second pass using DictReader for named columns
dict_contributor_names = []  # List to store contributor names from dict reader
dict_html_content = ''  # String to store HTML output from dict reader

with open('patrons.csv', 'r') as data_file2:
    csv_dict_data = csv.DictReader(data_file2)
    # Skip the header row
    next(csv_dict_data)
    # Skip the blank row
    next(csv_dict_data)

    # Process each row until 'No Reward' is found
    for row in csv_dict_data:
        if row['FirstName'] == "No Reward":
            break
        dict_contributor_names.append(f"{row['FirstName']} {row['LastName']}")

# Generate final HTML output
dict_html_content += (
    f"<p>There are currently {len(dict_contributor_names)} public contributors. Thank you!</p>"
)
dict_html_content += "\n<ul>"
for contributor in dict_contributor_names:
    dict_html_content += f"\n\t<li>{contributor}</li>"
dict_html_content += "\n</ul>"
print(dict_html_content)
