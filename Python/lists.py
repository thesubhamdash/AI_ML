marks = [99, 95, 92, 100]

idx=0
key = 100

for val in marks:
    if(val == key):
        print(f"{key} found at index: {idx}")
        break
    idx += 1
