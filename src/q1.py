"""HW6 Question 1: processing data using Pandas

Please use the dataset provided in spam.csv.
The original dataset is available at 
https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset
Please ignore the rows that do not follow the correct format.

Please implement a class called `SpamReader` that reads the dataset 
into a Pandas dataframe and provides methods to access the data.

The constructor should take the name of the file (e.g., 'spam.csv') as an argument
and store the dataframe as an instance variable. It should rename the dataframe's columns 
to 'label' and 'message'. The constructor should raise a `ValueError` if the file does not 
exist.

It should have a method called `get_first_five_rows` that returns the first five rows 
of the dataset as a dataframe as a Pandas dataframe.

It should also have methods called `get_spam` and `get_ham` that return dataframes 
containing only the rows marked as spam and ham, respectively. (Ham is messages that
are not spam.)

SpamReader should also have a method called `get_messages_containing` that returns a 
dataframe containing only the rows where the message contains a given substring. It should
have a required parameter for the substring to search for in the messages, an optional
parameter `include_ham` to specify whether to include ham messages, and an optional
parameter `include_spam` to specify whether to include spam messages that contain the 
substring. Both optional parameters should have a default value of `True`, meaning that the
method returns all spam and ham messages that include the substring.

Example usage:
    reader = SpamReader('spam.csv')
    print(reader.get_first_five_rows()) # outputs the first five rows of the dataset
    print(reader.get_spam()) # outputs all rows marked as spam
    print(reader.get_ham()) # outputs all rows marked as ham
    print(reader.get_messages_containing("free")) # outputs all messages containing "free"
    print(reader.get_messages_containing("free", include_ham=False)) # spam containing "free"
    print(reader.get_messages_containing("free", include_spam=False)) # ham containing "free"

Make sure to write appropriate documentation and tests. You may assume that `spam.csv` is in the 
same location in the autograder for your tests. (In practice, it is recommended not to use "real"
data in tests, but we have not covered the necessary material to do so. You can receive full
credit for tests that use the "real" data, but if you are interested in learning the best practice,
you may research and use "mock data" instead.)
"""

import sys
sys.path.append(".")
import os
import pandas as pd
