class Symbol:
    def __init__(self, char, probability):
        self.char = char
        self.probability = probability
        self.code = ""


def get_split_index(list):
    diff_list = []
    sum = 0.0
    for symbol in list:
        sum += symbol.probability
    half = float(sum / 2)
    # print(f'Half: {half}')

    suma = 0.0
    for i in range(0, len(list)):
        suma += list[i].probability
        diff = round(abs(half-suma),3)
        diff_list.append([diff, i])


    diff_list = sorted(diff_list)
   
    return diff_list[0][1]

def calculate_symbol_codes(list):
    seperation_index = get_split_index(list) + 1

    first_list = list[0:seperation_index]
    second_list = list[seperation_index:len(list)]

    for symbol in first_list:
        symbol.code += "0"
    if len(first_list) > 1:
        calculate_symbol_codes(first_list)

    for symbol in second_list:
        symbol.code += "1"
    if len(second_list) > 1:
        calculate_symbol_codes(second_list)

    for element in second_list:
        first_list.append(element)

    return first_list

# write probability in descending order
symbols_list = [Symbol('a', 0.35), Symbol('b', 0.17), Symbol('c', 0.17), Symbol('d', 0.16), Symbol('e', 0.15)]
# symbols_list = [Symbol('a', 0.3), Symbol('e', 0.3), Symbol('d', 0.2), Symbol('b', 0.1), Symbol('c', 0.1)]
# symbols_list = [Symbol('a', 0.5), Symbol('i', 0.2), Symbol('s', 0.15), Symbol('d', 0.15)]
measured_symbols = calculate_symbol_codes(symbols_list)
for symbol in measured_symbols:
    print(symbol.char, symbol.probability, symbol.code)

