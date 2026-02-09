import time
import random

def cetak_dramatis(teks):
    """Fungsi untuk mencetak teks dengan jeda 0.05 detik per karakter"""
    for karakter in teks:
        print(karakter, end='', flush=True)
        time.sleep(0.05)
    print()

def pedang_menang():
    """ASCII Art pedang untuk kemenangan"""
    print("""
    ⚔️  KEMENANGAN! ⚔️
    
        /\_/\\
       ( o.o )
        > ^ <
       /|   |\\
        |   |
    """)

def tengkorak_kalah():
    """ASCII Art tengkorak untuk kekalahan"""
    print("""
    ☠️  GAME OVER! ☠️
    
      _____
     /     \\
    | () () |
    |   >   |
    |  \\_/  |
     \\_____/
    """)


def game_utama():
    bermain = True
    
    while bermain:
        print("\n--- MEMULAI PETUALANGAN DIGITAL ---\n")
        
        nama = input("Siapa namamu? ")
        nyawa = 100
        
        cetak_dramatis("\nSelamat datang, " + nama + "!")
        time.sleep(0.5)
        
        cetak_dramatis("Kamu terjebak di dimensi digital yang penuh misteri...")
        time.sleep(0.5)
        
        cetak_dramatis("Sebelum melanjutkan, pilih senjatamu!")
        cetak_dramatis("1. Pedang - Cocok untuk pertarungan jarak dekat")
        cetak_dramatis("2. Panah - Cocok untuk serangan jarak jauh")
        time.sleep(0.5)
        
        senjata = input("\nPilihan senjata mu (Pedang / Panah)? ").lower()
        
        if senjata not in ["pedang", "panah"]:
            cetak_dramatis("\nSenjata tidak valid! Kamu tersesat...")
            nyawa -= 20
            cetak_dramatis(f"Nyawa berkurang 20 poin!\n[Nyawa saat ini: {nyawa}]")
            time.sleep(0.5)
            if nyawa <= 0:
                cetak_dramatis("Kamu tidak selamat!")
                tengkorak_kalah()
            continue
        
        cetak_dramatis(f"\nKamu memilih senjata: {senjata.upper()}")
        time.sleep(0.5)
        
        cetak_dramatis("\nAda tiga jalan di depanmu:")
        cetak_dramatis("1. Lembah Coding - Tempat yang penuh dengan syntax error")
        cetak_dramatis("2. Gunung Bug - Puncak tertinggi di dunia debugging")
        cetak_dramatis("3. Gua Bom - Gua misterius penuh dengan perangkap ledakan")
        time.sleep(0.5)
        
        cetak_dramatis(f"\n[Nyawa: {nyawa}]")
        
        pilihan = input("\nPilihan mu (Lembah Coding / Gunung Bug / Gua Bom)? ").lower()
        
        if pilihan == "lembah coding":
            cetak_dramatis("\nKamu memilih Lembah Coding...")
            time.sleep(0.5)
            cetak_dramatis("Kamu memasuki lembah yang penuh dengan error-error digital...")
            cetak_dramatis("Di depanmu ada dua jalan: ke kanan dan ke kiri")
            cetak_dramatis("Kanan terlihat cerah dan penuh harapan...")
            cetak_dramatis("Kiri terlihat gelap dan berbahaya...")
            time.sleep(0.5)
            
            arah = input("\nPilihan arah mu (Kanan / Kiri)? ").lower()
            
            if arah == "kanan":
                cetak_dramatis("\nKamu memilih jalan ke KANAN...")
                time.sleep(0.5)
                cetak_dramatis("Cahaya terang membimbingmu melalui lembah!")
                time.sleep(0.5)
                cetak_dramatis("Error-error digital mulai menghilang saat kamu berjalan...")
                cetak_dramatis("Langit bersinar cerah, dimensi digital mulai pulih!")
                cetak_dramatis("Kamu menemukan jalan keluar dengan selamat!")
                cetak_dramatis(f"Selamat datang kembali, {nama}! Dimensi digital selamat!")
                time.sleep(0.5)
                pedang_menang()
                cetak_dramatis(f"Akhir permainan dengan nyawa: {nyawa}")
                
            elif arah == "kiri":
                cetak_dramatis("\nKamu memilih jalan ke KIRI...")
                time.sleep(0.5)
                cetak_dramatis("Gelap menyelimuti sekitarmu...")
                cetak_dramatis("Tiba-tiba, error-error digital menyerangmu dari segala arah!")
                cetak_dramatis("Error besar demi besar menghujani tubuhmu tanpa henti!")
                nyawa -= 70
                cetak_dramatis(f"Kamu terluka sangat parah! Nyawa berkurang 70 poin!")
                cetak_dramatis(f"[Nyawa saat ini: {nyawa}]")
                time.sleep(0.5)
                
                if nyawa <= 0:
                    cetak_dramatis("Error terakhir melumpuhkanmu sepenuhnya...")
                    cetak_dramatis("Kamu kolaps dan tidak sanggup melanjutkan perjalanan...")
                    time.sleep(0.5)
                    tengkorak_kalah()
                else:
                    cetak_dramatis(f"Meski hampir tewas, {nama} berhasil merangkak keluar dari kegelapan!")
                    cetak_dramatis("Kamu berhasil escape dengan sisa nyawa yang sedikit!")
                    time.sleep(0.5)
                    pedang_menang()
                    cetak_dramatis(f"Akhir permainan dengan nyawa: {nyawa}")
            else:
                cetak_dramatis("\nPilihan arah tidak valid! Kamu tersesat...")
                nyawa -= 40
                cetak_dramatis(f"Nyawa berkurang 40 poin!")
                cetak_dramatis(f"[Nyawa saat ini: {nyawa}]")
                time.sleep(0.5)
                if nyawa <= 0:
                    cetak_dramatis("Kamu tidak sanggup bertahan lagi...")
                    tengkorak_kalah()
                else:
                    cetak_dramatis("Akhirnya kamu menemukan jalan keluar dari kebingungan!")
                    time.sleep(0.5)
                    pedang_menang()
                    cetak_dramatis(f"Akhir permainan dengan nyawa: {nyawa}")
            
        elif pilihan == "gunung bug":
            cetak_dramatis("\nKamu memilih Gunung Bug...")
            time.sleep(0.5)
            cetak_dramatis("Kamu mulai mendaki. Udara semakin dingin dan gelap...")
            time.sleep(0.5)
            cetak_dramatis("Tiba-tiba, sebuah sphinx digital muncul menghadangmu!")
            cetak_dramatis("Sphinx: Menjawab tebakan ini atau kamu tidak bisa melanjutkan!")
            time.sleep(0.5)
            
            cetak_dramatis("Apa itu BUG dalam dunia programming?")
            cetak_dramatis("A. Serangga asli")
            cetak_dramatis("B. Kesalahan dalam kode programming")
            cetak_dramatis("C. Nama monster")
            time.sleep(0.5)
            
            jawaban_bug = input("\nJawaban mu (A / B / C)? ").upper()
            
            if jawaban_bug != "B":
                cetak_dramatis("\nSphinx: JAWABAN SALAH!!!")
                time.sleep(0.5)
                cetak_dramatis("Sphinx menggunakan kekuatan magic untuk memanggilmu ke dalam batu!")
                cetak_dramatis("Kamu terjebak dalam dimensi lain dan tidak bisa escape!")
                time.sleep(0.5)
                tengkorak_kalah()
            else:
                cetak_dramatis("\nSphinx: JAWABAN BENAR! Kamu boleh melanjutkan...")
                cetak_dramatis("Sphinx menghilang dalam cahaya terang.")
                time.sleep(0.5)
            
            # Cek kecocokan senjata dengan lokasi
            if senjata == "panah":
                cetak_dramatis("Tiba-tiba, monster bug raksasa muncul!!!")
                time.sleep(0.5)
                cetak_dramatis("Kamu mengeluarkan panah, tapi Panah tidak cukup efektif!")
                cetak_dramatis("Monster itu bergerak terlalu cepat, panahmu meleset!")
                cetak_dramatis("Monster yang marah menyerangmu dengan penuh kekuatan!")
                nyawa -= 50
                cetak_dramatis(f"Kamu terpukul dan terluka parah! Nyawa berkurang 50 poin!")
                cetak_dramatis(f"[Nyawa saat ini: {nyawa}]")
                time.sleep(0.5)
                
                if nyawa <= 0:
                    cetak_dramatis("Monster bug melayangkan pukulan final ke tubuhmu...")
                    cetak_dramatis("Kamu kolaps dan tidak bisa bangkit lagi!")
                    time.sleep(0.5)
                    tengkorak_kalah()
                else:
                    cetak_dramatis(f"Meski terluka parah, {nama} masih sanggup escape!")
                    cetak_dramatis("Kamu berlari menuruni gunung dengan semua kekuatan yang tersisa...")
                    time.sleep(0.5)
                    pedang_menang()
                    cetak_dramatis(f"Akhir permainan dengan nyawa: {nyawa}")
            else:  # senjata == "pedang"
                cetak_dramatis("Tiba-tiba, monster bug raksasa muncul!!!")
                time.sleep(0.5)
                cetak_dramatis("Pedang adalah pilihan yang tepat! Pertarungan epik dimulai...")
                time.sleep(0.5)
                cetak_dramatis("Dengan gerakan presisi, kamu menyerang monster itu!")
                cetak_dramatis("SHING! SHING! Pedang mu menembus tubuh monster bug!")
                cetak_dramatis(f"Selamat! {nama} berhasil menyelamatkan dimensi digital!")
                time.sleep(0.5)
                pedang_menang()
                cetak_dramatis(f"Akhir permainan dengan nyawa: {nyawa}")
                
        elif pilihan == "gua bom":
            cetak_dramatis("\nKamu memilih Gua Bom...")
            time.sleep(0.5)
            cetak_dramatis("Kamu memasuki gua gelap yang penuh misteri...")
            time.sleep(0.5)
            cetak_dramatis("Tiba-tiba, seorang penjaga gua digital muncul!")
            cetak_dramatis("Penjaga: Jika ingin lewat, jawab tebakan ini!")
            time.sleep(0.5)
            
            cetak_dramatis("Berapa banyak digit biner yang digunakan dalam sistem komputer?")
            cetak_dramatis("A. 2 digit (0 dan 1)")
            cetak_dramatis("B. 10 digit (0-9)")
            cetak_dramatis("C. 16 digit")
            time.sleep(0.5)
            
            jawaban_bom = input("\nJawaban mu (A / B / C)? ").upper()
            
            if jawaban_bom != "A":
                cetak_dramatis("\nPenjaga: SALAH! Ini hukumanmu!")
                time.sleep(0.5)
                cetak_dramatis("Penjaga mengaktifkan semua bom di gua sekaligus!")
                cetak_dramatis("LEDAKAN DAHSYAT MELEDAK DI SEKITARMU!!!")
                cetak_dramatis("Tidak ada jalan untuk escape!")
                time.sleep(0.5)
                tengkorak_kalah()
            else:
                cetak_dramatis("\nPenjaga: BENAR! Kamu bijak. Silakan lewat...")
                cetak_dramatis("Penjaga membukakan jalan yang aman untuk mu.")
                time.sleep(0.5)
            
            # Cek kecocokan senjata dengan lokasi
            if senjata == "panah":
                cetak_dramatis("Kamu mencoba menggunakan panah untuk mengatasi ledakan!")
                cetak_dramatis("Tapi panah tidak bisa menangkal ledakan yang begitu besar!")
                cetak_dramatis("Bom-bom digital meledak dengan kekuatan penuh ke tubuhmu!")
                nyawa -= 80  # Damage yang lebih besar karena senjata tidak cocok
                cetak_dramatis(f"Ledakan menghancurkan tubuhmu! Nyawa berkurang 80 poin!")
                cetak_dramatis(f"[Nyawa saat ini: {nyawa}]")
                time.sleep(0.5)
                
                if nyawa <= 0:
                    cetak_dramatis("Ledakan final mengenai langsung ke tubuhmu...")
                    cetak_dramatis("Kamu tidak sanggup bertahan...")
                    time.sleep(0.5)
                    tengkorak_kalah()
                else:
                    cetak_dramatis(f"Meski hampir terbakar habis, {nama} berhasil escape!")
                    cetak_dramatis("Dengan sisa nyawa yang sangat tipis, kamu meninggalkan gua...")
                    time.sleep(0.5)
                    pedang_menang()
                    cetak_dramatis(f"Akhir permainan dengan nyawa: {nyawa}")
            else:  # senjata == "pedang"
                cetak_dramatis("Pedang adalah pilihan yang tepat untuk menghadapi ini!")
                cetak_dramatis("Kamu menggunakan pedang untuk meredam dampak ledakan!")
                cetak_dramatis("Dengan teknik pertahanan khusus, kamu menahan energi ledakan!")
                nyawa = nyawa // 2  # Tetap kehilangan setengah tapi selamat
                cetak_dramatis(f"Kamu terluka tapi berhasil survive! Nyawa hilang setengah.")
                cetak_dramatis(f"[Nyawa saat ini: {nyawa}]")
                time.sleep(0.5)
                
                if nyawa > 0:
                    cetak_dramatis(f"Dengan gigih, {nama} berhasil keluar dari gua itu!")
                    cetak_dramatis("Meski penuh luka, kamu telah selamat dari malapetaka!")
                    time.sleep(0.5)
                    pedang_menang()
                    cetak_dramatis(f"Akhir permainan dengan nyawa: {nyawa}")
                else:
                    cetak_dramatis("Energi ledakan masih terlalu kuat untukmu...")
                    cetak_dramatis("Kamu kolaps dan tidak sanggup lagi...")
                    time.sleep(0.5)
                    tengkorak_kalah()
            
        else:
            cetak_dramatis("\nPilihan tidak valid! Kamu tersesat di dimensi gelap...")
            time.sleep(0.5)
            nyawa -= 20
            cetak_dramatis(f"Nyawa berkurang 20 poin!")
            cetak_dramatis(f"[Nyawa saat ini: {nyawa}]")
            time.sleep(0.5)
            
            if nyawa <= 0:
                cetak_dramatis("Kegelapan menelan dirimu...")
                time.sleep(0.5)
                tengkorak_kalah()
            else:
                cetak_dramatis("Kamu berhasil mencari jalan keluar dari kegelapan!")
                time.sleep(0.5)
                pedang_menang()
        
        # Tanyakan apakah mau main lagi
        time.sleep(1)
        ulang = input("\n=== Mau main lagi? (ya/tidak) === ").lower()
        
        if ulang != "ya":
            cetak_dramatis("\nTerima kasih telah bermain Mystery Adventure Bot!")
            cetak_dramatis("Sampai jumpa lagi di dimensi digital!")
            bermain = False


    
if __name__ == "__main__":
    game_utama()