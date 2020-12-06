
data = ""
with open('2020_day_4_input', 'r') as input_file:
    data = input_file.read()

passport_list=[i.split() for i in data.split('\n\n')]


print ("--- PART 1 ---")

num_of_valid_passport=0

for i in range(len(passport_list)):
    fields_list = []

    fields_list.append(any('byr:' in x for x in passport_list[i]))
    fields_list.append(any('iyr' in x for x in passport_list[i]))
    fields_list.append(any('eyr:' in x for x in passport_list[i]))
    fields_list.append(any('hgt:' in x for x in passport_list[i]))
    fields_list.append(any('hcl:' in x for x in passport_list[i]))
    fields_list.append(any('ecl:' in x for x in passport_list[i]))
    fields_list.append(any('pid:' in x for x in passport_list[i]))
    
    if all(fields_list):
        num_of_valid_passport+=1

print("Part 1 Total: " + str(num_of_valid_passport))


print ("--- PART 2 ---")

def field_data_validator(p_list, field_name):
    entry = [x for x in p_list if field_name in x]
    if entry:
        f_name = entry[0].split(':')[0]
        f_value = entry[0].split(':')[1]

        if f_name == 'byr':
            if int(f_value) >= 1920 and int(f_value) <= 2002:
                return True
        if f_name == 'iyr':
            if int(f_value) >= 2010 and int(f_value) <= 2020:
                 return True
        if f_name == 'eyr':
            if len(f_value) == 4 and (int(f_value) >= 2020 and int(f_value) <= 2030):
                return True
        if f_name == 'hgt':
            unit = f_value.lstrip('0123456789')
            num_value = int(f_value.rstrip('cmin'))
            if unit == 'cm' and (num_value >= 150 and num_value <= 193):
                return True
            elif unit == 'in' and (num_value >= 59 and num_value <= 76):
                return True
        if f_name == 'hcl':
            if (f_value[:1] == '#' and len(f_value) == 7) and all([(x in ('1234567890abcdef')) for x in f_value[1:]]):
                return True
        if f_name == 'ecl':
            if [x for x in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth') if x in f_value]:
                return True
        if f_name == 'pid':
            if len(f_value) == 9 and f_value.isnumeric():
                return True
            
    else:
        return False

num_of_valid_passport=0

for i in range(len(passport_list)):
    fields_list = []

    fields_list.append(field_data_validator(passport_list[i], 'byr:'))
    fields_list.append(field_data_validator(passport_list[i], 'iyr:'))
    fields_list.append(field_data_validator(passport_list[i], 'eyr:'))
    fields_list.append(field_data_validator(passport_list[i], 'hgt:'))
    fields_list.append(field_data_validator(passport_list[i], 'hcl:'))
    fields_list.append(field_data_validator(passport_list[i], 'ecl:'))
    fields_list.append(field_data_validator(passport_list[i], 'pid:'))

    if all(fields_list):
        num_of_valid_passport+=1

print("Part 2 Total: " + str(num_of_valid_passport))
