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

# Using regular dictionaries
jj_times = []
jj = {}
jj_total_start = perf_counter()
for _ in range(iterations):
    start = perf_counter()
    jj['b'] = 'bbc'
    jj_times.append(perf_counter() - start)
jj_total = perf_counter() - jj_total_start

# Using classyjson's custom dicts
cj_times = []
cj = {}
cj_total_start = perf_counter()
for _ in range(iterations):
    start = perf_counter()
    cj.b = 'bbc'
    cj_times.append(perf_counter() - start)
cj_total = perf_counter() - cj_total_start

jj_avg = sum(jj_times) / len(jj_times)
cj_avg = sum(cj_times) / len(cj_times)

print('\n\n setting an attribute / key to a value:')
print(' regular dicts: {:2.8f} seconds || total time: {} || total iterations: {}'.format(round(jj_avg, 8), round(jj_total, 4), iterations))
print('   classy-json: {:2.8f} seconds || total time: {} || total iterations: {}'.format(round(cj_avg, 8), round(cj_total, 4), iterations))

iterations = 1000000

# Using regular dictionaries
jj_times = []
jj = {'b': {'hellothere': ['general kenobi']}}
jj_total_start = perf_counter()
for _ in range(iterations):
    start = perf_counter()
    jj['b']['hellothere']
    jj_times.append(perf_counter() - start)
jj_total = perf_counter() - jj_total_start

# Using classyjson's custom dicts
cj_times = []
cj = classyjson.CustomTypes.objectify({'b': {'hellothere': ['general kenobi']}})
cj_total_start = perf_counter()
for _ in range(iterations):
    start = perf_counter()
    cj.b.hellothere
    cj_times.append(perf_counter() - start)
cj_total = perf_counter() - cj_total_start

jj_avg = sum(jj_times) / len(jj_times)
cj_avg = sum(cj_times) / len(cj_times)

print('\n\n getting an attribute / key:')
print(' regular dicts: {:2.8f} seconds || total time: {} || total iterations: {}'.format(round(jj_avg, 8), round(jj_total, 4), iterations))
print('   classy-json: {:2.8f} seconds || total time: {} || total iterations: {}'.format(round(cj_avg, 8), round(cj_total, 4), iterations))
