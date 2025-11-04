str = input()

result = ""

for n in range(len(str)):
    if str[n].isupper() == True:
        result += str[n].lower()
    else:
        result += str[n].upper()
        
print(result)