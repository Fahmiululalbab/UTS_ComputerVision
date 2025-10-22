import cv2
import numpy as np
import os

# Pastikan folder output ada
os.makedirs("output", exist_ok=True)

# Membuat kanvas kosong hitam (300x300 pixel)
canvas = np.zeros((300, 300, 3), dtype=np.uint8)

# ----------------- Membuat Karakter Orang Riau -----------------

# Kepala (wajah)
cv2.ellipse(canvas, (150, 90), (40, 50), 0, 0, 360, (210, 180, 140), -1)  # wajah

# Mata
cv2.circle(canvas, (135, 80), 6, (255, 255, 255), -1)
cv2.circle(canvas, (165, 80), 6, (255, 255, 255), -1)
cv2.circle(canvas, (135, 80), 3, (0, 0, 0), -1)
cv2.circle(canvas, (165, 80), 3, (0, 0, 0), -1)

# Alis
cv2.line(canvas, (125, 70), (145, 70), (0, 0, 0), 2)
cv2.line(canvas, (155, 70), (175, 70), (0, 0, 0), 2)

# Mulut
cv2.ellipse(canvas, (150, 110), (15, 7), 0, 0, 180, (0, 0, 0), 2)

# Songkok Melayu (peci)
cv2.rectangle(canvas, (110, 45), (190, 60), (0, 0, 0), -1)
cv2.ellipse(canvas, (150, 45), (40, 15), 0, 0, 180, (0, 0, 0), -1)

# Baju Melayu
cv2.rectangle(canvas, (115, 130), (185, 230), (0, 100, 200), -1)

# Kain samping
cv2.rectangle(canvas, (115, 200), (185, 230), (0, 180, 255), -1)

# Kancing baju
cv2.circle(canvas, (150, 150), 4, (255, 255, 0), -1)
cv2.circle(canvas, (150, 175), 4, (255, 0, 0), -1)
cv2.circle(canvas, (150, 200), 4, (0, 255, 0), -1)

# Tangan
cv2.line(canvas, (95, 150), (115, 180), (210, 180, 140), 6)
cv2.line(canvas, (185, 180), (205, 150), (210, 180, 140), 6)

# Kaki
cv2.line(canvas, (135, 230), (135, 270), (0, 100, 200), 6)
cv2.line(canvas, (165, 230), (165, 270), (0, 100, 200), 6)

# Simpan karakter asli
cv2.imwrite("output/karakter.png", canvas)


# ----------------- Transformasi -----------------

# Translasi
M_translate = np.float32([[1, 0, 30], [0, 1, 20]])
translated = cv2.warpAffine(canvas, M_translate, (300, 300))

# Rotasi
M_rotate = cv2.getRotationMatrix2D((150, 150), 25, 1)
rotated = cv2.warpAffine(canvas, M_rotate, (300, 300))
cv2.imwrite("output/rotate.png", rotated)

# Resize (ubah ukuran jadi 150x150)
resized = cv2.resize(canvas, (150, 150))

# Crop (potong bagian tengah)
crop = canvas[60:220, 90:210]
cv2.imwrite("output/crop.png", crop)


# ----------------- Bitwise -----------------

# Background default
bg = np.full((300, 300, 3), (80, 80, 80), dtype=np.uint8)

# bitwise_and
bitwise = cv2.bitwise_and(canvas, bg)
cv2.imwrite("output/bitwise.png", bitwise)

# bitwise_or
final = cv2.bitwise_or(rotated, bg)
cv2.imwrite("output/final.png", final)


# ----------------- Tempel ke Background -----------------

gray = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)
_, mask = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

bg_part = cv2.bitwise_and(bg, bg, mask=mask_inv)
fg_part = cv2.bitwise_and(canvas, canvas, mask=mask)
combined = cv2.add(bg_part, fg_part)
cv2.imwrite("output/final.png", combined)


# ----------------- Tampilkan Hasil -----------------
cv2.imshow("Karakter - Orang Riau", canvas)
cv2.imshow("Rotate", rotated)
cv2.imshow("Crop", crop)
cv2.imshow("Bitwise", bitwise)
cv2.imshow("Final", combined)

cv2.waitKey(0)
cv2.destroyAllWindows()
