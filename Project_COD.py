import datetime  # Импортируем библиотеку для работы со временем
import pygame   # Импортируем библиотеку для работы с окном

def set_time(): # Создаём новую функцию, для установки времени и учёта предпочтений пользователя
    try:
        print("\n Загрузка..." * 10)  # 10 раз пишем слово "Загрузка...", чтобы не было видно сообщение от PyGame
        time = input("Введите время для будильника в формате ЧЧ:ММ:")
        time_list = [int(x) for x in time.split(":")]  # Создаём новый список, переводим все элементы из str в int
        t = datetime.time(*time_list).strftime("%H:%M") # Уходим из списка, разделяем значения по часы:минуты. В конце обрезаем секунды

        while True:
            if str(t) == str(datetime.datetime.now().strftime("%H:%M")):
                print("Будильник сработал")
                break
    except:
        print("\n Пожалуйста, убедитесь в правильности введенного времени")

#def






def functional(): # Функция, которая будет содержать в себе остальные функции
    set_time()



if __name__ == "__main__":
    functional()
