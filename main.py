#kezdet: 13:46

print("1. feladat ")

# feladat = input("Adja meg a bemeneti fájl nevét! ")
feladat = "konnyu.txt"
sudoku_table = []
with open(feladat, "r", encoding="UTF-8") as file:
    for sorok in file.readlines()[0:9]:
        uj_sor = [int(i) for i in sorok.split(" ")]
        sudoku_table.append(uj_sor)
 
sor = int(input("Adja meg egy sor számát! "))
oszlop = int(input("Adja meg egy oszlop számát! "))

print("\n3. feladat ")
print(f"Az adott helyen szereplő szám: {sudoku_table[oszlop-1][sor-1]}")

#lol melyik résztáblához tartozik a szam, ez erdekes

szotar = {
    (1,1): 1,
    (1,2): 1,
    (1,3): 1,
    (1,4): 2,
    (1,5): 2,
    (1,6): 2,
    (1,7): 3,
    (1,8): 3,
    (1,9): 3,

    (2,1): 1,
    (2,2): 1,
    (2,3): 1,
    (2,4): 2,
    (2,5): 2,
    (2,6): 2,
    (2,7): 3,
    (2,8): 3,
    (2,9): 3,

    (3,1): 1,
    (3,2): 1,
    (3,3): 1,
    (3,4): 2,
    (3,5): 2,
    (3,6): 2,
    (3,7): 3,
    (3,8): 3,
    (3,9): 3,

    (4,1): 4,
    (4,2): 4,
    (4,3): 4,
    (4,4): 5,
    (4,5): 5,
    (4,6): 5,
    (4,7): 6,
    (4,8): 6,
    (4,9): 6,

    (5,1): 4,
    (5,2): 4,
    (5,3): 4,
    (5,4): 5,
    (5,5): 5,
    (5,6): 5,
    (5,7): 6,
    (5,8): 6,
    (5,9): 6,

    (6,1): 4,
    (6,2): 4,
    (6,3): 4,
    (6,4): 5,
    (6,5): 5,
    (6,6): 5,
    (6,7): 6,
    (6,8): 6,
    (6,9): 6,

    (7,1): 7,
    (7,2): 7,
    (7,3): 7,
    (7,4): 8,
    (7,5): 8,
    (7,6): 8,
    (7,7): 9,
    (7,8): 9,
    (7,9): 9,

    (8,1): 7,
    (8,2): 7,
    (8,3): 7,
    (8,4): 8,
    (8,5): 8,
    (8,6): 8,
    (8,7): 9,
    (8,8): 9,
    (8,9): 9,

    (9,1): 7,
    (9,2): 7,
    (9,3): 7,
    (9,4): 8,
    (9,5): 8,
    (9,6): 8,
    (9,7): 9,
    (9,8): 9,
    (9,9): 9,
}

print(f"A hely a(z) {szotar[(sor, oszlop)]} résztáblázathoz tartozik. ")

print("4. feladat ")
nullaszamlalo = 0
for sor in sudoku_table:
    for szam in sor:
        if szam == 0:
            nullaszamlalo += 1
#sulipy megoldása:
print(f"Az üres helyek aránya: {nullaszamlalo / 81 * 100:.1f}")


#szunet: 14:23
szam1, szam2 = 0,0 
print(f"5. feladat ")
print(f"A kiválasztott sor: {szam1 := int(input(''))} oszlop: {szam2 := int(input('')} a szám: ", end="")
print(sudoku_table[szam2-1][szam1-1])
