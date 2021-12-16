import json

fileName = "www_2s_new_size_10.json"

def getData(fileName):
    
    # Opening JSON file
    with open(fileName, 'r') as f:
        data = json.load(f)
    return data


data = getData(fileName)

print("--- level 0 length ---")
print(len(data))

for index1, subData1 in enumerate(data):
    print("--- level 1 length ---")
    print(index1)
    print(len(subData1))
    for key2 in subData1:
        value2 = subData1[key2]
        print("--- level 2 length ---")
        print(key2)
        print(len(value2))


# Correct:

# --- level 0 length ---
# 2
# --- level 1 length ---
# 0
# 3
# --- level 2 length ---
# train
# 10
# --- level 2 length ---
# dev
# 10
# --- level 2 length ---
# test
# 10
# --- level 1 length ---
# 1
# 3
# --- level 2 length ---
# train
# 10
# --- level 2 length ---
# dev
# 10
# --- level 2 length ---
# test
# 10