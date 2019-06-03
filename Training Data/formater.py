file = open("english_words.txt", "r")
text = file.read()
text = text.split("\n")
for i in range(250):
    print(text[i])
file.close()