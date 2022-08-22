#Author : Mohammad Fallahzade
from translators import google
class translators:
    def __init__(self):
        self.text = input("Enter the text: ")
        self.language = input("Enter the text language(en/fa): ")
        self.translationLanguage = input("Translate to(en/fa): ")
    def translate(self):
        self.translatedText = google(self.text, self.language,self.translationLanguage)
        print(self.translatedText)
trans = translators()
trans.translate()