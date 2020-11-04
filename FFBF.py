import math


def firstFit(blockSize, m, processSize, n):
    allocation = [-1] * n

    for i in range(n):
        for j in range(m):
            if blockSize[j] >= processSize[i]:
                allocation[i] = j

                blockSize[j] -= processSize[i]

                break

    print(" Process No. Process Size      Block no.")
    for i in range(n):
        print(" ", i + 1, "         ", processSize[i],
              "         ", end=" ")
        if allocation[i] != -1:
            print(allocation[i] + 1)
        else:
            print("Not Allocated")


def bestFit(blockSize, m, processSize, n):
    allocation = [-1] * n

    for i in range(n):

        bestIdx = -1
        for j in range(m):
            if blockSize[j] >= processSize[i]:
                if bestIdx == -1:
                    bestIdx = j
                elif blockSize[bestIdx] > blockSize[j]:
                    bestIdx = j

        if bestIdx != -1:
            allocation[i] = bestIdx

            blockSize[bestIdx] -= processSize[i]

    print("Process No. Process Size     Block no.")
    for i in range(n):
        print(i + 1, "         ", processSize[i],
              end="         ")
        if allocation[i] != -1:
            print(allocation[i] + 1)
        else:
            print("Not Allocated")


if __name__ == '__main__':
    BlockValue = 900
    processSize = [379, 395, 760, 379, 241, 200, 105, 40, 395, 105]
    m = math.ceil((sum(processSize))/BlockValue)
    blockSize =[]
    for x in range(m):
        blockSize.append(BlockValue)
    #m = len(blockSize)
    n = len(processSize)
    firstFit(blockSize, m, processSize, n)
    print("Кол-во процессов:", m, "\n")

    processSize = [379, 395, 760, 379, 241, 200, 105, 40, 395, 105]
    m = math.ceil((sum(processSize)) / BlockValue)
    processSize.sort(reverse=True)
    blockSize = []
    for x in range(m):
        blockSize.append(BlockValue)
    # m = len(blockSize)
    n = len(processSize)
    bestFit(blockSize, m, processSize, n)
    print("Кол-во процессов:", m)

