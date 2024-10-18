def fibonacci(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    fib_list = [0,1]
    for i in range(n-2):
      fib_list.append(fib_list[i] + fib_list[i+1])
    return fib_list[n-1] + fib_list[n-2]


# test cases
print(fibonacci(3) == 2)
print(fibonacci(7) == 13)
print(fibonacci(0) == 0)