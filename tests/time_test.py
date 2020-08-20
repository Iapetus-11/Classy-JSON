import json
from time import perf_counter
import sys

sys.path.append('..')

import .classyjson


# Test options
iterations = 50
file = 'test_large.json'

with open(file, 'r') as f:
    raw = f.read()

# Using regular json
print(f'classy-json test using regular json ({iterations} iterations)')
jj_times = []
jj_total_start = perf_counter()
for i in range(iterations):
    start = perf_counter()
    json.loads(raw)
    jj_times.append(perf_counter() - start)
    print(f'iteration: {i+1} time: {jj_times[i]}')
jj_total = perf_counter() - jj_total_start

# Using classyjson
print(f'classy-json test using classy-json ({iterations} iterations)')
cj_times = []
cj_total_start = perf_counter()
for i in range(iterations):
    start = perf_counter()
    classyjson.loads(raw, threaded=True)
    cj_times.append(perf_counter() - start)
    print(f'iteration: {i+1} time: {cj_times[i]}')
cj_total = perf_counter() - cj_total_start

jj_avg = sum(jj_times) / len(jj_times)
cj_avg = sum(cj_times) / len(cj_times)

print()
print('        json average time: {:2.4f} seconds || total time: {} || total iterations: {}'.format(round(jj_avg, 4), round(jj_total, 4), iterations))
print(' classy-json average time: {:2.4f} seconds || total time: {} || total iterations: {}'.format(round(cj_avg, 4), round(cj_total, 4), iterations))
