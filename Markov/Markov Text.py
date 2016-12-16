import random


class Markov(object):
    def __init__(self, open_file):
        self.cache = {}
        self.open_file = open_file
        self.words = self.file_to_words()
        self.tuples = self.create_tuples()
        self.fill_cache()

    def file_to_words(self):
        self.open_file.seek(0)
        data = self.open_file.readlines()
        words = []
        for i in data:
            words.append(i.split())
        return words

    def create_tuples(self):
        tuples = []
        for line in self.words:
            for i in range(len(line)-1):
                tuples.append((line[i], line[i+1]))
        return tuples

    def fill_cache(self):
        for tuple in self.tuples:
            key = tuple[0]
            if key in self.cache:
                self.cache[key].append(tuple[1])
            else:
                self.cache[key] = [tuple[1]]

    def generate_markov_text(self, size=25):
        w1 = self.words[0][0]  # Select <s> as the first word of the sentence
        gen_words = []
        for i in xrange(size):
            gen_words.append(w1)
            w1 = random.choice(self.cache[w1])
        gen_words.append(w1)
        return ' '.join(gen_words)

if __name__ == '__main__':
    text_file = open('ggcc-saetze.txt', 'r')
    markov = Markov(text_file)
    while raw_input("Weiter machen?"):
        print(markov.generate_markov_text())

