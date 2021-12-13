import os.path

#print(__file__)
#python_folder = os.path.dirname(__file__)
python_folder = 'C:/Temp'
print(python_folder)

def sum_space(some_folder):
    sum_bytes = 0
    for file in os.listdir(some_folder):
        f = os.path.join(some_folder, file)
        if os.path.isfile(f):
            sum_bytes += os.path.getsize(f)
        else:
            sum_bytes += sum_space(f)
    return sum_bytes

some_folder = 'C:/Temp'
print(some_folder)
sum_folders = sum_space(some_folder)
print('Sum space: {}'.format(sum_folders))

# 1. Include summing space occupied for folders with their content
# Hint: use recursion...
# Step 1: create a function that iterates over files in a folder and returns the sum of the size
# Step 2: add a condition for the case of a folder - then the function should call itself for
#         the subfolder as input parameter