'''
Write a script that reads in the contents of words.txt and writes the contents in reverse
to a new file words_reverse.txt.
'''


words_list = []
reverse_list = []

with open('words.txt', 'r') as words:
    for word in words:
        words_list.append(word)

reverse_list = reversed(words_list)

with open('words_reverse.txt', 'w') as reverse:
    for word in reverse_list:
        reverse.write(word)