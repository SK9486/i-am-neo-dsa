def findsubStr(n):
    if(len(n) == 1):
        print(f"{n} has only 1 char")
        return " "

    for a in range(1,max+1):
        fst = n[s:s+a]
        sec = n[s+a:s+(2*a)]
        if(sec == " " or sec == ""):
            print("sec become empty")
        print(f"frst : {fst} seco : {sec}")
        if(fst == sec):
            global sum
            sum = sum +1
            print("match found with n : ",a)
            print("sum : ",sum)
            m = n[a:len(n)+1]
            print("new str : ",m)
            return m
n = input()
min = 0
max = int(len(n)/2)
s = 0
sum = 0
m = findsubStr(n)
s = findsubStr(m)
k = findsubStr(s)
# n = findsubStr(n)
# print(max)
