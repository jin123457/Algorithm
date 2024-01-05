row,col = map(int,input().split())
total = 0
dire = "row"
while True :
    if col == 1 or row == 1 :break
    if dire == "row" :
        row -= 1
    else :
        col -= 1

    total += 1
    dire = "col" if dire == "row" else "row"

if row > 1 or col > 1 :
    print(total + 1)
else :
    print(total)