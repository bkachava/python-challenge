# PyBoss - Python Challenges 

In this challenge, a company recently decided to purchase a new HR system, that requires employee records be stored
in a specific format, therefore a Python script to convert the employee records to the required format was created. 

The resulting [Python script](main.py) does the following:
 - Import the [employee_data1.csv](Resources/employee_data1.csv) and [employee_data2.csv](Resources/employee_data2.csv) files, 
 which holds employee records like: Emp ID,Name,DOB,SSN,State.

 - Convert and export the data to use the following format: Emp ID,First Name,Last Name,DOB,SSN,State, making the 
 required conversions as follows:
   * The Name column should be split into separate First Name and Last Name columns.
   * The DOB data should be re-written into MM/DD/YYYY format.
   * The SSN data should be re-written such that the first five numbers are hidden from view.
   * The State data should be re-written as simple two-letter abbreviations.

 - Use a Python Dictionary for [State Abbreviations](https://gist.github.com/afhaque/29f0f4f37463c447770517a6c17d08f5).
 
 The script generates a csv file with the [results](Output/employee_data_new.csv).
