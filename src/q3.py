"""HW6 Question 3: working with dictionaries

Write a function `next_letter_frequency` that takes 1) a prompt string and 2) a dictionary of 
character ngram counts (in the format returned by CharNGramCounter.get_ngram_counts()), 
and returns a dictionary of the possible next letters and their frequencies.

The function should not take the value of n as a separate parameter.
Instead, you can assume that the prompt string has length n-1, and the dictionary is formatted 
correctly, with ngrams of length n.

The function should return a dictionary where the keys are the possible next letters, and the v
alues are their frequencies based on the provided ngram counts.

Example usage:
    counts = {
        " a c": 2,
        " a d": 1
    }
    print(next_letter_frequency(" a ", counts))  # {'c': 2, 'd': 1}

Make sure to write appropriate documentation and tests.
"""
