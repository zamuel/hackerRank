# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def transformSentence(sentence):
    palabra = sentence[0]
    for i in range(1,len(sentence)):
        if sentence[i-1]==" " or  sentence[i]==" ":
            palabra += sentence[i]
        elif sentence[i-1].lower()<sentence[i].lower():
            palabra += sentence[i].upper()
        elif sentence[i-1].lower()>sentence[i].lower():
            palabra+=sentence[i].lower()
        else:
            palabra+=sentence[i]
    return palabra











if __name__ == '__main__':


    print(transformSentence("CoOl Dog"))

