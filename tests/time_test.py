import classyjson
import json
from time import perf_counter


# Test options
iterations = 500
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
    classyjson.loads(raw)
    cj_times.append(perf_counter() - start)
    print(f'iteration: {i+1} time: {cj_times[i]}')
cj_total = perf_counter() - cj_total_start

jj_avg = sum(jj_times) / len(jj_times)
cj_avg = sum(cj_times) / len(cj_times)

print(f'json average time: {jj_avg} seconds || total time: {jj_total}')
print(f'classy-json average time: {cj_avg} seconds || total time: {cj_total}')
