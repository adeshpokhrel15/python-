#Pangram_string
import string
to_check = "The quick brown"
alphabets = set(list(string.ascii_lowercase))
print(sorted(alphabets))
letters_in_word=list()
for char in to_check:
    if char.isalpha():
        letters_in_word.append(char)
print(set(letters_in_word))
print(len(letters_in_word))
print(len(alphabets))
