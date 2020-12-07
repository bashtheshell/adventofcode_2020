seating=[]
with open('2020_day_5_input', 'r') as input_file:
    for i in input_file:
        seating.append(i.split())


print ("--- PART 1 ---")

from math import ceil

column_length = 3
row_length = len(seating[0][0]) - column_length
max_row = 127
max_column = 7

highest_seat_id = 0

# seating = [
# ['FBFBBFFRLR'],
# ['BFFFBBFRRR'],
# ['FFFBBBFRRR'],
# ['BBFFBBFRLL']]

for i in range(len(seating)):
    top_row = max_row
    bottom_row = 0
    right_column = max_column
    left_column = 0

    for j in range(row_length):
        if seating[i][0][j] == 'B':
            bottom_row = int(bottom_row + ceil((top_row - bottom_row) / 2))
        elif seating[i][0][j]  == 'F':
            top_row = int(top_row - ceil((top_row - bottom_row) / 2))
    for j in range(row_length, row_length + column_length):
        if seating[i][0][j]  == 'R':
            left_column = int(left_column + ceil((right_column - left_column) / 2)) 
        elif seating[i][0][j]  == 'L':
            right_column = int(right_column - ceil((right_column - left_column) / 2)) 

    # print(f"{seating[i][0]} - Top: {top_row} and Bottom: {bottom_row} and Left: {left_column} and Right: {right_column}")

    seat_id = (top_row * 8) + left_column
    if seat_id > highest_seat_id:
        highest_seat_id = seat_id

print("Part 1 Highest ID Value: " + str(highest_seat_id))

print ("--- PART 2 ---")

manifest = []

for i in range(len(seating)):
    top_row = max_row
    bottom_row = 0
    right_column = max_column
    left_column = 0

    for j in range(row_length):
        if seating[i][0][j] == 'B':
            bottom_row = int(bottom_row + ceil((top_row - bottom_row) / 2))
        elif seating[i][0][j]  == 'F':
            top_row = int(top_row - ceil((top_row - bottom_row) / 2))
    for j in range(row_length, row_length + column_length):
        if seating[i][0][j]  == 'R':
            left_column = int(left_column + ceil((right_column - left_column) / 2)) 
        elif seating[i][0][j]  == 'L':
            right_column = int(right_column - ceil((right_column - left_column) / 2)) 

    # print(f"{seating[i][0]} - Top: {top_row} and Bottom: {bottom_row} and Left: {left_column} and Right: {right_column}")

    seat_id = (top_row * 8) + left_column
    manifest.append(seat_id)

ordered_manifest = sorted(manifest)
missing_manifest = []
for i in range(len(ordered_manifest)):
    # print(ordered_manifest[i])
    if i == 0: # skip first index
        continue
    elif i == len(ordered_manifest) - 1: # skip last index
        break
    else:
        num_before = int(ordered_manifest[i-1])
        num_current = int(ordered_manifest[i])
        num_after = int(ordered_manifest[i+1])
        if num_before != (num_current - 1) or num_after != (num_current + 1):
            missing_manifest.append(num_current)

print(f"Part 2 Result is between: {missing_manifest[:1][0]} and {missing_manifest[1:][0]}")

