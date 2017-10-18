# -*- coding: utf-8 -*-
jed = open("JedilniList.txt", "w+")

print("Jedilni list")

jed.write("Jedilni list" "\n")
print("Vnesi jed na dnevni meni, nato dodaj še ceno: ")
i=1
while True:
    #dnjed=str(raw_input("Vnesi jed:"))
    #jed.write(dnjed + " ")

    jed.write(str(i) + ". "+ raw_input("Vnesi jed:") +" ")
    jed.write(raw_input("Vnesi ceno:") + "€\n")
    i += 1
    A=raw_input("Želiš vnesti še kakšno jed? (da/ne) ")
    if A.lower()=="da":
        continue
    else:
        break

jed.write("Vse cene vsebujejo ddv. Želimo vam dober tek!")
jed.close()