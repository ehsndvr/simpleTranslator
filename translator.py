"""Authores
    Names
        Ehsan Davari
        Mohammad Fallahzade
    GithubUsernames
        iamehsandvr
        mofallahzade
    Version
        1.2.0
"""
from translators import google

""" Languages """


class Languages:
    def __init__(self) -> None:
        self.strLanguages = {
            "fa": {
                "welcome": "متن خودرا وارد کنید :",
                "f-enter": "زبان متن وارد شده را وارد کنید ({0}):",
                "l-enter": "زبانی که میخواید متن به آن ترجمه شود را وارد کنید ({0}):",
                "error": "زبان وارد شده در لیست زبان های وارد شده وجود نداره یا شما قبلا این زبان رو انتخاب کردید"
            },
            "en": {
                "welcome": "Enter the text: ",
                "f-enter": "Enter the text language({0}): ",
                "l-enter": "Translate to({0}): ",
                "error": "The language you want is not in the list of supported languages or this language has already been selected."
            },
        }


""" Index Code """


class translators:
    def __init__(self, strLT="en") -> None:
        self.strlstLanguages = ["en", "fa"]
        self.strLanguagesString = "/".join(self.strlstLanguages)
        self.text = input((Languages().strLanguages.get(strLT)).get("welcome"))
        try:
            self.language = input(
                ((Languages().strLanguages.get(strLT)).get("f-enter").format(self.strLanguagesString)))
            self.strlstLanguages.remove(self.language)
            self.strLanguagesString = "/".join(self.strlstLanguages)
            self.translationLanguage = input(
                (Languages().strLanguages.get(strLT)).get("l-enter").format(self.strLanguagesString))
            self.strlstLanguages.remove(self.translationLanguage)
        except:
            print((Languages().strLanguages.get(strLT)).get("error"))
            translators().translate()

    def translate(self):
        self.translatedText = google(
            self.text, self.language, self.translationLanguage)
        print(self.translatedText)


translators(strLT="en").translate()
