def max_num(nums):
    max = nums[0]
    for i in nums:
        if i > max:
            max = i
    return max

def mult_list(nums):
    product = 1
    for i in nums:
        product = product * i
    return product

def rev_string(str):
    opp_string = ''
    str_as_list = [char for char in str] 
    reversed_list = []
    for i in str_as_list:
        reversed_list.insert(0,i)
    return opp_string.join(reversed_list)

def num_within(input, min, max):
    return input >= min and input <= max

def pascal(n):
    triangle = [[1], [1,1]]
    if n < 1:
        print('Invalid number of rows')
    elif n == 1:
        print(1)
    else:
        #No idea what to do from here: checked solution code 
        row_number = 2
        while len(triangle) < n:
            row = []
            row_prev = triangle[row_number - 1]
            length = len(row_prev) + 1
            for i in range(length):
                if i == 0:
                    row.append(1)
                elif i > 0 and i < length - 1:
                    row.append(triangle[row_number - 1][i-1] + triangle[row_number - 1][i])
                else:
                    row.append(1)
            triangle.append(row)
            row_number += 1
        for row in triangle:
            print(row)

print(max_num([3, 33, 333]))
print(mult_list([2,4,6]))
print(rev_string('Hello World'))
print(num_within(3, 13, 26))
print(pascal(5))