# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}
from collections import Counter


def read_file_content(filename):
    # [assignment] Add your code here
    textfile = open(filename, "r")
    data = textfile.read()

    return data


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here

    words_counted = dict(Counter(text.split()))
    # print(occurences)

    return words_counted


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    count_words()
