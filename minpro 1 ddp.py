antrian = []
nomor_antrian = 1

while True:
    print("---- Menu antrean laundy lovely ----")
    print("1. Tambah Antrean")
    print("2. Tampilkan Antrean")
    print("3. Hapus Antrean")
    print("4. Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        nama = input("Masukkan nama: ")
    
        print("jenis layanan yang tersedia: ")
        print("1. Cuci Kering")
        print("2. Cuci + Setrika")  
        print("3. Express")

        layanan = (input("Pilih jenis layanan (1/2/3): "))

        if layanan == "1":
            jenis_layanan = "Cuci Kering"
            harga = 4000
            waktu = "1-2 hari"
            
        elif layanan == "2":
            jenis_layanan = "Cuci + Setrika"
            harga = 6000
            waktu = "2-3 hari"
            
        elif layanan == "3":
            jenis_layanan = "Express"
            harga = 10000
            waktu = "1 hari"

        else:
            print("Layanan tidak tersedia")
            continue            

        berat = float(input("Masukkan berat pakaian (kg): "))

        if berat <= 0:
            print("Berat pakaian harus lebih dari 0 kg!")
            continue

        estimasi_biaya = harga * berat
        data = (nomor_antrian, nama, jenis_layanan, berat, estimasi_biaya, waktu)
        antrian.append(data)

        print("=== Antrian berhasil ditambahkan ===")
        print("Nomor Antrian      : ", nomor_antrian)
        print("Nama Pelanggan     : ", nama)
        print("Jenis Layanan      : ", jenis_layanan)
        print("Berat Pakaian      : ", berat, "kg")
        print("Estimasi Biaya     :  Rp", int(estimasi_biaya))
        print("Estimasi Waktu     : ", waktu)
        print("=====================================")

        nomor_antrian += 1

    elif pilih == "2":
        if not antrian:
            print("Belum ada antrean laundry")

        else:
            print("---- Daftar Antrian Laundry Lovely ----")

            for data in antrian:
                print("Nomor Antrian      : ", data[0])
                print("Nama Pelanggan     : ", data[1])
                print("Jenis Layanan      : ", data[2])
                print("Berat Pakaian      : ", data[3], "kg")
                print("Estimasi Biaya     :  Rp", int(data[4]))
                print("Estimasi Waktu     : ", data[5])
                print("================================")

    elif pilih == "3":
        if not antrian:
            print("Belum ada antrean laundry")
        else:
            nomor = int(input("Masukkan nomor antrian: "))

            for data in antrian:
                if data[0] == nomor:
                    antrian.remove(data)
                    print("Antrian berhasil dihapus")
                    break

    elif pilih == "4":
        print("Terima kasih telah menggunakan layanan laundry lovely")
        break

    else:
        print("Pilihan menu tidak tersedia")