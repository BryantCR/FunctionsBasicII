#1 Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
# Example: countdown(5) should return [5,4,3,2,1,0]

def countDown(num): 
    result = []

    for i in range(num, -1, -1):
        result.append(i)
    print(result)

countDown(5)

#2 Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
# Example: print_and_return([1,2]) should print 1 and return 2

def printAndReturn(myList):
#    for i in range(0, len(myList), 1):
    print(myList[0])
#        break
    return myList[1]

print(printAndReturn([1, 2]))
print(printAndReturn([5, 8]))

#3 First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
# Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)

def first_plus_length(arr):
    for i in range(0, len(arr), 1):
        sum = 0
        sum = arr[0] + len(arr)
    return sum

print(first_plus_length([1, 2, 3, 4, 5]))

#4 Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
# Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
# Example: values_greater_than_second([3]) should return False

def values_greater_than_second(arr):
    greaterValues = []

    if len(arr) < 2:
        return False
    else:
        for i in range (0 ,len(arr), 1):
            if arr[i] > arr[1]:
                greaterValues.append(arr[i])

    print(len(greaterValues))
    return greaterValues


print(values_greater_than_second([5, 2, 3, 2, 1, 4]))

#5 This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
# Example: length_and_value(4,7) should return [7,7,7,7]
# Example: length_and_value(6,2) should return [2,2,2,2,2,2]

def length_and_value(a,b):
    newlist = []

    for i in range (0 ,a, 1):
        newlist.append(b)
    print(newlist)

length_and_value(4,7)
length_and_value(6,2)

#         newlist.append(arr[1])
#     return newlist
# def length_and_value(arr):
#     newlist = []
#     for i in range (0 , arr[0], 1):
#         newlist.append(arr[1])
#     return newlist


# print(length_and_value([7,2]))
# print(length_and_value([4,3]))