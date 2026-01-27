def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False

    array = [0] * 256
    for char in str1:
        print(char)
        print(array)
        array[ord(char)] += 1
    for char in str2:
        print(array)
        array[ord(char)] -= 1

    for arr in array:
        if arr != 0:
            return False
    return True

print(is_anagram('silent', 'listen'))