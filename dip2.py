import cv2
import numpy as np

# функции-обработчики ползунков
def update_ranges(pos):
    # Hmin = cv2.getTrackbarPos("Hmin", "window")
    # Hmax = cv2.getTrackbarPos("Hmax", "window")
    # Smin = cv2.getTrackbarPos("Smin", "window")
    # Smax = cv2.getTrackbarPos("Smax", "window")
    # Vmin = cv2.getTrackbarPos("Vmin", "window")
    # Vmax = cv2.getTrackbarPos("Vmax", "window")
    GridSize = cv2.getTrackbarPos("GridSize", "window")

    # Применяем CLAHE к каналам V, R, G, B
    clahe = cv2.createCLAHE(clipLimit=5.0, tileGridSize=(GridSize, GridSize))
    v_clahe = clahe.apply(v)
    r_clahe = clahe.apply(r)
    g_clahe = clahe.apply(g)
    b_clahe = clahe.apply(b)

    # Объединяем каналы
    # image = cv2.merge((h_range, s_range, v_clahe))
    # hsv = cv2.merge((h, s, v_clahe))
    # rgb = cv2.cvtColor(image, cv2.COLOR_HSV2BGR)

    # Объединяем изображения для вывода
    img_h = r.shape[0]
    img_w = r.shape[1]
    image = np.zeros((img_h, 4*img_w))
    image = np.concatenate((r_clahe, g_clahe, b_clahe, v_clahe), axis=1)

    # cv2.imshow("window", image)
    cv2.imshow("window", image)

# имя картинки задаётся первым параметром
filename = "4.jpeg"
# получаем картинку
image = cv2.imread(filename)
print("[i] image:", filename)

b, g, r = cv2.split(image)

# конвертируем в HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(image)

# создаем окно для отображения картинки и ползунков
cv2.namedWindow("window", cv2.WINDOW_NORMAL)

# определяем минимальное и максимальное значение у каналов HSV
Hmin, Hmax = np.min(h), np.max(h)
Smin, Smax = np.min(s), np.max(s)
Vmin, Vmax = np.min(v), np.max(v)
HSVmax = 256


# создаем трекбары для настройки параметров
# cv2.createTrackbar("Hmin", "window", Hmin, HSVmax, update_ranges)
# cv2.createTrackbar("Hmax", "window", Hmax, HSVmax, update_ranges)
# cv2.createTrackbar("Smin", "window", Smin, HSVmax, update_ranges)
# cv2.createTrackbar("Smax", "window", Smax, HSVmax, update_ranges)
# cv2.createTrackbar("Vmin", "window", 0, HSVmax, update_ranges)
# cv2.createTrackbar("Vmax", "window", 0, HSVmax, update_ranges)
cv2.createTrackbar("GridSize", "window", 2, 200, update_ranges)

# отображаем изображение и ждем нажатия клавиши
while True:
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # нажатие клавиши Esc для выхода
        break

cv2.destroyAllWindows()