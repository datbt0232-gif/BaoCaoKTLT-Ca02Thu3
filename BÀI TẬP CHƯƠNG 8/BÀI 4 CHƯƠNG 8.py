fname = input("Enter file name: ")
fhand = open(fname)

words_list = []

for line in fhand:
    words = line.split()
    for word in words:
        if word not in words_list:
            words_list.append(word)

words_list.sort()
print(words_list)
