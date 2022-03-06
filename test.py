from fractions import Fraction

# Fungsi untuk mencari bentuk baris eselon tereduksi/tak tereduksi dari matriks
def getRowEchelon(mat):
    row, col = len(mat), len(mat[0])
    lead = 0

    for i in range(row):
        # Mencari posisi nilai terdepan
        while lead < col and mat[i][lead] == 0:
            for j in range(i, row):
                if mat[j][lead] == 0: 
                    continue

                if i != j: 
                    mat[i], mat[j] = mat[j], mat[i]

                lead -= 1
                break

            lead += 1

        # Membagi semua elemen dalam i dengan nilai terdepan
        for j in range(col - 1, lead - 1, -1):
            mat[i][j] /= mat[i][lead]
        
        # Menjadikan mat[i][lead] sebagai pivot dan melakukan OBE pada baris lainnya
        for j in range(row):
            if j == i: 
                continue

            for k in range(col - 1, lead - 1, -1):
                mat[j][k] -= mat[j][lead] * mat[i][k]

        lead += 1

    return mat


# Input dengan matriks augmented dalam bentuk desimal atau pecahan
def matrixAugmentedInput(row, decimal = False):
    matrix = [list(map(float if decimal else Fraction, input().split())) for i in range(row)]
    return matrix


# Main Function
def main():
    row = int(input("Jumlah Baris: "))
    col = int(input("Jumlah Kolom: "))

    tipeInput = input("Input desimal atau bukan(ya/tidak): ")

    matrix = getRowEchelon(matrixAugmentedInput(row, tipeInput == "ya"))
    print(matrix)
    print()

    
    # Output desimal
    for i in matrix:
        print(i)

    # Output pecahan
    for i in matrix:
        res = ''
        
        for j in i:
            res += str(j) + '\t'

        print(res)


if __name__ == "__main__":
    main()