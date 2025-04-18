import datetime  # Импортируем библиотеку для работы со временем
import pygame   # Импортируем библиотеку для работы с окном

def set_time(): # Создаём новую функцию, для установки времени и учёта предпочтений пользователя
    sounds = {1: 'FileMP3/alarm-clock-1', 2: 'FileMP3/The-Soviet-Union-2'}
    try:
        print("\n Загрузка..." * 10)  # 10 раз пишем слово "Загрузка...", чтобы не было видно сообщение от PyGame
        time = input("Введите время для будильника в формате ЧЧ:ММ:")
        message = input("Введите сообщение, которое нужно отправить при срабатывании будильника. Если сообщение отсутствует, укажите 0")
        print("Сообщение,которое будет отправлено:",message)
        number = int(input(f"Введите номер звука {sounds}"))
        time_list = [int(x) for x in time.split(":")]  # Создаём новый список, переводим все элементы из str в int
        user_time = datetime.time(*time_list).strftime("%H:%M") # Уходим из списка, разделяем значения по часы:минуты. В конце обрезаем секунды

        while True:
            if str(user_time) == str(datetime.datetime.now().strftime("%H:%M")):
                if int(message) == 0:
                    print("Будильник сработал")
                    break
    except ValueError:
        print(message)
    except:
        print("\n Пожалуйста, убедитесь в правильности введенного Времени | Сообщение | Номера звука")

#def






def functional(): # Функция, которая будет содержать в себе остальные функции
    set_time()



if __name__ == "__main__":
    functional()
