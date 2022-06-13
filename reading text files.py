# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}
import string
def read_file_content(filename):
    text_file= open('story.txt')
    content= text_file.read()
    # [assignment] Add your code here 
    return text_file
    


def count_words():
    with open("story.txt",'r') as f:
        text= f.read()
        words = text.split()
        text_punc= str.maketrans("", "", string.punctuation)
        text_punc_stip= [w.translate(text_punc) for w in words]
        word_count= {}

        for word in words:
            word_count[word] = words.count(word)
        return word_count
    
    
    
    # [assignment] Add your code here
    

    