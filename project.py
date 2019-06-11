import requests

# This function will pass your text to the machine learning model
# and return the top result with the highest confidence
def classify(text):
    key = "547555f0-885e-11e9-a888-89aa3aa5808d2d690b6c-eeef-4353-b91d-6cb2a3d72896"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={ "data" : text })

    if response.ok:
        response_data = response.json()
        top_match = response_data[0]
        return top_match
    else:
        response.raise_for_status()


user_input = ""
while user_input != "quit":
    user_input = input("type your review: \n")
    demo = classify(user_input)

    label = demo["class_name"]
    confidence = demo["confidence"]

    print ("result: '%s' with %d%% confidence\n" % (label, confidence))
