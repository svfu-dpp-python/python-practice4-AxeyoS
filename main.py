import os

def find_maximums(filename):
    max_numbers = []
    with open(filename, 'r') as file:
        for line in file:
            numbers = list(map(int, line.split()))
            if numbers:  # проверяем, что строка не пустая
                max_numbers.append(max(numbers))
    return max_numbers

def write_range(filename, a, b):
    with open(filename, 'w') as file:
        for number in range(a, b):
            file.write(f"{number}\n")

def count_files(directory):
    return len(os.listdir(directory))

def open_in_notepad(filename):
    os.system(f'notepad {filename}')

if __name__ == "__main__":
    # Тестируем find_maximums
    test_file = 'test_numbers.txt'
    with open(test_file, 'w') as f:
        f.write("1 2 3 4 5\n6 7 8 9\n-1 -2 -3\n")
    print(find_maximums(test_file))
    
    # Тестируем write_range
    test_range_file = 'range_numbers.txt'
    write_range(test_range_file, 1, 5)
    with open(test_range_file, 'r') as f:
        print(f.read())
    
    # Тестируем count_files
    test_dir = '.'
    print(count_files(test_dir))
    
    # Тестируем open_in_notepad
    open_in_notepad(test_file)  # Открытие файла test_numbers.txt в блокноте