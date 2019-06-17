# Python Challenges

These four challenges encompass real-world situations where my `Python` scripting skills came in handy.

##PyBank

In this challenge, a Python script for analyzing the financial records of a company was created. The financial [dataset](PyBank/Resources/budget_data.csv) is composed of two columns: Date and Profit/Losses.

The resulting [Python script](PyBank/main.py) calculates each of the following:
 - The total number of months included in the dataset
 - The net total amount of "Profit/Losses" over the entire period
 - The average of the changes in "Profit/Losses" over the entire period
 - The greatest increase in profits (date and amount) over the entire period
 - The greatest decrease in losses (date and amount) over the entire period

The script prints the analysis to the terminal and export a text file with the [results](PyBank/Output/results.txt).

##PyPoll

To help a small, rural town modernize its vote-counting process, a Python script was created. A set of [poll data](PyPoll/Resources/election_data.csv), with three columns: Voter ID, County, and Candidate; was used. 

The resulting [Python script](PyPoll/main.py) calculates each of the following:
 - The total number of votes cast
 - A complete list of candidates who received votes
 - The percentage of votes each candidate won
 - The total number of votes each candidate won
 - The winner of the election based on popular vote

The script prints the analysis to the terminal and export a text file with the [results](PyPoll/Output/results.txt).

##PyBoss

In this challenge, a company recently decided to purchase a new HR system, that requires employee records be stored in a specific format, therefore a Python script to convert the employee records to the required format was created. 

The resulting [Python script](PyBoss/main.py) does the following:
 - Import the [employee_data1.csv](PyBoss/Resources/employee_data1.csv) and [employee_data2.csv](PyBoss/Resources/employee_data2.csv) files, which holds employee records like: Emp ID,Name,DOB,SSN,State.

 - Convert and export the data to use the following format: Emp ID,First Name,Last Name,DOB,SSN,State, making the required conversions as follows:
   * The Name column should be split into separate First Name and Last Name columns.
   * The DOB data should be re-written into MM/DD/YYYY format.
   * The SSN data should be re-written such that the first five numbers are hidden from view.
   * The State data should be re-written as simple two-letter abbreviations.

 - Use a Python Dictionary for [State Abbreviations](https://gist.github.com/afhaque/29f0f4f37463c447770517a6c17d08f5).
 
 The script generates a csv file with the [results](PyBoss/Output/employee_data_new.csv).
 
 ##PyParagraph
 
A Python script to automate the analysis of differetn types of passages of writing was created. A simple set of metrics for assessing complexity was designed to automate the analysis of any passage 

The resulting [Python script](PyParagraph/main.py) does the following:
 - Import a text file filled with a paragraph. See [samples](PyParagraph/Resources).
 - Assess the passage for each of the following: 
   * Approximate word count
   * Approximate sentence count
   * Approximate letter count (per word)
   * Average sentence length (in words)
 
 The script prints the analysis to the terminal.
