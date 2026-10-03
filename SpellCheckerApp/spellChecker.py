#Importing the required library / import spell checker library / third party library(provides readymade functions)
#Creating the app class / Advantage of building a class / we can place multiple functions in a organized structure
#Step-1 importing the required library'
from spellchecker import SpellChecker

#Step-2 creating the app class
class SpellCheckerApp:
    def __init__(self):
        self.spell = SpellChecker()

    def correct_text(self,text):
        words = text.split() #hello world['hello','world']
        corrected_words = []
        for word in words:
            corrected_word = self.spell.correction(word)
            if corrected_word != word.lower():
                print(f'Correcting "{word}" to "{corrected_word}"')
                corrected_words.append(corrected_word)

        #Step-3  returning the corrected text
        return ' '.join(corrected_words)
    #Step-4 Running the app
    def run(self):
        print("\n---Spell Checker----")

        while True:
            text = input('Enter text to check (or type "exit" to quit): ')
            if text.lower() == 'exit':
                print('Closing the program.....')
            corrected_text = self.correct_text(text)
            print(f'Corrected Text : {corrected_text}')
#Step-5 running the main program
if __name__ == "__main__":
    SpellCheckerApp().run()