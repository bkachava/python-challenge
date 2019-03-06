# Script to automate the analysis of any passage using the following metrics:
#    Approximate word count
#    Approximate sentence count
#    Approximate letter count (per word)
#    Average sentence length (in words)

#module to read the txt
import os
#module to calculate the sentences using the dot
import re

def average_letter(word_list):
    count = 0
    
    # Calculate the sum of the length of the words 
    for word in word_list:
        count += len(word)
    
    # Return the average of the words or the sentences
    return count / len(word_list)

def average_sentence(sentence_list):
    count = 0
    
    # Calculate the sum of the length of the words in the sentences
    for sentence in sentence_list:
        words = list(filter(None,sentence.split(" ")))
        count += len(words)

    # Return the average of sentence length (in words)
    return count / len(sentence_list)

# Import a text file with a paragraph - There are 3 examples in the folder Resources
# To test each file is necessary to remove the corresponding comment tag
input_file = os.path.abspath("Resources\\paragraph.txt")
# input_file = os.path.abspath("Resources\\paragraph_1.txt")
# input_file = os.path.abspath("Resources\\paragraph_2.txt")

try:
    # Code that might cause an exception
    # open the output file and write the results
    with open(input_file, "r", encoding='utf-8') as text_file:
        parag_file = text_file.read()

except FileNotFoundError:
    # Code to be ejecuted in case the FileNotFoundError exception arises
    print("path=" + str(os.path.abspath("Resources\\paragraph.txt")))
    print("Please check the path of the file.")

else:
    # Code to be ejecuted if the try block was successful
    
    # Calculate the approximate word count
    word_count = list(filter(None,parag_file.split(" ")))
    
    # Calculate the approximate sentence count
    if any("\n" in s for s in parag_file):
        # Check if the file has break lines for calculating the sentences
        sentence_count = list(filter(None,parag_file.split("\n")))
    else:
        # Otherwise the dot will be used for calculating the sentences
        sentence_count = list(re.split("(?<=[.!?]) +", parag_file))
    
    # Calculate the approximate letter count (per word)
    avg_let_count = round(average_letter(word_count),1)
    
    # Calculate the average sentence length (in words)
    avg_sent_count = round(average_sentence(sentence_count),1)
    
    print("Paragraph Analysis\n-----------------")
    print("Approximate Word Count: " + str(len(word_count)))
    print("Approximate Sentence Count: " + str(len(sentence_count)))
    print("Average Letter Count: " + str(avg_let_count))
    print("Average Sentence Length : " + str(avg_sent_count))