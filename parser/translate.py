from parser import result
print("### translate ###")

# init dicionaries
varDict = {}
actDict = {}

acc = 0
for item in result.variables:
    print(item)
    varDict[item] = acc
    acc += 1

acc = 5
for item in result.actions:
    print(item)
    actDict[item] = acc
    acc += 5

process_num = len(varDict)
print(process_num)
