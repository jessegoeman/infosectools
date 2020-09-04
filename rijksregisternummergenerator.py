# generate rijksregisternummer

def rijksregisternummer(eerstecijfers):
    for i in range(0, 99999):
        aantal = len(str(i))
        f = (5 - aantal) * "0"
        cijf = f + str(i)
        rrnr = str(eerstecijfers) + str(cijf)
        rrnrA = int(rrnr[:9])
        rrnrC = int(rrnr[9:])
        controle = 97 - (rrnrA % 97)
        if controle == rrnrC:
            print("nummer is: " + str(rrnr))
x = 981021
print(rijksregisternummer(x))