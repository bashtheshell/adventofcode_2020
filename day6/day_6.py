data = []
with open('2020_day_6_input', 'r') as input_file:
    for i in input_file.read().split('\n\n'):
        data.append(i.split())

print ("--- PART 1 ---")

num_answer_list = []
for i in range(len(data)):
    answer=""
    for j in range(len(data[i])):
        answer=answer+''.join([ x for x in data[i][j] if x not in answer]) 
    num_answer_list.append(len(answer))

total = 0
for i in num_answer_list:
    total+=i

print(f"Part 1 Total: {total}")



