import re

c = 'Qeeeee Wrrrr asasas'
s = re.search(r'^[a-z][a-z]*', c)
print(s)
