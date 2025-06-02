from modules.pemilih import PemilihManager
from modules.calon import CalonManager
from modules.voting import VotingManager
from modules.statistik import StatistikManager

def menu():
    pm = PemilihManager()
    cm = CalonManager()
    vm = VotingManager(pm, cm)
    sm = StatistikManager(pm, cm)

    while True:
        print("\n=== Sistem Simulasi E-Voting ===")
        print("1. Tambah Pemilih")
        print("2. Tambah Calon Ketua")
        print("3. Voting")
        print("4. Tampilkan Hasil Sementara")
        print("5. Tampilkan Statistik Pemilu")
        print("6. Keluar")

        pilihan = input("Pilih menu (1-6): ").strip()
        if pilihan == '1':
            try:
                id = input("Masukkan ID Pemilih: ").strip()
                nama = input("Masukkan Nama Pemilih: ").strip()
                jurusan = input("Masukkan Jurusan Pemilih: ").strip()
                pm.tambah_pemilih(id, nama, jurusan)
                print("Pemilih berhasil ditambahkan.")
            except ValueError as e:
                print("Error:", e)

        elif pilihan == '2':
            try:
                id = input("Masukkan ID Calon: ").strip()
                nama = input("Masukkan Nama Calon: ").strip()
                visi = input("Masukkan Visi Misi Calon: ").strip()
                cm.tambah_calon(id, nama, visi)
                print("Calon ketua berhasil ditambahkan.")
            except ValueError as e:
                print("Error:", e)

        elif pilihan == '3':
            try:
                id_pemilih = input("Masukkan ID Pemilih: ").strip()
                id_calon = input("Masukkan ID Calon Pilihan: ").strip()
                vm.voting(id_pemilih, id_calon)
            except ValueError as e:
                print("Error:", e)

        elif pilihan == '4':
            cm.tampilkan_semua()

        elif pilihan == '5':
            sm.tampilkan_statistik()

        elif pilihan == '6':
            print("Terima kasih telah menggunakan sistem ini.")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")

if __name__ == "__main__":
    menu()
