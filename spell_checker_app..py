from spellchecker import SpellChecker

class SpellCheckerApp:
    def __init__(self):
        self.spell=SpellChecker()

    def correct_text(self,text):
        words=text.split()
        corrected_words=[]

        for word in words:
            correct_wrd=self.spell.correction(word)
            if correct_wrd.lower()!=word.lower():
                print(f'corrected {word} to {correct_wrd}')
            corrected_words.append(correct_wrd)
            
        return ' '.join(corrected_words)
    
    def run(self):
        print('---spell checker ---')

        while True:
            text=input("enter text or exit:")

            corr_text=self.correct_text(text)
            print(f'corrected text: {corr_text}')

            if text.lower()=='exit':
                print('closing program...')
                break

if __name__=="__main__":
    SpellCheckerApp().run()