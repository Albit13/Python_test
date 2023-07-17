def read_last(file_path, symbol_number):
    with open(file_path, 'r') as file:
        for line in file:
            line = line.rstrip('\n')
            if line.strip():
                last_symbols = line[-symbol_number:]
                print(last_symbols)

read_last('read_last.txt', 6)
