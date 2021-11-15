#text: https://cooking.nytimes.com/recipes/1022727-classic-apple-pie

file = 'ApplePie.txt'
with open(file, 'r') as file_in:
    lines = file_in.read().replace(",", " ").replace(".", " ").replace("(", "").replace(")", " ").lower().split()
from collections import Counter
print(Counter(lines))