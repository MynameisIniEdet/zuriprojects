# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}


def read_file_content():
    # [assignment] Add your code here
    with open("Reading-Text-Files\story.txt", "r") as file:
        data = file.read()
    # return "Hello World"
    return data


def count_words():
    text = read_file_content()
    # assignment] Add your code here
    counts = dict()
    x = text.split()
    
    for word in x:
        if word in counts:
            counts[word] +=1
        else:
            counts[word] =1
    return counts