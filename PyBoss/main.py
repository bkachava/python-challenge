#Script to convert employee records to the required format

#modules to read the csvs and write the csv with the results
import os
import csv

# The sets of employee records are called employee_data1.csv and 
# employee_data2.csv. They must be located in the folder Resources
employee1_csv = os.path.abspath("Resources\\employee_data1.csv")
employee2_csv = os.path.abspath("Resources\\employee_data2.csv")

try:
    # Code that might cause an exception
    # Read the first file and store the content in a temporal list
    with open(employee1_csv, newline='') as csvfile:  
        csvreader = csv.reader(csvfile, delimiter=',')
        csv_header = next(csvreader)
        employees1 = list(csvreader)

    # Read the second file and store the content in a temporal list
    with open(employee2_csv, newline='') as csvfile:  
        csvreader = csv.reader(csvfile, delimiter=',')
        csv_header = next(csvreader)
        employees2 = list(csvreader)

    # Join the temporal lists
    employees = employees1 + employees2

except FileNotFoundError:
    # Code to be ejecuted in case the FileNotFoundError exception arises
    print("employee_data1 path=" + str(os.path.abspath("Resources\\employee_data1.csv")))
    print("employee_data2 path=" + str(os.path.abspath("Resources\\employee_data2.csv")))
    print("Please check the path of the files.")

else:
    # Code to be ejecuted if the try block was successful
    us_state_abbrev = {
        'Alabama': 'AL',
        'Alaska': 'AK',
        'Arizona': 'AZ',
        'Arkansas': 'AR',
        'California': 'CA',
        'Colorado': 'CO',
        'Connecticut': 'CT',
        'Delaware': 'DE',
        'Florida': 'FL',
        'Georgia': 'GA',
        'Hawaii': 'HI',
        'Idaho': 'ID',
        'Illinois': 'IL',
        'Indiana': 'IN',
        'Iowa': 'IA',
        'Kansas': 'KS',
        'Kentucky': 'KY',
        'Louisiana': 'LA',
        'Maine': 'ME',
        'Maryland': 'MD',
        'Massachusetts': 'MA',
        'Michigan': 'MI',
        'Minnesota': 'MN',
        'Mississippi': 'MS',
        'Missouri': 'MO',
        'Montana': 'MT',
        'Nebraska': 'NE',
        'Nevada': 'NV',
        'New Hampshire': 'NH',
        'New Jersey': 'NJ',
        'New Mexico': 'NM',
        'New York': 'NY',
        'North Carolina': 'NC',
        'North Dakota': 'ND',
        'Ohio': 'OH',
        'Oklahoma': 'OK',
        'Oregon': 'OR',
        'Pennsylvania': 'PA',
        'Rhode Island': 'RI',
        'South Carolina': 'SC',
        'South Dakota': 'SD',
        'Tennessee': 'TN',
        'Texas': 'TX',
        'Utah': 'UT',
        'Vermont': 'VT',
        'Virginia': 'VA',
        'Washington': 'WA',
        'West Virginia': 'WV',
        'Wisconsin': 'WI',
        'Wyoming': 'WY',
    }
    trans_emp = []

    for record_emp in employees:
        # The Name column should be split into separate First Name and Last Name columns.
        name = list(record_emp[1].split(" "))
        # print("Name" + record_emp[1])
        # print(name)
        # Transform the format of date of birth into MM/DD/YYYY 
        date_birth = record_emp[2][-5:].replace("-","/") + "/" + record_emp[2][:4]
        # print(date_birth)
        # The SSN data should be re-written such that the first five numbers are hidden from view.
        ss_num = '***-**-' + record_emp[3][-4:]
        # print(ss_num)
        # The State data should be re-written as simple two-letter abbreviations.
        abrev_state = us_state_abbrev.get(record_emp[4])
        # print(abrev_state)
        trans_emp.append([record_emp[0],name[0],name[1],date_birth,ss_num,abrev_state])


# Specify the file to write to
output_path = os.path.abspath("Output\\employee_data_new.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:
    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')
    # Write the first row (column headers)
    csvwriter.writerow(['Emp ID','First Name','Last Name','DOB','SSN','State'])

    for line in trans_emp:
        # Write the second row
        csvwriter.writerow(line)
    
    # Message to indicate that the process has finished and the location of the new file
    print("The new file with " + str(len(employees)) + " employees is located in: " + str(output_path))
