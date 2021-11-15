#text: https://www.gutenberg.org/files/10/10-0.txt

file = 'Bible.txt'
with open(file, 'r') as file_in:
    lines = file_in.read().replace(",", " ").replace(".", " ").replace("(", "").replace(")", " ").lower().split()
from collections import Counter
print(Counter(lines))