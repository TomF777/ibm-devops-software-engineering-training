
from deep_translator import MyMemoryTranslator

def englishToFrench(englishText: str):
    # function translates english text into french
    frenchText = MyMemoryTranslator(source='en-US', target='fr-FR').translate(englishText)
    #print(frenchText)
    return frenchText
    
def frenchToEnglish(frenchText):
    # function translates french text into english
    englishText = MyMemoryTranslator(source='fr-FR', target='en-US').translate(frenchText)
    #print(englishText)
    return englishText

