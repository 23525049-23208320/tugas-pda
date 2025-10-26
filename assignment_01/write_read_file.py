# create file
with open('intpos_file.txt', 'w') as file:

    i = 1
    while i <= 10:
        # input angka
        input_angka = input("Masukkan angka positif ke "+str(i)+": ")
        angka = int(input_angka)

        if angka < 0:
            print(" Anda memasukkan angka negatif! Silakan masukkan angka positif kembali.")
        else:
            # write file
            file.write(str(angka)+'\n')
            i += 1

# read file
print("\nRead file intpos_file.txt")
with open("intpos_file.txt", "r") as file_read:
    positif = file_read.read()

print(positif)