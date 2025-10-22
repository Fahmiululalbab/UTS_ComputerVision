Nama dan NIM  
FAHMI ULUL ALBAB – 43050230014  

Penjelasan singkat karakter yang dibuat  
Karakter yang dibuat adalah tokoh “Orang Riau” dengan ciri khas pakaian adat Melayu Riau.  
Karakter terdiri dari wajah manusia, songkok (peci Melayu), baju Melayu, kain samping,  
serta tambahan ornamen seperti kancing baju berwarna. Karakter digambar menggunakan bentuk  
bentuk dasar seperti ellipse, rectangle, circle, line dan polygon dari library OpenCV.

Transformasi dan operasi yang digunakan  
1. Translasi  
   - Menggeser posisi gambar menggunakan matrix transformasi warpAffine.
2. Rotasi  
   - Memutar karakter dengan sudut 25 derajat menggunakan getRotationMatrix2D.
3. Resize  
   - Mengubah ukuran gambar menjadi 150x150 piksel.
4. Crop  
   - Memotong bagian tengah karakter untuk menampilkan sebagian objek.
5. Bitwise AND  
   - Menggabungkan karakter dengan background menggunakan operasi bitwise AND.
6. Bitwise OR  
   - Menggabungkan hasil rotasi karakter dengan background menggunakan operasi OR.
7. Masking dan Overlay  
   - Menghapus background hitam dan menempelkan karakter ke background lain.

Hasil output yang disimpan  
- karakter.png  
- rotate.png  
- crop.png  
- bitwise.png  
- final.png

