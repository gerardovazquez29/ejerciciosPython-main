def encontrar_vacio(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                return (i, j)
    return None
def es_valido(sudoku, fila, col, num):
    for j in range(9):
        if sudoku[fila][j] == num:
            return False
        
    for i in range(9):
        if sudoku[i][col] == num:
            return False
        
    inicio_fila, inicio_col = 3 * (fila // 3), 3 * (col // 3)
    for i in range(inicio_fila, inicio_fila + 3):
        for j in range(inicio_col, inicio_col + 3):
            if sudoku[i][j] == num:
                return False
    return True

def resolver(sudoku):
    encontrado = encontrar_vacio(sudoku)
    if encontrado is None:
        return True
    fila, col = encontrado
    for num in range(1, 10):
        if es_valido(sudoku, fila, col, num):
            sudoku[fila][col] = num
            if resolver(sudoku):
                return True
            sudoku[fila][col] = 0
    return False
def imprimir_sudoku(sudoku):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            if j == 8:
                print(sudoku[i][j])
            else:
                print(sudoku[i][j], end=" ")
if __name__ == "__main__":
    ejemplo_sudoku = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    print("Sudoku original:")
    imprimir_sudoku(ejemplo_sudoku)
    if resolver(ejemplo_sudoku):
        print("Sudoku resuelto:")
        imprimir_sudoku(ejemplo_sudoku)
    else:
        print("No hay solución")