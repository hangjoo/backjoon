roads = [
    ["ULSAN", "BUSAN"],
    ["DAEJEON", "ULSAN"],
    ["DAEJEON", "GWANGJU"],
    ["SEOUL", "DAEJEON"],
    ["SEOUL", "ULSAN"],
    ["DAEJEON", "DAEGU"],
    ["GWANGJU", "BUSAN"],
    ["DAEGU", "GWANGJU"],
    ["DAEGU", "BUSAN"],
    ["ULSAN", "DAEGU"],
    ["GWANGJU", "YEOSU"],
    ["BUSAN", "YEOSU"],
]

tot_count = 0


def search(src, hub, dst, line):
    line[src]["visited"] = True

    if src == dst:
        if line[hub]["visited"]:
            line[dst]["arrived"] += 1

    else:
        for city in line[src]["dst"]:
            if city in line:
                if line[city]["visited"] == False:
                    search(city, hub, dst, line)


line = dict()
dst = {"count": 0}
for val in roads:
    if val[0] not in line:
        line[val[0]] = dict()
        line[val[0]]["dst"] = [val[1]]
        line[val[0]]["visited"] = False
        line[val[0]]["arrived"] = 0
    elif val[1] not in line:
        line[val[1]] = dict()
        line[val[1]]["dst"] = []
        line[val[1]]["visited"] = False
        line[val[1]]["arrived"] = 0
    else:
        line[val[0]]["dst"].append(val[1])

for idx, val in line.items():
    print(idx)
    print(val)

search("SEOUL", "DAEGU", "YEOSU", line)

print(line["YEOSU"]["arrived"])