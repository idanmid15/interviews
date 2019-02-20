
def max_contiguous_sub_array(array):
    """
    Given a binary array, find the maximum length of a contiguous sub array with equal number of 0 and 1

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


def add_up_to_k(arr1, arr2, k):
    """
    Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

    For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
    """
    k_complements = [k - i for i in arr1]
    for i in arr2:
        if i in k_complements:
            return True
    return False


def product_except_i(arr):
    """
    Given an array of integers, return a new array such that each element at index i of the new array is the product of all
     the numbers in the original array except the one at i.

    For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was
     [3, 2, 1], the expected output would be [2, 3, 6].

    Follow-up: what if you can't use division?
    """
    product_arr = [1]

    # Multiply and carry the sum along to the right
    for idx, _ in enumerate(arr):
        if idx > 0:
            product_arr += [product_arr[idx - 1] * arr[idx - 1]]

    right_accum = 1

    # Multiply and carry the sum from the right to left in addition to the left to the right sum already calculated
    for idx, _ in enumerate(arr):
        if idx > 0:
            right_accum *= arr[len(product_arr) - idx]
            product_arr[len(product_arr) - 1 - idx] *= right_accum
    return product_arr


def missing_positive_integer(arr):
    """
    Given an array of integers, find the first missing positive integer in linear time and constant space.
    In other words, find the lowest positive integer that does not exist in the array.
    The array can contain duplicates and negative numbers as well.

    For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

    You can modify the input array in-place.
    """
    max1 = max(arr)
    right_idx = len(arr) - 1
    left_idx = 0

    #  Move positives to the right of array
    while left_idx < right_idx:
        while arr[left_idx] < 0 and left_idx < len(arr):
            left_idx += 1
        while arr[right_idx] > 0 and right_idx > 0:
            right_idx -= 1
        if left_idx < right_idx:
            arr[left_idx], arr[right_idx] = arr[right_idx], arr[left_idx]

    #  Take current list values which are positive and turn the cells who's location corresponds to the value and turn
    #  them negative
    for i in range(len(arr)):
        if len(arr) > arr[i] > -1:
            tmp = arr[i]
            while arr[tmp] > -1:
                if arr[tmp] < len(arr):
                    tmp1 = arr[tmp]
                    arr[tmp] = -1
                    tmp = tmp1
                arr[tmp] = -1

    #  Find first non negative occurrence
    for idx, val in enumerate(arr):
        if val > 0 and idx > 0:
            return idx
    return max1 + 1


if __name__ == '__main__':
    print(max_contiguous_sub_array([]))
    print(max_contiguous_sub_array([1]))
    print(max_contiguous_sub_array([0]))
    print(max_contiguous_sub_array([0, 1, 0]))
    print(max_contiguous_sub_array([0, 0, 0, 1, 1, 0]))
    print(max_contiguous_sub_array([0, 1, 1, 0, 0, 1, 1, 0, 0]))
    print(max_contiguous_sub_array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1]))
    print(max_contiguous_sub_array([1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1]))
    print(switch_first_and_last_words(['p', 'e', 'r', 'f', 'e', 'c', 't', ' ', 'm', 'a', 'k', 'e', 's', ' ', 'p', 'r',
                                       'a', 'c', 't', 'i', 'c', 'e']))
    print(add_up_to_k([1, 2, 3], [4, 5, 6], 9))  # True
    print(add_up_to_k([1, 2, 3], [4, 5, 6], 10))  # False
    print(add_up_to_k([], [4, 5, 6], 10))  # False
    print(add_up_to_k([-1], [4, 5, 6], 4))  # True
    print(product_except_i([1, 2, 3]))
    print(missing_positive_integer([1, -3, 0, -1, 2, 1, 5, 4]))  # 3
    print(missing_positive_integer([3, 4, -1, 1]))  # 2
    print(missing_positive_integer([1, 2, 0]))  # 3
    print(missing_positive_integer([5, 7, 6]))  # 1
    print(missing_positive_integer([5, 7, 6, 3, 2, 1]))  # 4
