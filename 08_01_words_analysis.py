'''
Write a script that reads in the words from the words.txt file and finds and prints:

1. The shortest word (if there is a tie, print all)
2. The longest word (if there is a tie, print all)
3. The total number of words in the file.


'''


with open('words.txt', 'r') as words:
    short = ['fsdakjfkl;asjdfkl;asjdl;fkasjdl;kfa']
    long = ['a']
    count = 0

    for word in words:
        if len(word) < len(short[0]):
            short = [word]
        elif len(word) == len(short[0]):
            short.append(word)
        elif len(word) > len(long[0]):
            long = [word]
        elif len(word) == len(long[0]):
            long.append(word)


short_stripped = []
for i in short:
    short_stripped.append(i.strip('\n'))

long_stripped = []
for i in long:
    long_stripped.append(i.strip('\n'))


print(short_stripped)
print(long_stripped)