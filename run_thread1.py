import time

start_time = time.time()

sum_of_numbers = 0
for i in range(1, 100000001):
    sum_of_numbers += i

end_time = time.time()

print(f"1부터 1억까지의 합: {sum_of_numbers}")
print(f"실행 시간: {end_time - start_time} 초")