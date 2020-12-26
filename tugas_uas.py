#program kasir RICKY ATK STORE
"""FITUR: 1. TOTAL BAYAR (JUMLAH TAGIHAN)
          2. JENIS KAMAR YANG DIPESAN
          3. JUMLAH MENGINAP YANG DIPESAN
          4. KEMBALIAN
          5. MENU
          6. CETAK STRUK    """
print("\n")
print("\n")
print("\n")
print("-----------------------------------------------------------------")
print("                                                                 ")
print("~~~~~~Kasir Lobi Manejemen Hotel Grand Suite KK(KANAN KIRI)~~~~~~")
print("                                                                 ")
print("-----------------------------------------------------------------")
print("\n")

pemesan = input("MASUKKAN NAMA PEMESAN: ")
print("NAMA PEMBELI : ", pemesan)
total1=0
jenis1=""
menginap=0
gelas=0

#membuat fungsi kamar dengan kata kunci def kemudian dengan nama fungsinya 
def kamar():

#membuat variabel global: variabel global adalah variabel yang bisa diakses dari semua 
#fungsi dari fungsi ~kamar
    global total1 
    global menginap
    global jenis1
    print ("\n~~~~PILIH KAMAR~~~~")
    print ("1. Standar Room(STD)      /Malam  - Rp300000")
    print ("2. Superior Room(SUP)     /Malam  - Rp387000")
    print ("3. Delux Room(DLX)        /Malam  - Rp420000")
    print ("4. Junior Suit Room(JRST) /Malam  - Rp490000")
    print ("5. Suit Room(STE)         /Malam  - Rp550000")
    print ("6. Presidential Suit(VVIP)/Malam  - Rp720000")
    nomor = int(input("MASUKKAN PILIHAN KAMAR: "))
    menginap = int(input("JUMLAH Menginap: "))

    if nomor==1:
        total1=menginap*300000
        print (menginap," MALAM KAMAR STD Rp.", total1)
        jenis1=("Standar Room(STD)")
    elif nomor==2:
        total1=menginap*387000
        print (menginap," MALAM KAMAR SUP Rp.", total1)
        jenis1=("Superior Room(SUP)")
    elif nomor==3:
        total1=menginap*420000
        print (menginap," MALAM KAMAR DLX Rp.", total1)
        jenis1=("Delux Room(DLX) ")
    elif nomor==4:
        total1=menginap*490000
        print (menginap," MALAM KAMAR JRST Rp.", total1)
        jenis1=("Junior Suit Room(JRST) ")
    elif nomor==5:
        total1=menginap*550000
        print (menginap," MALAM KAMAR STE Rp.", total1)
        jenis1=("Suit Room(STE)")
    elif nomor==6:
        total1=menginap*720000
        print (menginap," MALAM KAMAR VVIP Rp.", total1)
        jenis1=("Presidential Suit(VVIP)")
    else:
        print("Pilihan Kamar Tidak Ditemukan!")
        kamar()
    
kamar()

total2=0
jenis2=""

def fungsiminuman():
    global total2
    global jenis2
    global gelas
    print("\n~~~~BreakFast~~~~")
    print("\n****Menu Coffee****")
    print("1. COFFEE MILK WITH BROWN SUGAR     - Rp10000")
    print("2. COFFEE MILK WITH MACCHA          - Rp13000")
    print("3. COFFE MUR SPESIAL                - Rp20000")
    print("4. COFFEE ESSPRESO GAYO             - Rp15000")
    print("5. TIDAK MEMESAN COFFEE             - Rp 0")
    nomor=int(input("MASUKKAN PILIHAN MINUMAN: "))
    gelas= int(input("Berapa Gelas: "))

    if nomor==1:
        total2=gelas*10000
        print(gelas," COFFE MILK WITH BROWN SUGAR Rp.", total2)
        jenis2=("COFFEE MILK WITH BROWN SUGAR")
    elif nomor==2:
        total2=gelas*13000
        print(gelas," COFFEE MILK WITH MACCHA Rp.", total2)
        jenis2=("COFFEE MILK WITH MACCHA")
    elif nomor==3:
        total2=gelas*20000
        print(gelas," COFFE MUR SPESIAL Rp.", total2)
        jenis2=("COFFE MUR SPESIAL")
    elif nomor==4:
        total2=gelas*15000
        print(gelas," COFFEE ESSPRESO GAYO Rp.", total2)
        jenis2=("COFFEE ESSPRESO GAYO")
    elif nomor==5:
        total2=gelas*0
        print(gelas," TIDAK MEMESAN COFFEE Rp.", total2)
        jenis2=("TIDAK MEMESAN COFFEE")
    else:
        print("Pilihan menu tidak ada!!")
        fungsiminuman()
    
fungsiminuman()

totalsemua=0
totalsemua=total1+total2
print("\nTotal harus Dibayar: Rp.", totalsemua)
uang=int(input("Uang Tunai Pembeli: Rp."))
kembalian=int(uang-totalsemua)
print("Kembalian : ",kembalian)
print("\n")
print("------------------------------------------------")
print("                                                ")
print("^^^^^^^^^^^^^^^^^^ STRUK BOOKING ^^^^^^^^^^^^^^^")
print("                                  ")
print("Nama: ",pemesan)
print("Booking: ",menginap,jenis1,"-",total1)
print("  ",gelas,jenis2,"-",total2)
print("Tagihan:Rp. ",totalsemua)
print("Uang:Rp. ",uang)
print("Kembalian:Rp. ",kembalian)
print("~~~~~~ THANKYOU ",pemesan, "FOR YOUR ORDER ~~~~~")
print("                                                ")
print("------------------------------------------------")


