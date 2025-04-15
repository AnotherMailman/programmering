count = {}

sentence = input()

for letter in sentence:
    if letter in count:
        count[letter] += 1
    else:
        count[letter] = 1

print(count)