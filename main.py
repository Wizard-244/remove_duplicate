print ("Remove duplicate")
print("Enter a character or numbers")
s_smbl = input()
f_smbl = ""
for i in range(len(s_smbl)):
    if f_smbl.find(s_smbl[i]) == -1 and s_smbl[i] != " ":
        f_smbl += s_smbl[i]
print("Clean data")
print(f_smbl)