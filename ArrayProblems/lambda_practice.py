#lambda is use to make function in a single line

def add(a,b):
    return a+b

add = lambda a,b: a+b

square = lambda x: x*x

is_even = lambda x: x%2==0

nums = [1,2,3,4,5]

squr_arr = list(map(lambda x: x*x, nums))

filtr_arr = list(filter(lambda x:x%2==0, nums))


data = [(1,3), (4,1), (2,2)]
sorted_list = list(sorted(data, key=lambda x: x[1]))


