import datetime  # Импортируем библиотеку для работы со временем
import pygame   # Импортируем библиотеку для работы с окном
import sys      # Импортируем библиотеку, с помощью которой программа будет завершаться, если пользователь неправильно что-то ввёдет

def set_time(): # Создаём новую функцию, для установки времени и учёта предпочтений пользователя
    sounds = {1: 'FileMP3/alarm-clock-1', 2: 'FileMP3/The-Soviet-Union-2'}
    try:
        print("\n Загрузка..." * 10)  # 10 раз пишем слово "Загрузка...", чтобы не было видно сообщение от PyGame
        time = input("Введите время для будильника в формате ЧЧ:ММ: ")
        time_list = [int(x) for x in time.split(":")]  # Создаём новый список, переводим все элементы из str в int
        user_time = datetime.time(*time_list).strftime("%H:%M") # Уходим из списка, разделяем значения по часы:минуты. В конце обрезаем секунды
        message = input("Введите сообщение, которое нужно отправить при срабатывании будильника. Если сообщение отсутствует, укажите 0: ")
        number = int(input(f"Введите номер звука {sounds}: "))
        return user_time, message, number

    except:
        print("\n Пожалуйста, убедитесь в правильности введенного Времени | Сообщение | Номера звука: ")
        sys.exit()

def display_sound(number):
    sounds = {1: 'FileMP3/alarm-clock-1', 2: 'FileMP3/The-Soviet-Union-2'}
    pygame.init()
    pygame.display.set_mode((800, 600))
    run = True
    while run:
        sound = sounds.get(number)
        pygame.mixer.init()
        file_path = sound
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                run = False

def start_cycle(time,message, number_sound): # Создаём функцию, на которой будет держаться цикл

    try:
        while True:
            if str(time) == str(datetime.datetime.now().strftime("%H:%M")):
                if int(message) == 0:
                    print("\n Будильник сработал" * 10)                          # Печатаем сообщение при срабатывании будильника
                    display_sound(number_sound)
                    break
    except ValueError:
        print(message)
        display_sound(number_sound)
    except:
        print("Произошла какая-то ошибка...")



def functional(): # Функция, которая будет содержать в себе остальные функции
    time,message,number_sound = set_time()
    start_cycle(time,message,number_sound) # Передаём значение в функцию - цикл




if __name__ == "__main__":
    functional()
