db = []
total=0

with open('2020_day_2_input', 'r') as input_file:
    for each_line in input_file:
        db.append(each_line.split())

print ("--- PART 1 ---")

for line in db:
    letter_count = line[2].count(line[1][0])
    minimum_num = int(line[0].split('-')[0])
    maximum_num = int(line[0].split('-')[1])

    if letter_count >= minimum_num and letter_count <= maximum_num:
        total+=1
        # print(str(line) + " - " + str(total))

print("Part 1 Total: " + str(total))

print ("--- PART 2 ---")
total=0

for line in db:
    first_char_index = line[2].find(line[1][0], int(line[0].split('-')[0]) - 1, int(line[0].split('-')[0]))
    second_char_index = line[2].find(line[1][0], int(line[0].split('-')[1]) - 1, int(line[0].split('-')[1]))

    if (first_char_index != -1 and second_char_index == -1) or (first_char_index == -1 and second_char_index != -1):
        # print(str(line) + " -  " + str(first_char_index) + "  " +  str(second_char_index))
        total+=1

print("Part 2 Total: " + str(total))


    