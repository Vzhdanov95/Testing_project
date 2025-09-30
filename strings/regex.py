import re

text = 'Homer Simpson, HomerSimpson, Homer Simpson, Homer Simpson, Homer Simpson'

result = re.findall(r'\bH\w*\s+S\w*', text)
print(result)