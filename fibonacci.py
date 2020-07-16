fibonacci_list = []
fibonacci_list.append(1)
fibonacci_list.append(1)
n = 0
total = 0
while total < 55:
    total = fibonacci_list[n] + fibonacci_list[n + 1]
    fibonacci_list.insert(n + 2, total)
    n +=1
print("Fibonacci numbers from 1 to 55 are : ", fibonacci_list)