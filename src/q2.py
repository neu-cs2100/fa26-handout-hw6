"""HW6 Question 2: building sets and dictionaries

When we process text in machine learning, we often use character ngrams instead of entire words, 
to avoid dealing with punctuation and typos. For example, the text "chocolate", with a value of 
n=4, has these character ngrams: "choc", "hoco", "ocol", "cola", "olat", and "late". Each of 
these character ngrams appears once in "chocolate", and each of them appears twice in 
"chocolatechocolate" (and "chocolatechocolate" also has the additional character ngrams "atec", 
"tech", and "echo", each of which appears once).

Please write a class `CharNGramCounter` that counts character ngrams in a given text.

The constructor should take a string containing the text to be analyzed and an integer `n` 
specifying the length of the character ngrams.
It should initialize an internal dictionary to keep track of character ngram counts.
It should take an optional parameter for `ignore_case` that specifies whether 
to treat words as case-insensitive. If `ignore_case` is `True`, all words should 
be converted to lowercase before counting. The default for `ignore_case` should be `True`.

The class should have a method `get_ngrams` that returns a set of all character ngrams that 
appear in the text. This method should respect the `ignore_case` setting and return a copy 
of the set of ngrams, rather than a direct reference to the internal set of ngrams.

The class should also have a method `get_ngram_counts` that returns a dictionary of character 
ngram counts. The keys in the dictionary should be the character ngrams, and the values should 
be the counts of how many times each character ngram appears in the text. This method should 
also respect the `ignore_case` setting and return a copy of the internal dictionary, rather 
than a direct reference to it.

Example usage:
    counter = CharNGramCounter("chocococo", 4)
    print(counter.get_ngrams())  # {'choc', 'hoco', 'ococ', 'coco'}
    print(counter.get_ngram_counts())  # {'choc': 1, 'hoco': 1, 'ococ': 2, 'coco': 2}

Make sure to write appropriate documentation and tests.
"""
