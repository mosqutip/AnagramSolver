# user input letters
    # wildcards?
    # remove one letter, return matches?
        # permutations?

# permutations / reduced letters
    # TODO

from anagram_trie import AnagramTrie
import json
from urllib import request, error

class AnagramSolver:
    def __init__(self):
        self.get_input_words()
        self.parse_intput_dictionary()

    def get_input_words(self) -> None:
        try:
            input_words = request.urlopen('https://raw.githubusercontent.com/dwyl/english-words/master/words.txt').read().decode('utf-8')
            self.corpus = [str.lower(word.strip()) for word in input_words.split('\n')]
        except error.URLError as e:
            print(f'Could not access URL! Exception: {e}')

    def parse_intput_dictionary(self) -> None:
        if not self.corpus:
            returnx

        self.dictionary = AnagramTrie()
        for word in self.corpus:
            self.dictionary.insert_word(word)

    def get_user_input(self) -> str:
        print('Enter the anagram letters, or "quit" to quit: ')
        input_anagram = input()
        input_anagram = str.lower(input_anagram)

        return input_anagram

    def print_anagrams(self, input_anagram: str) -> [str]:
        print(f'For input: {input_anagram}, found the following anagrams: {", ".join(self.dictionary.get_anagrams(input_anagram))}')

def main():
    anagram_solver = AnagramSolver()
    user_input = ''
    while True:
        user_input = anagram_solver.get_user_input()
        if user_input == 'quit':
            break

        anagram_solver.print_anagrams(user_input)

if __name__ == '__main__':
    main()
