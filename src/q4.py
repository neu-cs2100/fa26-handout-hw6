"""HW6 Question 4: building a small language model

Write a function `generate_next_char` that takes a prompt string and a dictionary of ngram 
counts, and returns the next character based on the probabilities derived from the counts.

As with the previous question, the function should not take the value of n as a separate 
parameter. Instead, you can assume that the prompt string has length n-1, and the dictionary is 
formatted correctly, with ngrams of length n.

First, `generate_next_char` should call `next_letter_frequency()` with the prompt and counts to 
get the possible next characters and their counts.

If the dictionary returned by `next_letter_frequency` is empty (because the character ngram 
prompt was not there in the original text), then `generate_next_char` should randomly choose a
letter between a and z and return it.

If the dictionary returned by `next_letter_frequency` is not empty, then `generate_next_char` 
should randomly choose one of the characters listed as an option in the dictionary and return it.

If you are looking for an added challenge, use the counts returned by `next_letter_frequency()` 
to indicate how likely each next letter should be. For example, if `next_letter_frequency()` 
returns {'c': 2, 'd': 1} then `generate_next_char()`should be twice as likely to generate 'c' as 
'd'. You can do this by generating a random number between 0 and 3. If the number is 0 or 1, then 
return 'c', and if the number is 2, then return 'd'. This is an added, ungraded challenge.

A main function is provided below for you to test it out. (To fully appreciate the small language
model you've built, it will be useful to replace the training text with a much longer string, 
read from a file.)

Make sure to write appropriate documentation and tests. You do not need to test `main`.
"""

import random
import sys
sys.path.append(".")
from src.q2 import CharNGramCounter
from src.q3 import next_letter_frequency


def main() -> None:
    """Generate text using a small language model and a prompt."""
    n = 3
    training_text = 'catcatcat' # you should replace this with longer text from a file
    n_gram_counts = CharNGramCounter(training_text, n).get_ngram_counts()
    output_text = 'cat'

    for _ in range(1, 20):
        next_letter = generate_next_char(output_text[-(n-1):], n_gram_counts)
        output_text += next_letter
    print(output_text)

if __name__ == "__main__":
    main()
