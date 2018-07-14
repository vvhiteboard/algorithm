
class Cow:
    def __init__(self, element):
        self.element = element
        self.favoriteStables = set({})
        self.stable = None

    def addFavortieStable(self, stable):
        self.favoriteStables.add(stable)

    def setStable(self, stable):
        self.favoriteStables.remove(stable)
        self.stable = stable

    def changeStable(self, stable):
        if self.stable is not None:
            self.favoriteStables.add(self.stable)
        self.favoriteStables.remove(stable)
        self.stable = stable

    def isEmpty(self):
        return self.stable is None

def allocateAll(cows, allocatedStable):
    unAllocatedCows = set({})

    for num in cows.keys():
        cow = cows[num]

        if not cow.isEmpty():
            continue

        for stable in cow.favoriteStables:
            if stable not in allocatedStable:
                break

        if stable not in allocatedStable:
            allocatedStable[stable] = num
            cow.setStable(stable)
        else:
            unAllocatedCows.add(num)

    return unAllocatedCows


def reallocate(cows, cowNum, allocatedStable, reallocateTarget):
    cow = cows[cowNum]

    if cowNum in reallocateTarget:
        return False

    reallocateTarget.add(cowNum)

    for stable in cow.favoriteStables:
        if stable not in allocatedStable:
            allocatedStable[stable] = cowNum
            cow.changeStable(stable)
            return True

        isSuccess = reallocate(cows, allocatedStable[stable], allocatedStable, reallocateTarget)

        if isSuccess:
            allocatedStable[stable] = cowNum
            cow.changeStable(stable)
            return True

    return False

if __name__ == "__main__":
    arr = input().split(" ")
    cowNum = int(arr[0])
    stableNum = int(arr[1])
    cows = {}
    allocatedStable = {}

    for n in range(1, cowNum + 1):
        arr = input().split(" ")[1:]

        cow = Cow(n)
        for a in arr:
            cow.addFavortieStable(int(a))

        cows[n] = cow

    unAllocatedCows = allocateAll(cows, allocatedStable)
    # reallocateTarget = set({})
    beforeCows = set({})

    while len(unAllocatedCows) != len(beforeCows):
        newAllocatedCows = set({})
        beforeCows = unAllocatedCows

        for cowNum in unAllocatedCows:
            isSuccess = reallocate(cows, cowNum, allocatedStable, set({}))

            if isSuccess:
                newAllocatedCows.add(cowNum)

        unAllocatedCows = unAllocatedCows - newAllocatedCows

    print(len(allocatedStable))






"""
5 5
2 1 2
2 2 3
2 3 4
2 4 5
1 1
"""