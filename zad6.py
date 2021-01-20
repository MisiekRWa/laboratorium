import copy
di = {'one': [1], 'two': [2], 'three': [3], 'four': [4]}
diCopy = copy.deepcopy(di)
print(di)
print(diCopy)
di['four'][0] = 'cztery'
print(di)
print(diCopy)