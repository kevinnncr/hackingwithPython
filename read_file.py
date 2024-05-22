def read_lines(filename, num_lines):
    with open (filename, 'r') as file:
        for _ in range(num_lines):
            line= file.readline()
            if not line:
                break
            print(line.strip())


read_lines('estudiantes.txt', 2)            