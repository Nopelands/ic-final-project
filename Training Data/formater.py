file = open("training_data_action.txt", "r")
text = file.read()
text = text.replace("{", "")
text = text.split("}")
for i in range(20):
    print(text[i])
file.close()