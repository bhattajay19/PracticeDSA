

def plusOne(digits):
    n = len(digits)
    if n == 0:
        return 0

    for i in range(n-1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        else:
            digits[i] = 0
    return [1] + digits

digits = [9,9,9,9]
print(plusOne(digits))