import nltk, json, pickle
import numpy as np
import random
from nltk.stem import SnowballStemmer
from tensorflow.python.keras.models import load_model

stemmer = SnowballStemmer('spanish')

model = load_model("chatbot_model.h5")
intents = json.loads(open("intent.json").read())
words = pickle.load(open("words.pkl","rb"))
classes = pickle.load(open("classes.pkl","rb"))

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
    return sentence_words

def bow(sentence, words, show_details=True):
    sentence_words = clean_up_sentence(sentence)
    bag = [0]*len(words)
    for i in sentence_words:
        for j, w in enumerate(words):
            if w == i:
                bag[j] = 1
                if show_details:
                    print("encontrado en la bolsa: ", w)
    return (np.array(bag))

def predict_class(sentence, model):
    p = bow(sentence, words, show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i, r in enumerate(res) if r>ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    print("return list : ", return_list)
    return return_list

def get_response(ints, intents_json):
    tag = ints[0]["intent"]
    list_of_intents = intents_json["intents"]
    for i in list_of_intents:
        if (i["tag"] == tag):
            result = random.choice(i["responses"])
            break
    return result

def chatbot_response(text):
    ints = predict_class(text, model)
    res = get_response(ints, intents)
    return res

########PROBAR EN CONSOLA###################
def start_bot():
    texto_us=""
    print("bienvenido, para salir escriba salir: ")
    while texto_us!="salir":
        texto_us=input()
        res = chatbot_response(texto_us)
        print(res)
###############################################
def bot(texto_us):
        #start_chatbot() #CONSOLA
        res=chatbot_response(texto_us)
        return res

def start_chatbot():
    start_intents()
    start_model()
    #start_bot() #CONSOLA

# _________________________________MAIN________________________
from intents import start_intents
from model_builder import start_model


# Driver program
if __name__ == '__main__':

    #para ejecutar en consola:
    start_chatbot()
    #start_bot()

    #para integrar con whatsapp
    #answer=bot(texto_us)
