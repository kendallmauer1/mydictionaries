word_frequency = {}

file_name = "sometext-1.txt"
with open(file_name, 'r') as file:
    for line in file:

        w = line.split()

        for word in w:

            word_frequency[word] = word_frequency.get(word, 0) + 1

for word, freq in word_frequency.items():
    print(f"{word}: {freq}")