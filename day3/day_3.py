
grid = []

with open('2020_day_3_input', 'r') as input_file:
    for each_line in input_file:
        grid.append(each_line.split())

print ("--- PART 1 ---")

horizontal_length = len(grid[0][0])
horizontal_position=0
tree_counter=0

for i in range(len(grid)):
    if i == len(grid) - 1:
        break
    horizontal_position+=3
    if grid[i+1][0][horizontal_position%(horizontal_length)] == '#':
        tree_counter+=1

print("Part 1 Total: " + str(tree_counter))

print ("--- PART 2 ---")

def tree_encountered(grid_list, num_of_right_pos, num_of_down_pos):
    horizontal_length = len(grid_list[0][0])
    horizontal_position=0
    tree_counter=0
    for i in range(0, len(grid_list), num_of_down_pos):
        if i >= len(grid_list) - num_of_down_pos:
            break
        horizontal_position+=num_of_right_pos
        if grid_list[i+num_of_down_pos][0][horizontal_position%(horizontal_length)] == '#':
            tree_counter+=1
    return tree_counter

r1d1=tree_encountered(grid, 1, 1)
r3d1=tree_encountered(grid, 3, 1)
r5d1=tree_encountered(grid, 5, 1)
r7d1=tree_encountered(grid, 7, 1)
r1d2=tree_encountered(grid, 1, 2)
print("Part 2 r1d1 Total: " + str(r1d1))
print("Part 2 r3d1 Total: " + str(r3d1))
print("Part 2 r5d1 Total: " + str(r5d1))
print("Part 2 r7d1 Total: " + str(r7d1))
print("Part 2 r1d2 Total: " + str(r1d2))
print("Part 2 Product Total: " + str(r1d1*r3d1*r5d1*r7d1*r1d2))
