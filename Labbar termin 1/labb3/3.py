words = []


for i in range(5):
    w = input("Enter a word: ")
    words.append(w)


words.sort()


print("Sorted words:")
for w in words:
    print(w)