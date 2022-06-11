# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True





def find_anagram(word, anagram):
  
    if sorted(word)==sorted(anagram) or len(word)==len(anagram):
        return True
    else:
        return False
    # [assignment] Add your code here
print(find_anagram('pot','tops'))
print(find_anagram('secure','rescue'))