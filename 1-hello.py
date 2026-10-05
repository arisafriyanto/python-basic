# IF Statement

# x = int(input("Please enter an integer: "))

# if x < 0 :
#     x = 0
#     print("Negative change to zero");
# elif x == 0:
#     print("Zero")
# elif x == 1:
#     print('Single')
# else :
#     print("More")


# For Statement

# words = ['cat', 'window', 'defenestrate']
# for w in words:
#     print(w, len(w))


### Range function

# for i in range(10):
#     if i % 2 == 0:
#         print(i, "Genap")
#     else:
#         print(i, "Ganjil")

# print('\n\n');
# print(list(range(0, 10, 3)))


# a = ['Mary', 'had', 'a', 'little', 'lamb']
# for i in range(len(a)):
#     print(i, a[i])

# print('\n\n')
# print(sum(range(4))) # 0 + 1 + 2 + 3


# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, 'equals', x, '*', n//x)
#             break
#         else:
#             print(n, 'is prime number')

# for num in range(2, 10):
#     if num % 2 == 0:
#         print("Found an even number", num)
#         continue
#     print("Found an odd number", num)


# Pass Statement

# while True:
#     pass


# Defining Functions

# def fibonacci(n):
#     a, b = 0, 1
#     while a < n:
#         print(a, end=' ')
#         a, b = b, a+b
#         print()

# fib = fibonacci
# fib(200)



### Data Structures

# More on Lists

# fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana', 'apple']

# countApple = fruits.count('apple');
# countTangerine = fruits.count('tangerine')
# indexBanana = fruits.index('banana')
# index4Banana = fruits.index('banana', 4)

# fruits.reverse()
# fruits.append('grape')
# fruits.sort()
# fruits.pop()

# print(fruits);


# Using Lists as Stacks

# stack = [3,4,5]
# stack.append(6)
# stack.append(7)

# stack.pop()

# print(stack)

# stack.pop()
# stack.pop()

# print(stack)



# Using Lists as Queues

# from collections import deque
# queue = deque(['Eric', 'John', 'Michael'])
# queue.append('Terry')
# queue.append('Graham')

# queue.popleft()
# # queue.popleft()
# queue.pop()

# print(queue)


# Tuples and Sequences

# t = 12345, 54321, 'hello!'

# print(t[0])
# print(t)

# u = t, (1,2,3,4,5)

# print(u)

# t[0] = 88888

# print(t)


