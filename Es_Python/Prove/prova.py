somma = 0
for i in range (7,10):
    print("sto sommando ",i, "...")
    somma+=i

print("somma 1: ", somma)
print("\n")

somma = 0
for i in range (5,11,2):
    #controllo di sicurezza
    if i == 9:
        break
    print("sto sommando ",i, "...")
    somma+=i
    print("somma 2: ", somma)

s = "abcdefgh"
for char in s:
    print (char)
    if char == 'c' or char == 'h':
        print("Trovato i o u")
