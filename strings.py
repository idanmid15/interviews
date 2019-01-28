
import string
import random
import time


def generate_characters():
    """
    For any given input, renders random combinations of characters until the input is rendered,
    giving a "Matrix" like effect to the rendering
    """
    allowed_letters = string.printable
    input_sentence = input("Enter a sentence!\n")
    generated_sentence = [random.choice(allowed_letters)
                          for _ in range(len(input_sentence))]
    while ''.join(generated_sentence) != input_sentence:
        for idx, letter in enumerate(generated_sentence):
            if letter != input_sentence[idx]:
                generated_sentence[idx] = random.choice(allowed_letters)
        time.sleep(0.025)
        print(''.join(generated_sentence))


if __name__ == '__main__':
    generate_characters()
