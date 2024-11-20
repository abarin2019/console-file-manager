import os
import shutil
import platform
import victory
from bank_account import use_bank_account


def dir_contents(content_type='all'):
    """
    Просмотр содержимого текущей директории, согласно content_type

    :param content_type: 'all' - вывод всех объектов, 'dirs' - только директории, 'files' - только файлы
    :return: список с именами объектов в текущей директории, согласно content_type
    """

    contents = os.listdir('.')

    if content_type == 'dirs':
        return [i for i in contents if os.path.isdir(i)]
    elif content_type == 'files':
        return [i for i in contents if os.path.isfile(i)]
    else:
        return contents


def show_contents(contents: list):
    """
    Выводит на экран: значения списка contents, разделенные тремя пробелами
    :param contents:   представляет собой список значений, который нужно вывести
    :return:  None
    """

    for i in contents:
        print(i, end=' '*3)
    print()


def current_dir():
    """
    Выводит на экран текущую директорию в виде:   Рабочая директория:   'путь к директории'
    :return:  None
    """

    print(f"Рабочая директория:   {os.getcwd()}")


def show_current_dir(content_type='all'):
    """
    Выводит на экран текущую директорию согласно content_type

    :param content_type: 'all' - вывод всех объектов, 'dirs' - только директории, 'files' - только файлы
    :return: None
    """

    current_dir()

    if content_type == 'dirs':
        print('Содержимое (только папки):   ', end='')
    elif content_type == 'files':
        print('Содержимое (только файлы):   ', end='')
    else:
        print('Содержимое:   ', end='')

    show_contents(dir_contents(content_type))


def make_dir():
    show_current_dir()

    folder = input("Введите название папки:  ")
    path_to_makedir = os.path.join(os.getcwd(), folder)

    os.mkdir(path_to_makedir)
    print(f"Создана папка:   {path_to_makedir}")

    print('Обновленное содержимое:   ', end='')
    show_contents(dir_contents())


def delete_file_dir():
    show_current_dir()

    to_delete = input("Введите название файла или папки для удаления:  ")
    path_to_delete = os.path.join(os.getcwd(), to_delete)

    if os.path.isfile(path_to_delete):
        os.remove(path_to_delete)
        print(f"Файл {path_to_delete} удален")

    elif os.path.isdir(path_to_delete):
        shutil.rmtree(path_to_delete)
        print(f"Папка {path_to_delete} удалена")

    else:
        print(f"Ошибка:  Отсутствует файл/папка {path_to_delete}")

    print('Обновленное содержимое:   ', end='')
    show_contents(dir_contents())


def copy_file_dir():
    show_current_dir()

    source = input("Введите файл/папку для копирования:  ")
    source_path = os.path.join(os.getcwd(), source)

    destination = input("Введите куда скопировать:  ")
    destination_path = os.path.join(os.getcwd(), destination)

    if os.path.isfile(source_path):
        shutil.copy(source_path, destination_path)
        print(f"Файл {source_path} скопирован в {destination_path}")

    elif os.path.isdir(source_path):
        shutil.copytree(source_path, destination_path)
        print(f"Папка {source_path} скопирована в {destination_path}")

    else:
        print(f"Ошибка:  Отсутствует файл/папка {source_path}")

    print('Обновленное содержимое:   ', end='')
    show_contents(dir_contents())


def show_os_info():
    print(f"Информация об операционной системе: \n")

    print(f"Имя ОС:  {os.name}")
    print(f"Система:  {platform.system()}")
    print(f"Версия ОС:  {platform.version()}")
    print(f"Версия ядра:  {platform.release()}")
    print(f"Архитектура:  {platform.architecture()}")


def change_work_dir():
    show_current_dir()

    new_work_dir = input("\nДля смены рабочей директории, введите путь (полный или относительный):  ").strip()
    new_path = os.path.abspath(new_work_dir)

    if os.path.exists(new_path):
        os.chdir(new_path)
        print(f"Рабочая директория сменена на:   {os.getcwd()}")
    else:
        print(f"Директории {new_path} не существует")


while True:
    print()
    print("1. Создать папку")
    print("2. Удалить (файл/папку)")
    print("3. Копировать (файл/папку)")
    print("4. Просмотр содержимого рабочей директории")
    print("5. Посмотреть только папки")
    print("6. Посмотреть только файлы")
    print("7. Просмотр информации об операционной системе")
    print("8. Создатель программы")
    print("9. Играть в викторину")
    print("10. Мой банковский счет")
    print("11. Смена рабочей директории")
    print("12. Выход\n")

    choice = input("Выберите пункт меню: ")

    if choice == "1":
        make_dir()

    elif choice == "2":
        delete_file_dir()

    elif choice == "3":
        copy_file_dir()

    elif choice == "4":
        show_current_dir()

    elif choice == "5":
        show_current_dir('dirs')

    elif choice == "6":
        show_current_dir('files')

    elif choice == "7":
        show_os_info()

    elif choice == "8":
        print("Создатель программы:  Баринов Андрей Владимирович")

    elif choice == "9":
        victory.play_victory()

    elif choice == "10":
        use_bank_account()

    elif choice == "11":
        change_work_dir()

    elif choice == "12":
        break
    else:
        print("Неверный пункт меню")