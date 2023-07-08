print("=============================================")
print("========= KASIR RUMAH MAKAN PADANG ==========")
print("=========       MINANG RAYA        ==========")
print("========= Jl. Raya Pakuan - Bogor ===========")
print("=============================================")

pembeli = input("Nama Pembeli : ") 


def fungsimakanan (): 
    global total1 
    global porsi
    global jenis1
    print("\nMenu Makan")
    print("1. Nasi Rendang - Rp15.000")
    print("2. Nasi Ayam Goreng - Rp18.000")
    print("3. Nasi Telur Dadar - Rp12.000")
    print("4. Nasi Ayam Gulai - Rp20.000")
    print("5. Nasi Perkedel - Rp10.000")

    nomor = int(input("\nMasukan Pilihan: ")) 
    porsi = int(input("Berapa Porsi: "))

    if nomor == 1:
        total1 = porsi * 15000
        print(porsi, " porsi Nasi Rendang = Rp", total1)
        jenis1 = ("Nasi Rendang")
    elif nomor == 2:
        total1 = porsi * 18000
        print(porsi, " porsi Nasi Ayam Goreng = Rp", total1)
        jenis1 = ("Nasi Ayam Goreng")
    elif nomor == 3:
        total1 = porsi * 12000
        print(porsi, " porsi Nasi Telur Dadar = Rp", total1)
        jenis1 = ("Nasi Telur Dadar")
    elif nomor == 4:
        total1 = porsi * 20000
        print(porsi, " porsi Nasi Ayam Gulai = Rp", total1)
        jenis1 = ("Nasi Ayam Gulai")
    elif nomor == 5:
        total1 = porsi * 10000
        print(porsi, " porsi Nasi Perkedel = Rp", total1)
        jenis1 = ("Nasi Perkedel")
    else:
        print("Pilihan tidak tersedia")

fungsimakanan()



def fungsiminuman():
    global total2
    global jenis2
    global gelas
    print("\nMenu Minuman")
    print("1. Teh Hangat - Rp 2.000")
    print("2. Es Teh Manis - Rp 3.000")
    print("3. Jeruk Hangat - Rp 3.500")
    print("4. Es Jeruk - Rp 4.000")
    nomor = int(input("\nMasukkan Pilihan: "))
    gelas = int(input("Berapa Gelas: "))

    if nomor == 1:
        total2 = gelas * 2000
        print(gelas, " Gelas Teh Hangat = Rp", total2)
        jenis2 = ("Teh Hangat")
    elif nomor == 2:
        total2 = gelas * 3000
        print(gelas, " Gelas Es Teh Manis = Rp", total2)
        jenis2 = ("Es Teh Manis")
    elif nomor == 3:
        total2 = gelas * 3500
        print(gelas, " Gelas Jeruk Hangat = Rp", total2)
        jenis2 = ("Jeruk Hangat")
    elif nomor == 4:
        total2 = gelas * 4000
        print(gelas, " Gelas Es Jeruk = Rp", total2)
        jenis2 = ("Es Jeruk")
    else:
        print("Pilihan tidak tersedia")

fungsiminuman()


totalsemua = total1 + total2

print("\nTotal harus Dibayar: Rp", totalsemua)
uang = int(input("Uang Tunai Pembeli: Rp."))
kembalian = int(uang - totalsemua)
print("Kembalian :", kembalian)

print("\n\n\n=============================================")
print("====== S T R U K   P E M B E L I I A N ======")
print("=========    RUMAH MAKAN PADANG   ===========")
print("=========        MINANG RAYA        =========")
print("========= Jl. Raya Pakuan - Bogor ===========")
print("=============================================")
print(" Nama         :", pembeli)
print(" Beli         :", porsi, jenis1, "-", total1)
print("               ", gelas, jenis2, "-", total2)
print(" Tagihan      : Rp.", totalsemua)
print(" Uang         : Rp.", uang)
print(" Kembalian    : Rp.", kembalian)
print("=============================================")
print("========== T E R I M A  K A S I H ===========")
print("=============================================\n\n\n")

