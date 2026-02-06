n = int(input("Masukkan jumlah baris: "))

for i in range(n):
    # spasi di kiri
    print(" " * (n - i - 1), end="")

    # bintang
    for j in range(2 * i + 1):
        print("*", end=" ")

    print()
