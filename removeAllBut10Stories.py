import json

fileName = "../../Verifiable-Coherent-NLU/all_data/www_2s_new.json"

def getData(fileName):
    
    # Opening JSON file
    with open(fileName, 'r') as f:
        data = json.load(f)
    return data


data = getData(fileName)

newOverallData = []

for index1, sub1Data in enumerate(data):
    newOverallData.append({})
    for sub2DataKey in sub1Data:
        sub2DataValue = sub1Data[sub2DataKey]
        newData = sub2DataValue[:10]
        newOverallData[index1][sub2DataKey] = newData


outFileName = "www_2s_new_size_10.json"

with open(outFileName, 'w') as outfile:
    json.dump(newOverallData, outfile)