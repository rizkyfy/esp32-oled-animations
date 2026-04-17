# ESP32 OLED Video Player (Micro Flipbook)

![C++](https://img.shields.io/badge/C%2B%2B-Arduino-00599C?style=for-the-badge&logo=c%2B%2B&logoColor=white)
![Python](https://img.shields.io/badge/Python-OpenCV-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Hardware](https://img.shields.io/badge/Hardware-ESP32--C3_Super_Mini-orange?style=for-the-badge)

> **Sistem Konversi Video Otomatis & Pemutar Animasi Monokrom High-FPS untuk Layar OLED I2C berbasis Mikrokontroler.**

---

## Tentang Project
Project ini menyulap mikrokontroler mungil (ESP32-C3 Super Mini) dan layar OLED 0.96 inch menjadi gantungan resleting tas digital yang bisa memutar video animasi (seperti lirik lagu *Radiohead - Let Down*). Karena mikrokontroler tidak bisa memutar file `.mp4` secara langsung, project ini menggunakan *pipeline* konversi di komputer (Python) untuk mengubah video menjadi barisan kode *Hexadecimal* (Byte Array), lalu menyimpannya di memori Flash ESP32 untuk diputar bagaikan buku *flipbook* digital yang sangat cepat.

### Fitur Utama

* **Automated Video-to-Hex Parsing:** Script Python otomatis mengekstrak *frame* dari video `.mp4`, mengubahnya menjadi gambar monokrom 1-bit, dan menyusunnya menjadi kode C++ (`frames.h`).
* **Smart Aspect Ratio (Anti-Gepeng):** Dilengkapi algoritma *Zoom & Crop* (Full Screen) atau *Pillarboxing* agar video dari format apapun (misal 1:1 Instagram) tetap proporsional di layar 128x64.
* **Overclocked I2C Playback:** Konfigurasi khusus di Arduino IDE (`Wire.setClock(400000)`) untuk menembus batas standar I2C, memungkinkan pemutaran video hingga **30 FPS** dengan lancar tanpa *glitch*.
* **Deep Sleep & Ultra-Portable Ready:** Desain kodingan disiapkan untuk penggunaan baterai LiPo 3.7V ukuran mini (cocok untuk modifikasi *gantungan kunci/resleting*).

---

## Tools & Hardware

Project ini menggunakan kombinasi *software* dan *hardware* berikut:

* **Microcontroller:** ESP32-C3 Super Mini (Dipilih karena ukurannya yang seujung jempol dan memori Flash 4MB yang lega).
* **Display:** OLED 0.96" SSD1306 (I2C) - Warna Putih.
* **Power:** Baterai LiPo 3.7V (Kapasitas ~150mAh) + Modul TP4056 Micro-USB.
* **Software Converter:** [Python](https://www.python.org/) dengan *library* OpenCV (`cv2`) & Numpy.
* **IDE:** Arduino IDE (dengan library `Adafruit_GFX` & `Adafruit_SSD1306`).

---

## Prasyarat (Prerequisites)

Sebelum menjalankan sistem ini, pastikan Anda memiliki:

1.  **Python 3.x** terinstall di komputer untuk menjalankan script *converter*.
2.  Library Python: Buka terminal/CMD dan ketik `pip install opencv-python numpy`.
3.  **Arduino IDE** dengan *board manager* ESP32 yang sudah terinstall.
4.  Video *source* dalam format `.mp4` (disarankan durasi maksimal 30-60 detik agar muat di memori ESP32).

---

## Cara Penggunaan (How to Run)

Ikuti langkah-langkah berikut:

### Langkah 1: Extract Video ke Kode C++ (Python)
Siapkan video Anda (misal: `video_30detik.mp4`) dan taruh di folder yang sama dengan file `convert.py`. Buka `convert.py` dan sesuaikan nama videonya:

```python
video_path = 'video_30detik.mp4' # Ganti dengan nama file videomu
fps_target = 30 # Target kecepatan frame
