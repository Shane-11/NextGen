t = 9
name = 'Mr. T'
animal = 'hippo'

# print(vars())

d = vars().copy()

for k in d:
    print(d[k])

print('__name__ =', d['__name__'])

# for k in d:
#     print(k, ':', d[k])

# for k, v in d.items():
#     # if k[0] != '_':   excludes underscore
#     if '_' not in k:
#         print(k, ':', v)
#
# # print the value of __name__
# # Do the following
# print(__name__)