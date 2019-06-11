import requests


# This function will store your text in one of the training
# buckets in your machine learning project
def storeTraining(text, label):
    key = "547555f0-885e-11e9-a888-89aa3aa5808d2d690b6c-eeef-4353-b91d-6cb2a3d72896"
    url = "https://machinelearningforkids.co.uk/api/scratch/" + key + "/train"

    response = requests.post(url, json={"data": text, "label": label})

    if not response.ok:
        # if something went wrong, display the error
        print(response.json())


#storeTraining(training, label)
language = input("enter file: ")
label = language
file = open(language + ".txt", "r", encoding="latin-1")
text = file.read()
text = text.split("\n\n")
file.close()
for i in text:
    print(i)
    training = i
    storeTraining(training, label)