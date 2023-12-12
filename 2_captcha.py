def isnum(num):
    flag = True
    for x in range(len(num)):
        if not (num[x].isdigit() or (num[x] == '-' and x == 0)):
            if(num[x] == '.' and flag):
                flag = False
                continue
            # print("num[x] = ", num[x])
            return False
    return True

def isname(name):
    for x in name:
        if not x.islower():
            # print("x = ", x)
            return False
    return True

def dig_alpha(dig):
    if dig == '0':
        return "zer"
    elif dig == '1':
        return "one"
    elif dig == '2':
        return "two"
    elif dig == '3':
        return "thr"
    elif dig == '4':
        return "fou"
    elif dig == '5':
        return "fiv"
    elif dig == '6':
        return "six"
    elif dig == '7':
        return "sev"
    elif dig == '8':
        return "eig"
    elif dig == '9':
        return "nin"
    else:
        return "Invalid"

def todig(num):
    sum = 0
    for x in num:
        if(x == '.'):
            continue
        sum += int(x)
    if(sum < 10):
        return dig_alpha(str(sum))
    else:
        return todig(str(sum))
# main function

def main():
    t = int(input())
    for _ in range(t):
        num, name = input().split()
        # print(num, name)
        if isnum(num) and isname(name):
            isNeg = False
            dot = len(num)
            loc = -1
            dig = -1
            flag = True
            for x in range(len(num)):
                if num[x] == '-':
                    isNeg = True
                    continue
                if num[x] == '.':
                    dot = x
                    continue
                if int(num[x]) > 0 and int(num[x]) < 10 and flag:
                    loc = x
                    dig = num[x]
                    flag = False
            # print("loc = ", loc, "dig = ", dig, "dot = ", dot)
            ans=""
            if isNeg:
                ans += "-"
            ans += dig_alpha(dig)
            num = num[loc+1:]
            ans += "." + todig(num) 
            ans += "e"
            odd = True
            if dot == 1 and loc == 0:
                ans += 'zer'
                odd = False
            elif loc < dot:
                ans += '+' + dig_alpha(str(dot-loc-1))
                if (dot-loc-1) % 2 == 0:
                    odd = False
            else:
                ans += '-' + dig_alpha(str(loc-dot))
                if (loc-dot) % 2 == 0:
                    odd = False
            ans += "@"
            if odd:
                for x in name[::2]:
                    ans += x
            else:
                for x in name[1::2]:
                    ans += x
            # print("num = ", num)
            print(ans)
        else:
            print("Invalid")

if __name__ == '__main__':
    main()
