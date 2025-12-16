password = 0
dial = 50

with open("input.txt") as file:
    for line in file:
        line = line.strip()
        dial += (2*(ord(line[0])//82)-1)*int(line[1:])
        print(line,dial)
        password += int(dial<0 or dial>100)*(abs(dial)//100+int(dial<0))
        dial %= 100
        password += int(not dial)

print(password)