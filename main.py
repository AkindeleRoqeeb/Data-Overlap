with open('first_num.txt') as files1:
    new_1 = files1.readlines()

with open('second_num.txt') as files2:
    new_2 = files2.readlines()

new_list = []
for num in new_1:
    if num in new_2:
       print([int(num)])

##########################%%%%%%%%%%%% OR ###########%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

new_list = [int(num) for num in new_1 if num in new_2]
print(new_list)