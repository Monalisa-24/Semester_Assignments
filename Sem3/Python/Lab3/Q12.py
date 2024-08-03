def tablePrinting(r,c):
    for i in range(1, r+1):
        r = [str(i)]
        for j in range(c-1):
            r.append(str(i ** j))
        print(" ".join(r))

tablePrinting(5,5)