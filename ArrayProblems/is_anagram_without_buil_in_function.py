def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    str1 = str1.lower()
    str2 = str2.lower()

    array = [0] * 256
    for char in str1:
        array[ord(char)] += 1
    for char in str2:
        array[ord(char)] -= 1

    for arr in array:
        if arr == 0:
            return False
    return True