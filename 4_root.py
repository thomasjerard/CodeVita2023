def sortbytax(x):
    return -x[1],x[2],x[0]
    
mintax=0

def dfs(root, startcity, parent="", tax=0):
    global mintax
    mintax += tax
    print(startcity, end="-")
    for x in root[startcity]:
        if x[0] == parent:
            continue
        dfs(root, x[0], startcity, x[2])
        mintax += tax
        print(startcity, end="-")

def main():
    n = int(input())
    root = {}

    while(True):
        try:
            line = input()
        except EOFError:
            break
        startcity, endcity, goods, tax = line.split()
        # print(startcity, endcity, goods, tax)
        goods = int(goods)
        tax = int(tax)
        root.setdefault(startcity, []).append((endcity, goods, tax))
        root.setdefault(endcity, []).append((startcity, goods, tax))
    
    for x in root:
        root[x] = sorted(root[x], key= sortbytax)
        # print(x, root[x])
    global mintax
    dfs(root, "hyderabad")
    print()
    print(mintax)

if __name__ == "__main__":
    main()