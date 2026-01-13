nums = [1,2,3,4]

sqr_nums = [x*x for x in nums]
print(sqr_nums)

nums = [1,2,3,4,5,6]

sqr_even = [x*x for x in nums if x%2 == 0]
print(sqr_even)

# arr = [[1,2], [5,6], [5]]
#
# flat_arr = []
words = ["ajay", "python", "django"]

upper_words = [word.upper() for word in words]
print(upper_words)

nums = [3, 12, 5, 18, 7, 20]
new_nums = [x for x in nums if x > 10]
print(new_nums)

nums = [1,2,3,4,5,6]

new_nums = [x if x%2 == 0 else 0 for x in nums]
print(new_nums)

words = ["django", "rest", "api"]

len_arr = [len(word) for word in words]
print(len_arr)

text = "interview"

vower_arr = [vowel for vowel in text if vowel.lower() in 'aeiou']

print(vower_arr)

matrix = [[1,2,3], [4,5,6], [7,8]]

flat = [num for row in matrix for num in row]
print(flat)

new_arr = [i for i in range(1,101) if i%3 == 0 and i%5==0]
print(new_arr)

nums = [1,2,3,4]
list_of_tuple = [(num, num*num) for num in nums]
print(list_of_tuple)


vower_arr = [vowel for vowel in text if vowel.lower() not in 'aeiou']
print(vower_arr)

a = [1,2,3]
b = [4,5,6]

even_sum = [(x,y) for x in a for y in b if (x+y)%2==0]
print(even_sum)

marks = {"ajay": 85, "rahul": 40, "neha": 75}
new_marks = [name for name, score in marks.items() if score > 50]
print(new_marks)