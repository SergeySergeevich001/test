def main():
    tradersData = [int(i) for i in input().split()]

    listOfBonds = []

    while True:
        bond = input()
        if bond != "":
            listOfBonds.append([i for i in bond.split()])
        else:
            break

    enteredData(tradersData, listOfBonds)
    selectBonds(tradersData, listOfBonds)


def enteredData(tradersData, listOfBonds):
    for i in range(len(listOfBonds)):
        data = calculatedData(tradersData, listOfBonds[i])
        listOfBonds[i].extend(data)


def calculatedData(tradersData, one_bond_data):
    day = int(one_bond_data[0])
    name = one_bond_data[1]
    cost = float(one_bond_data[2])
    count = int(one_bond_data[3])

    countDays = tradersData[0]
    maxCountDayLots = tradersData[1]
    money = tradersData[2]

    bondIncome = countDays - day + 30
    bondCost = round((1000 - cost / 100 * 1000),1)

    return [round((cost / 100 * 1000 * count), 1), (bondCost + bondIncome) * count, bondCost + bondIncome]


def selectBonds(tradersData, listOfBonds):
    dataReceiveTable = [[[0, 0, []] for _ in range(0, int(tradersData[2]), 1000)] for _ in range(len(listOfBonds) + 1)]
    listOfBonds.sort(key=lambda x: x[6], reverse=True)
    gain = 0
    for i in range(len(listOfBonds)):
        for j in range(int(tradersData[2] // 1000)):
            if ((j + 1) - int(listOfBonds[i][4]) // 1000) > 0:
                if (dataReceiveTable[i][((j + 1) - int(listOfBonds[i][4]) // 1000)][0] + listOfBonds[i][4] <= (j + 1) * 1000):
                    if (dataReceiveTable[i][((j + 1) - int(listOfBonds[i][4]) // 1000)][1] + listOfBonds[i][5]) > dataReceiveTable[i][j][1]:
                        dataReceiveTable[i+1][j][1] = dataReceiveTable[i][j-int(listOfBonds[i][4]) // 1000][1] + listOfBonds[i][5]
                        dataReceiveTable[i+1][j][0] = dataReceiveTable[i][j-int(listOfBonds[i][4]) // 1000][0] + listOfBonds[i][4]
                        dataReceiveTable[i + 1][j][2] = dataReceiveTable[i][j - int(listOfBonds[i][4] // 1000)][2].copy()
                        dataReceiveTable[i + 1][j][2].append(listOfBonds[i])
                    else:
                        dataReceiveTable[i + 1][j][2] = dataReceiveTable[i][j][2].copy()
                        dataReceiveTable[i + 1][j][1] = dataReceiveTable[i][j][1]
                        dataReceiveTable[i + 1][j][0] = dataReceiveTable[i][j][0]
                else:
                    dataReceiveTable[i + 1][j][2] = dataReceiveTable[i][j][2].copy()
                    dataReceiveTable[i + 1][j][1] = dataReceiveTable[i][j][1]
                    dataReceiveTable[i + 1][j][0] = dataReceiveTable[i][j][0]
            else:
                dataReceiveTable[i + 1][j][2] = dataReceiveTable[i][j][2].copy()
                dataReceiveTable[i + 1][j][1] = dataReceiveTable[i][j][1]
                dataReceiveTable[i + 1][j][0] = dataReceiveTable[i][j][0]

    print(dataReceiveTable[-1][-1][1])
    for bond in dataReceiveTable[-1][-1][2]:
        print(" ".join(bond[:4]))

def test():
    tradersData = [2, 2, 8000]
    listOfBonds = [['1', 'alfa-05', '100.2', '2'], ['2', 'alfa-05', '101.5', '5'], ['2', 'gazprom-17', '100.0', '2']]

    enteredData(tradersData, listOfBonds)

    selectBonds(tradersData, listOfBonds)


test()
