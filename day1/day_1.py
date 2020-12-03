
entries = []

with open('2020_day_1_input', 'r') as input_file:
    entries = input_file.read().splitlines()

first_addend = second_addend = tuple(entries)

### PART 1
print ("--- PART 1 ---")

for i in first_addend:
    found = False
    for j in second_addend:
        #print(str(i) + " + " + str(j) + " = " + str(int(i) + int(j) ))
        
        if (int(i) + int(j)) == 2020:
            print(str(i) + " + " + str(j) + " = 2020. Product is " + str(int(i) * int(j)))
            found = True
            break
    if found:
        break

### PART 2
print ("--- PART 2 ---")

third_addend = tuple(entries)
for i in first_addend:
    found = False
    for j in second_addend:
        for k in third_addend:
            if (int(i) + int(j) + int(k)) == 2020:
                print(str(i) + " + " + str(j) + " + " + str(k) + " = 2020. Product is " + str(int(i) * int(j) * int(k)))
                found = True
                break
        if found:
            break
    if found:
        break


