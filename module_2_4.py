def get_matrix(n, m, value):
    matrix = [] # Создаём пустой список для матрицы
    for _ in range(n): # Внешний цикл для строк
        row = []
        for _ in range(m): # Внутренний цикл для столбцов
            row.append(value) # Добавляем значение в строку
        matrix.append(row) # Добавляем строку в матрицу
    return matrix # Возвращаем готовую матрицу

result = get_matrix(7,12, 44) # Пример вызова функции
for row in result: # Вывод результата
    print(row)