input = []

with open('input3.txt') as input_file:
    for line in input_file:
        input.append(line.strip())

width = len(input[0])
gamma_input = input[:]
for pos in range(0, width):
    one_count = 0
    for line in gamma_input:
        one_count += int(line[pos])
    if one_count >= len(gamma_input) / 2:
        gamma_input = [line for line in gamma_input if line[pos] == "1"]
    else:
        gamma_input = [line for line in gamma_input if line[pos] == "0"]

    if len(gamma_input) == 1:
        break
gamma = gamma_input[0]

epsilon_input = input[:]
for pos in range(0, width):
    one_count = 0
    for line in epsilon_input:
        one_count += int(line[pos])
    if one_count >= len(epsilon_input) / 2:
        epsilon_input = [line for line in epsilon_input if line[pos] == "0"]
    else:
        epsilon_input = [line for line in epsilon_input if line[pos] == "1"]

    if len(epsilon_input) == 1:
        break
epsilon = epsilon_input[0]

gamma_int = 0
epsilon_int = 0
for i in range(0, width):
    gamma_int += int(gamma[width-i-1]) * pow(2, i)
    epsilon_int += int(epsilon[width-i-1]) * pow(2, i)
print(gamma_int * epsilon_int)