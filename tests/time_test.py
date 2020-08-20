import classyjson
import json
from time import perf_counter


# Test options
iterations = 10
file = 'test_large.json'

with open(file, 'r') as f:
    raw = f.read()

# Using classyjson
print(f'classy-json test using classy-json ({iterations} iterations)')
cj_times = []
for i in range(iterations):
    start = perf_counter()
    classyjson.loads(raw)
    cj_times.append(perf_counter() - start)
    print(f'iteration: {i} time: {cj_times[i]}')

# Using regular json
print(f'classy-json test using regular json ({iterations} iterations)')
jj_times = []
for i in range(iterations):
    start = perf_counter()
    json.loads(raw)
    jj_times.append(perf_counter() - start)
    print(f'iteration: {i} time: {jj_times[i]}')

cj_avg = sum(cj_times) / len(cj_times)
jj_avg = sum(jj_times) / len(jj_times)

print(f'classy-json (average time to decode data from a string): {cj_avg} seconds')
print(f'json (average time to decode data from a string): {jj_avg} seconds')
