
def max_contiguous_subarray(array):
    """
    Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1

    *******
    [], [0], [1] = 0
    [0,1,0] = 2
    [0.0.0,1,1,0] = 4
    [0,0,0,1,1,1] = 6
    [0,1,1,0,0,1,1,0,0] = 8
    [0,0,0,0,0,0,1,1,1,1] = 8
    [0,0,0,1,1,1,1,1] = 6
    [0,1,0,1,1,1,0,0,0] = 8
    [0,0,1,1,1,1,1,1,1,0,0] = 4
    [1,0,1,1,1,0,1,0,1,0,1,1,1,1,1] = 6
    {0:2,
    1:2,
    2:4,
    3:5,
    }
    [1,0,1,1,0,0,1,1] = 6
    """
    if len(array) == 0 or len(array) == 1:
        return 0
    # if counter is positive, more 1s are present, negative means more 0s are
    equal_counter = 0
    count_found = {0: 0}
    largest_size = 0
    for idx, binary in enumerate(array):
        equal_counter = equal_counter + 1 if binary == 1 else equal_counter - 1
        if equal_counter not in count_found:
            count_found[equal_counter] = idx
        else:
            largest_size = max(largest_size, idx - count_found[equal_counter])
    return largest_size


def switch_first_and_last_words(letters):
    """
    Given an array filled with 3 words by characters,
    have to switch between the first and last words *in place*
    Example:
    ['p','e','r','f','e','c','t',' ', 'm','a','k','e','s',' ', 'p','r','a','c','t','i','c', 'e']
    =>
    ['p','e','r','f','e','c','t',' ', 'm','a','k','e','s',' ', 'p','r','a','c','t','i','c','e']
    """

    # Reverse the letters
    letters = letters[::-1]
    end_word = 0

    # the number of words
    for _ in range(3):
        begin_word, end_word = find_next_word_indices(letters, end_word)
        letters = reverse_str(begin_word, end_word, letters)
    return letters


def find_next_word_indices(words, end_word=0):
    if end_word == 0:
        while words[end_word] != ' ':
            end_word += 1
        return 0, end_word
    while words[end_word] == ' ':
        end_word += 1
    begin_word_index = end_word
    while end_word < len(words) and words[end_word] != ' ':
        end_word += 1
    return begin_word_index, end_word


def reverse_str(begin, end, words):
    for i in range(begin, int((end - begin) / 2) + begin):
        temp = words[i]
        words[i] = words[end - 1 - i + begin]
        words[end - 1 - i + begin] = temp
    return words


if __name__ == '__main__':
    print(max_contiguous_subarray([]))
    print(max_contiguous_subarray([1]))
    print(max_contiguous_subarray([0]))
    print(max_contiguous_subarray([0, 1, 0]))
    print(max_contiguous_subarray([0, 0, 0, 1, 1, 0]))
    print(max_contiguous_subarray([0, 1, 1, 0, 0, 1, 1, 0, 0]))
    print(max_contiguous_subarray([0, 0, 0, 0, 0, 0, 1, 1, 1, 1]))
    print(max_contiguous_subarray([1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1]))
    print(switch_first_and_last_words(['p','e','r','f','e','c','t',' ', 'm','a','k','e','s',' ', 'p','r','a','c','t','i','c', 'e']))
