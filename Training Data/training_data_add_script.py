import requests


# This function will store your text in one of the training
# buckets in your machine learning project
def storeTraining(text, label):
    key = "ab7fcf20-7c87-11e9-aa3b-5fc8612224ada51bd196-2f7d-48cc-a252-2755c151df72"
    url = "https://machinelearningforkids.co.uk/api/scratch/" + key + "/train"

    response = requests.post(url, json={"data": text, "label": label})

    if not response.ok:
        # if something went wrong, display the error
        print(response.json())


# CHANGE THIS to the text that you want to store
#training = "The text that you want to store"

# CHANGE THIS to the training bucket to store it in
label = "action"

#storeTraining(training, label)
print("input genre file name\n")
genre_file = input()
file = open("training_data_" + genre_file + ".txt", "r")
text = file.read()
text = text.replace("{", "")
text = text.split("}")
file.close()
for i in range(20):
    training = text[i]
    storeTraining(training, label)