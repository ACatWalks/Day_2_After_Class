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
    if n < 1:
        print('Minimum number of rows is 1')
    elif n == 1:
        return 1
    else:
        triangle = [[1], [1,1]]
        for i in range (2, n+1):
            row = []
            for j in range(0, i):
                if j == 0:
                    row.append(1)
                elif j == i-1:
                    row.append(1)
                else:
                    row.append(triangle[i-1][j] + triangle[i-1][j-1])
            triangle.append(row)
        for row in triangle:
            print(row)



print(max_num([3, 33, 333]))
print(mult_list([2,4,6]))
print(rev_string('Hello World'))
print(num_within(3, 13, 26))
print(pascal(5))