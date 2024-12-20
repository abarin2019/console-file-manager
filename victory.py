# Программа викторина:  Даты рождения знаменитых людей

#  1. Альберт Эйнштейн — 14.03.1879
#  2. Билл Гейтс — 28.10.1955
#  3. Александр Пушкин — 06.06.1799
#  4. Юрий Гагарин — 09.03.1934
#  5. Владимир Высоцкий — 25.01.1938
#  6. Арнольд Шварценеггер — 30.07.1947
#  7. Квентин Тарантино — 27.03.1963
#  8. Лионель Месси — 24.06.1987
#  9. Павел Дуров — 10.10.1984
# 10. Илон Маск — 28.06.1971

import random

famous_people = {
    'Альберт Эйнштейн': '14.03.1879',
    'Билл Гейтс': '28.10.1955',
    'Александр Пушкин': '06.06.1799',
    'Юрий Гагарин': '09.03.1934',
    'Владимир Высоцкий': '25.01.1938',
    'Арнольд Шварценеггер': '30.07.1947',
    'Квентин Тарантино': '27.03.1963',
    'Лионель Месси': '24.06.1987',
    'Павел Дуров': '10.10.1984',
    'Илон Маск': '28.06.1971'
}

months = {
    '01': 'января', '02': 'февраля', '03': 'марта', '04': 'апреля', '05': 'мая',
    '06': 'июня', '07': 'июля', '08': 'августа', '09': 'сентября', '10': 'октября',
    '11': 'ноября', '12': 'декабря'
}

days = {
    '01': 'первое', '02': 'второе', '03': 'третье', '04': 'четвёртое', '05': 'пятое',
    '06': 'шестое', '07': 'седьмое', '08': 'восьмое', '09': 'девятое', '10': 'десятое',
    '11': 'одиннадцатое', '12': 'двенадцатое', '13': 'тринадцатое', '14': 'четырнадцатое',
    '15': 'пятнадцатое', '16': 'шестнадцатое', '17': 'семнадцатое', '18': 'восемнадцатое',
    '19': 'девятнадцатое', '20': 'двадцатое', '21': 'двадцать первое', '22': 'двадцать второе',
    '23': 'двадцать третье', '24': 'двадцать четвёртое', '25': 'двадцать пятое',
    '26': 'двадцать шестое', '27': 'двадцать седьмое', '28': 'двадцать восьмое',
    '29': 'двадцать девятое', '30': 'тридцатое', '31': 'тридцать первое'
}


def play_victory():
    again = True

    while again:
        sample_people = random.sample(list(famous_people.keys()), 5)
        sample_people = {name: famous_people[name] for name in sample_people}

        score = 0
        print('Введите дату рождения знаменитости (в формате ДД.ММ.ГГГГ):  ')
        for i in sample_people:
            answer = input(f'\n{i} : ')
            if answer == sample_people[i]:
                score += 1
            else:
                day, month, year = sample_people[i].split('.')
                print(f'Правильный ответ:  {days[day]} {months[month]} {year} года')

        errors = len(sample_people) - score

        print(f'\nКоличество правильных ответов:  {score}')
        print(f"Количество ошибок:  {errors}")

        again_answer = input('\nНачать игру сначала? (Да/Нет):  ')

        if again_answer.lower() == 'нет':
            again = False


if __name__ == '__main__':
    play_victory()