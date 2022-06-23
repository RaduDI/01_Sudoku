sudoku_NOK = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [4, 5, 6, 7, 8, 9, 1, 2, 3],
    [7, 8, 9, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [4, 5, 6, 7, 8, 9, 1, 2, 3],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [4, 5, 6, 7, 8, 9, 1, 2, 3],
    [1, 1, 1, 4, 5, 6, 7, 8, 9]
]

sudoku_NOK_DI_Error = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [4, 5, 6, 7, 8, 9, 1, 2, 3],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [4, 5, 6, 7, 8, 9, 1, 2],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [4, 5, 6, 7, 8, 9, 1, 2, 3],
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
]

sudoku_OK = [
    [4, 3, 5, 2, 6, 9, 7, 8, 1],
    [6, 8, 2, 5, 7, 1, 4, 9, 3],
    [1, 9, 7, 8, 3, 4, 5, 6, 2],
    [8, 2, 6, 1, 9, 5, 3, 4, 7],
    [3, 7, 4, 6, 8, 2, 9, 1, 5],
    [9, 5, 1, 7, 4, 3, 6, 2, 8],
    [5, 1, 9, 3, 2, 6, 8, 7, 4],
    [2, 4, 8, 9, 5, 7, 1, 3, 6],
    [7, 6, 3, 4, 1, 8, 2, 5, 9]
]


# data input check: #coloane = #linii
def validareDataInput(matrix):
    for rand in range(len(matrix)):
        if len(matrix[rand]) != len(matrix):
            print("Error: matricea de sudoku nu este 9 x 9")
            return False


def validareSudoku(matrice):
    print("Functie validare sudoku")

    # validare pe OX
    for i in range(len(matrice)):
        set_Temp = set()
        for j in range(len(matrice)):
            set_Temp.add(matrice[i][j])
            if len(set_Temp) != j + 1:
                set_Temp.clear
                print("Error Ox")
                return False

    # validare pe OY
    for i in range(len(matrice)):
        set_Temp = set()
        for j in range(len(matrice)):
            set_Temp.add(matrice[j][i])
            if len(set_Temp) != j + 1:
                set_Temp.clear
                print("Error OY")
                return False

    # validare pe careu
    for i_0 in range(0, len(matrice) // 3):
        for j_0 in range(0, len(matrice) // 3):
            set_Temp = set()
            for i_1 in range(0, len(matrice) // 3):
                for j_1 in range(0, len(matrice) // 3):
                    set_Temp.add(matrice[i_1 + i_0 * 3][j_1 + j_0 * 3])
                    if len(set_Temp) != (i_1 * 3) + (j_1 + 1):
                        set_Temp.clear
                        print("Error Careu")
                        return False
    return True


def main():
    print("Test")
    matrice = sudoku_NOK
    if validareDataInput(matrice) == False:
        return
    else:
        if validareSudoku(matrice):
            print("Sudoku corect")
        else:
            print("Sudoku NOK")


if __name__ == "__main__":
    main()
