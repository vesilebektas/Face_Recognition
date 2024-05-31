import cv2
import face_recognition
import serial
import time

# Arduino ile iletişim kurmak için seri portu ayarla
ser = serial.Serial('COM3', 9600, timeout=1)
time.sleep(2)  # Arduino'nun başlaması


def yuz_karsilastir(image1):
    image1_yuz = face_recognition.load_image_file(image1)

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        image2_yuz = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        try:
            image1_embedding = face_recognition.face_encodings(image1_yuz)[0]
            face_locations = face_recognition.face_locations(image2_yuz)

            if face_locations:
                top, right, bottom, left = face_locations[0]
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

                image2_embedding = face_recognition.face_encodings(image2_yuz)[0]

                # Yüz görsellerini karşılaştırma yap
                result = face_recognition.compare_faces([image1_embedding], image2_embedding)

                if result[0]:
                    print("Yüzler aynı kişiye ait.")
                    ser.write(b'1')  # Arduino'ya 1 gönder (yeşil ışık)
                else:
                    print("Yüzler farklı kişilere ait.")
                    ser.write(b'0')  # Arduino'ya 0 gönder (kırmızı ışık)

            else:
                print("Yüz bulunamadı.")
                ser.write(b'0')  # Arduino'ya 0 gönder (kırmızı ışık)

        except IndexError:
            print("Yüz bulunamadı.")
            ser.write(b'0')  # Arduino'ya 0 gönder (kırmızı ışık)

        cv2.imshow('Face Comparison', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    ser.write(b'2')  # Arduino'ya 2 gönder (bütün ışıkları söndür)


# İki yüz görselini karşılaştır
image1_path = r"C:\Users\bekta\PycharmProjects\tezProject\ves1.jpeg"
yuz_karsilastir(image1_path)
