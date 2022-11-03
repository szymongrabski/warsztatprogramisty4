n = int(input("Wpisz rozmiar: "))

print("rozmiar:", n)

for i in range(0,n+1,1):
    print(" "*(n-i),"* "*i)

print(" "*(n-3), "|___|")
