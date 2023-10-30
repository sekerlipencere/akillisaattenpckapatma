import requests
import webbrowser
import time
import subprocess
import pyautogui

url = "Sizinsite.com/metin.txt"
check_interval = 15  # Kontrol aralığı (saniye)

while True:
    try:
        response = requests.get(url)
        if response.status_code == 200:
            content = response.text
            if "kapat" in content.lower():
                print("Metin dosyası kapatıldı. Bilgisayar kapatılıyor.")
                # Bilgisayarı kapatmak için aşağıdaki komutu kullanın.
                subprocess.call(["shutdown", "/s", "/t", "0"])
                break  # Döngüyü sonlandır
            elif "güncel" in content.lower():
                print("Metin dosyası güncel. Web sayfası açılıyor.")
                # Web sayfasını açmak için aşağıdaki komutu kullanın.
                webbrowser.open("http://hufryurfhuh.rf.gd/")
                time.sleep(5)  # Sayfanın yüklenmesini beklemek için birkaç saniye bekle
                pyautogui.press('f11')  # F11 tuşuna bas
                break  # Döngüyü sonlandır
        else:
            print("URL'ye erişilemiyor.")
    except Exception as e:
        print("Bir hata oluştu:", str(e))

    time.sleep(check_interval)
