x = int()                                   ## Memperkenalkan variable x sebagi intenger, kemudian menginputkan nilainya
y = 0                                       ## Mempekenalkan variable y dengan nilai 0
while x >= 0:                               ## Looping WHILE apabila nilai x lebih besar dari nilai 0
    x = int(input("Masukkan Bilangan: "))   ## Program yang akan dilooping
    if x > y:                               ## If kondisi apabila nilai x lebih besar dari nilai y
        y = int(x)                          ## Nilai y sama dengan nilai x
    if x == 0:                              ## If kondisi apabila nilai x sama dengan 0
        break                               ## Fungsi yang menghentikan operasi dibawahnya jika suatu kondisi yang ditentukan
print("\nAngka Terbesar Adalah ",y)         ## Mencetak bilangan terbesar