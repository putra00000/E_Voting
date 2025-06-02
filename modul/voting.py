class VotingManager:
    def __init__(self, pemilih_manager, calon_manager):
        self.pm = pemilih_manager
        self.cm = calon_manager

    def voting(self, id_pemilih, id_calon):
        if not self.pm.validasi_pemilih(id_pemilih):
            raise ValueError(f"ID Pemilih '{id_pemilih}' tidak valid.")
        if self.pm.sudah_memilih(id_pemilih):
            raise ValueError(f"Pemilih dengan ID '{id_pemilih}' sudah memilih.")
        if not self.cm.validasi_calon(id_calon):
            raise ValueError(f"ID Calon '{id_calon}' tidak valid.")

        self.pm.set_sudah_memilih(id_pemilih)
        self.cm.tambah_suara(id_calon)
        print(f"Pemilih dengan ID '{id_pemilih}' berhasil memilih Calon '{id_calon}'.")
