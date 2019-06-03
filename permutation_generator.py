import copy
import math

def generate_permutations(chars: [str], wildcards: int) -> [str]:
    word_length = len(chars)
    total_length = (word_length + wildcards)
    combinations = int((math.factorial(total_length) / (math.factorial(wildcards) * math.factorial(word_length))))
    all_words = [['' for _ in range(len(chars) + wildcards)] for _ in range(combinations)]

    start_row = 0
    iteration_size = total_length
    end_row = (start_row + iteration_size)
    start_col = 0
    iterations = (((wildcards - 1) * word_length) + 1)
    for i in reversed(range(iterations)):
        generate_permutations_helper(all_words, wildcards, start_row, end_row, start_col)
        start_row = (end_row - 1)
        iteration_size -= 1
        end_row = (start_row + iteration_size)
        start_col += 1

    return fill_word(all_words, chars)

def generate_permutations_helper(all_words: [[str]], wildcards: int, start_row: int, end_row: int, start_col: int) -> None:
    if wildcards == 1:
        j = start_col
        for i in range(start_row, end_row):
            all_words[i][j] = '*'
            j += 1
    else:
        end_row -= 1
        for i in range(start_row, end_row):
            all_words[i][start_col] = '*'
            generate_permutations_helper(all_words, (wildcards - 1), start_row, end_row, (start_col + 1))

def fill_word(all_words: [[str]], word: [str]) -> [str]:
    strings = []
    for i in range(len(all_words)):
        index = 0
        for j in range(len(all_words[0])):
            if all_words[i][j] == '*':
                continue
            else:
                if index == len(word):
                    break
                all_words[i][j] = word[index]
                index += 1

        strings.append(''.join(all_words[i]))

    return strings

word = 'wor*d'
chars = []
wildcards = 0
for char in word:
    if char == '*':
        wildcards += 1
    else:
        chars.append(char)

chars.sort()
all_words = generate_permutations(chars, wildcards)
print(all_words)
print(len(all_words))
