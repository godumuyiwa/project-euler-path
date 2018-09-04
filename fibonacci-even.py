fib = [1,2]
while fib[-1] < 4000000:
    fib.append(fib[-1] + fib[-2])
sum_even_fib = 0
for t in fib:
    if t%2 == 0:
        sum_even_fib += t
    else:
        continue
print(sum_even_fib)