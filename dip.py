import cv2
import numpy as np

# функции-обработчики ползунков
def update_ranges(pos):
    Hmin = cv2.getTrackbarPos("Hmin", "window")
    Hmax = cv2.getTrackbarPos("Hmax", "window")
    Smin = cv2.getTrackbarPos("Smin", "window")
    Smax = cv2.getTrackbarPos("Smax", "window")
    Vmin = cv2.getTrackbarPos("Vmin", "window")
    Vmax = cv2.getTrackbarPos("Vmax", "window")
    GridSize = cv2.getTrackbarPos("GridSize", "window")

    cv2.inRange(h_plane, Hmin, Hmax, h_range)
    cv2.inRange(s_plane, Smin, Smax, s_range)

    # Применяем CLAHE только к V-каналу
    clahe = cv2.createCLAHE(clipLimit=4.0, tileGridSize=(GridSize, GridSize))
    v_clahe = clahe.apply(v_plane)

    # Объединяем каналы
    image = cv2.merge((h_range, s_range, v_clahe))
    cv2.imshow("window", image)

# имя картинки задаётся первым параметром
filename = "1.jpeg"
# получаем картинку
image = cv2.imread(filename)
print("[i] image:", filename)

# создаем окно для отображения картинки и ползунков
cv2.namedWindow("window", cv2.WINDOW_NORMAL)

# конвертируем в HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
h_plane, s_plane, v_plane = cv2.split(hsv)

# определяем минимальное и максимальное значение у каналов HSV
Hmin, Hmax = np.min(h_plane), np.max(h_plane)
Smin, Smax = np.min(s_plane), np.max(s_plane)
Vmin, Vmax = np.min(v_plane), np.max(v_plane)
HSVmax = 256

# создаем изображения для хранения каналов HSV после преобразования
h_range = np.zeros_like(h_plane)
s_range = np.zeros_like(s_plane)
v_range = np.zeros_like(v_plane)

# создаем трекбары для настройки параметров
cv2.createTrackbar("Hmin", "window", Hmin, HSVmax, update_ranges)
cv2.createTrackbar("Hmax", "window", Hmax, HSVmax, update_ranges)
cv2.createTrackbar("Smin", "window", Smin, HSVmax, update_ranges)
cv2.createTrackbar("Smax", "window", Smax, HSVmax, update_ranges)
cv2.createTrackbar("Vmin", "window", 0, HSVmax, update_ranges)
cv2.createTrackbar("Vmax", "window", 0, HSVmax, update_ranges)
cv2.createTrackbar("GridSize", "window", 1, 200, update_ranges)

# отображаем изображение и ждем нажатия клавиши
while True:
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # нажатие клавиши Esc для выхода
        break

cv2.destroyAllWindows()