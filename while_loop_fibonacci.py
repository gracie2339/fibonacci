def fibonacci(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    fib_list = [0,1]

    idx = 0
    while idx < n - 2:
      fib_list.append(fib_list[idx] + fib_list[idx+1])
      idx += 1

    return fib_list[n-1] + fib_list[n-2]


# test cases
print(fibonacci(3) == 2)
print(fibonacci(7) == 13)
print(fibonacci(0) == 0)