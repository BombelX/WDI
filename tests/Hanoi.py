def TowerOfHanoi(n,rod1,rod3,rod2):
    if n == 0:
        return TowerOfHanoi(n-1,rod1,rod2,rod3)
    disk = rod1.pop()
    rod3.append(disk)
    TowerOfHanoi(n-1,rod2,rod3,rod1)

N = 3
rod1 = [3,2,1]
rod2 = []
rod3 = []

TowerOfHanoi(N,rod1,rod3,rod2)