class CatAgain:
    def __init__(self, language="english"):
        self.result = []
        print("CatAgain Alpha")

    def evaluate(self, text=""):
        if text.__len__() is 0:
            self.result.append("Kein Text gefunden")
            return self.result

        #   detect sentence
        sentences = text.split(". ")
        for sentence in sentences:
            self.evaluate_sentence(sentence)

    def evaluate_sentence(self, text):
        text = str(text)
        sen = text.split(" ")
        for word in sen:
            # TODO CHECK spells first
            # TODO CHECK Semantic
            print(word)
        print("sentence check done")


def main():
    text = "A B C D"
    cat = CatAgain()
    cat.evaluate(text)


if __name__ == '__main__':
    main()

