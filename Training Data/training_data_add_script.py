import requests


# This function will store your text in one of the training
# buckets in your machine learning project
def storeTraining(text, label):
    key = "f2474770-7d64-11e9-96e3-39e2771d810d01764370-411f-412e-8063-71409067b106"
    url = "https://machinelearningforkids.co.uk/api/scratch/" + key + "/train"

    response = requests.post(url, json={"data": text, "label": label})

    if not response.ok:
        # if something went wrong, display the error
        print(response.json())


# CHANGE THIS to the text that you want to store
#training = "The text that you want to store"


#storeTraining(training, label)
label = "spanish"
file = open("spanish_words.txt", "r")
text = file.read()
text = text.split("\n")
file.close()
for i in range(250):
    print(i)
    training = text[i]
    storeTraining(training, label)