import datetime
import pygame

print("\n" * 10) # Убираем сообщение от PyGame, для чистоты в консоли


class Alarm:  # Создаём класс, для создания будильника с параметрами
    def __init__(self, time, message, sound, week, answe):
        self.time = time
        self.message = message
        self.sound = sound
        self.week = week
        self.answe = answe

class Alarms: # Создаём класс для хранения всех будильников

    def __init__(self):
        self.alarms = []

    def new_alarm(self, name):
        self.alarms.append(name)

    def get_alarms(self):
        return self.alarms

    def del_alarms(self,name):
        self.alarms.remove(name)

all_alarms = Alarms() # Создаём объект, где будут храниться все будильники

def set_time(value): # Создаём новую функцию, для установки времени и учёта предпочтений пользователя
    sounds = {1: 'FileMP3/alarm-clock-1', 2: 'FileMP3/The-Soviet-Union-2'} # Создаём словарь, для вывода возможных звуков пользователю
    while True:
        try:

            time = input("\nВведите время для будильника в формате ЧЧ:ММ: ")                                                                     # Спрашиваем время у пользователя
            time_list = [int(x) for x in time.split(":")]  # Создаём новый список, переводим все элементы из str в int
            user_time = datetime.time(*time_list).strftime("%H:%M") # Уходим из списка, разделяем значения по часы:минуты. В конце обрезаем секунды
            message = input("\nВведите сообщение, которое нужно отправить при срабатывании будильника. Если сообщение отсутствует, укажите 0: ") # Спрашиваем сообщение у пользователя
            number = int(input(f"\nВведите номер звука {sounds}: "))                                                                             # Спрашиваем номер звука у пользователя
            if value:
                week = list(input("Укажите день недели, когда будильник должен будет сработать. \n1 - понедельник\n2 - вторник\n3 - среда\n4 - четверг\n5 - пятница\n6 - суббота\n7 - воскресенье: "))
            else:  # Если пользоватесь захотел выбрать дни недели, мы уточняем какие, else: week = None
                week = None
            answe = input("\nВы хотите чтобы будильник повторялся? Да ~ Нет: ").lower().strip()  # Спрашиваем, хочет ли пользователь повторение будильника в указанную дату и время
            if answe != "да":
                answe = False

            try:
                if int(message) == 0:
                    message = "Время вставать!"
            except:
                pass
            return user_time, message, number, week, answe
            break
        except:
            print("\n Пожалуйста, убедитесь в правильности введенного Времени | Сообщение | Номера звука: ")


def display_sound(number):  # Создаём новую функцию, для воспроизведения звука и дисплея
    sounds = {1: 'FileMP3/alarm-clock-1', 2: 'FileMP3/The-Soviet-Union-2'}

    sound_file = sounds.get(number)

    pygame.init()
    pygame.mixer.init()
    pygame.display.set_mode((800, 600))
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()

    running = True
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
        if not pygame.mixer.music.get_busy():
            running = False
        pygame.time.delay(100)

    pygame.quit()

def start_cycle(): # Создаём функцию, на которой будет держаться цикл


    while all_alarms is not None:
        pygame.time.delay(100)
        current_time = datetime.datetime.now().strftime("%H:%M")
        today = datetime.date.today()
        for alarn in all_alarms.get_alarms():
            if alarn.week: # Если со днями недели
                if current_time == alarn.time and str(datetime.date.today().isoweekday()) in alarn.week:

                    print("\n" * 2, alarn.message, "\n" * 2)
                    display_sound(alarn.sound)
                    answe = input("Хотите повторить будильник через 5 минут? Да или + : ").lower().strip()
                    if answe == "Да" or answe == "+":
                        time_str = alarn.time

                    # Преобразуем
                        full_datetime = datetime.datetime.combine(datetime.date.today(),datetime.datetime.strptime(time_str, "%H:%M").time())

                    # Добавляем 5 минут
                        full_datetime += datetime.timedelta(minutes=5)

                    # Обновляем строку
                        alarn.time = full_datetime.strftime("%H:%M")
                        continue

                    time_str = alarn.time
                    full_datetime = datetime.datetime.combine(datetime.date.today(),datetime.datetime.strptime(time_str, "%H:%M").time())


                    full_datetime += datetime.timedelta(minutes=-1) # Строка, которая убирает постоянное включение будильника в назначенное время

                        # Обновляем строку
                    alarn.time = full_datetime.strftime("%H:%M")
                    if alarn.answe:
                        pass
                    else:
                        alarn.week.remove(str(datetime.date.today().isoweekday()))
                        print(alarn.week)
            else: # Если без дней недели


                if current_time == alarn.time:
                    print("\n" * 2, alarn.message, "\n" * 2)
                    display_sound(alarn.sound)
                    answe = input("\nХотите повторить будильник через 5 минут? Да или + : ").lower().strip()
                    if answe == "Да" or answe == "+":
                        time_str = alarn.time

                        # Преобразуем
                        full_datetime = datetime.datetime.combine(datetime.date.today(),datetime.datetime.strptime(time_str, "%H:%M").time())

                        # Добавляем 5 минут
                        full_datetime += datetime.timedelta(minutes=5)

                        # Обновляем строку
                        alarn.time = full_datetime.strftime("%H:%M")
                        continue
                    if alarn.answe:
                        pass
                    else:
                        all_alarms.del_alarms(alarn)
    print("Все будильники закончились")

def main(): # Создаём основную функцию
    while True:
        a = input("Вы хотите поставить будильник на определённые дни недели? Да ~ Нет: ").lower().strip()
        if a == "да":
            user_time, message, number, week, answeb = set_time(a)
            user_time = Alarm(user_time,message,number,week,answeb)
            all_alarms.new_alarm(user_time)
            all_alarms.get_alarms()
        else:
            a = None
            user_time, message, number, week, answeb = set_time(a)
            user_time = Alarm(user_time, message, number, week, answeb)
            all_alarms.new_alarm(user_time)

        answe = input("\n Вы хотите поставить ещё один будильник? Да или + : ").lower().strip()
        if answe == "да" or answe == "+":
            continue
        start_cycle()


if __name__ == "__main__":
    main()
