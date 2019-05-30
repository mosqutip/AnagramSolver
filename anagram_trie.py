class AnagramTrieNode:
    def __init__(self, letter):
        self.letter = letter
        self.children = {}
        self.words = set()

class AnagramTrie:
    def __init__(self) -> None:
        self.root = AnagramTrieNode('')

    def insert_word(self, word: str) -> None:
        node = self.root
        alphabetized_word = ''.join(sorted(word)).strip()

        for letter in alphabetized_word:
            if letter not in node.children:
                node.children[letter] = AnagramTrieNode(letter)

            node = node.children[letter]

        node.words.add(word)

    def is_word_in_trie(self, word: str) -> bool:
        node = self.root
        alphabetized_word = ''.join(sorted(word)).strip()

        for letter in alphabetized_word:
            if letter in node.children:
                node = node.children[letter]
            else:
                return False

        return word in node.words

    def get_anagrams(self, word: str) -> [str]:
        node = self.root
        alphabetized_word = ''.join(sorted(word)).strip()

        for letter in alphabetized_word:
            if letter in node.children:
                node = node.children[letter]
            else:
                return []

        return list(node.words)

    def count_words(self, node: AnagramTrieNode = None) -> int:
        if not node:
            node = self.root

        count = len(node.words)
        for child in node.children.values():
            count += self.count_words(child)

        return count

    def print_words(self) -> None:
        node = self.root
        self._print_node_words(node)

    def _print_node_words(self, node: AnagramTrieNode) -> None:
        for word in node.words:
            print(word)
        for child in node.children.values():
            self._print_node_words(child)

# def main():
#     dictionary = AnagramTrie()

#     dictionary.insert_word('there')
#     dictionary.insert_word('the')
#     dictionary.insert_word('these')
#     dictionary.insert_word('three')

#     print(dictionary.is_word_in_trie('there'))
#     print(dictionary.is_word_in_trie('the'))
#     print(dictionary.is_word_in_trie('these'))
#     print(dictionary.is_word_in_trie('three'))

#     dictionary.print_words()
#     print(dictionary.count_words())

# if __name__ == '__main__':
#     main()
