def ondernemingsnummer(eerstecijfers):
    for i in range(0, 9999):
        aantal = len(str(i))
        f = (4 - aantal) * "0"
        cijf = f + str(i)
        rrnr = str(eerstecijfers) + str(cijf)
        rrnrA = int(rrnr[:9])
        rrnrC = int(rrnr[9:])
        controle = 97 - (rrnrA % 97)
        if controle == rrnrC:
            print("nummer is: " + str(rrnr))
#x = 981021
x = "073634"
print(ondernemingsnummer(x))