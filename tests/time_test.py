import json
from time import perf_counter
import classyjson


# Test options
iterations = 50
file = 'test_large.json'

with open(file, 'r') as f:
    raw = f.read()

# Using regular json
jj_times = []
jj_total_start = perf_counter()
for _ in range(iterations):
    start = perf_counter()
    json.loads(raw)
    jj_times.append(perf_counter() - start)
jj_total = perf_counter() - jj_total_start

# Using classyjson
cj_times = []
cj_total_start = perf_counter()
for _ in range(iterations):
    start = perf_counter()
    classyjson.loads(raw)
    cj_times.append(perf_counter() - start)
cj_total = perf_counter() - cj_total_start

jj_avg = sum(jj_times) / len(jj_times)
cj_avg = sum(cj_times) / len(cj_times)

print('\n Loading json:')
print('        json average time: {:2.4f} seconds || total time: {} || total iterations: {}'.format(round(jj_avg, 4), round(jj_total, 3), iterations))
print(' classy-json average time: {:2.4f} seconds || total time: {} || total iterations: {}'.format(round(cj_avg, 4), round(cj_total, 3), iterations))

iterations = 1000000

# Using regular json
jj_times = []
jj = json.loads(raw)
jj_total_start = perf_counter()
for _ in range(iterations):
    start = perf_counter()
    jj['a'] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    jj['a'] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    jj_times.append(perf_counter() - start)
jj_total = perf_counter() - jj_total_start

# Using classyjson
cj_times = []
cj = classyjson.loads(raw)
cj_total_start = perf_counter()
for _ in range(iterations):
    start = perf_counter()
    cj.a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    jj['a'] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    cj_times.append(perf_counter() - start)
cj_total = perf_counter() - cj_total_start

jj_avg = sum(jj_times) / len(jj_times)
cj_avg = sum(cj_times) / len(cj_times)

print('\n\n setting an attribute / key to a value twice:')
print(' regular dicts: {:2.8f} seconds || total time: {} || total iterations: {}'.format(round(jj_avg, 8), round(jj_total, 4), iterations))
print('   classy-json: {:2.8f} seconds || total time: {} || total iterations: {}'.format(round(cj_avg, 8), round(cj_total, 4), iterations))
