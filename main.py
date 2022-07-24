# -*- coding: utf-8 -*-
from pyrogram.errors import SlowmodeWait, ChatWriteForbidden, UsernameNotOccupied
from pyrogram import Client
from time import sleep


def spamer(text_OTC, need_time, path):
    with open(text_OTC, "r", encoding="utf-8") as file:
        need_text = file.read()

    with open(path, "r", encoding="utf-8") as file:
        list_OTC = file.read().split("\n")

    counter = 0
    while True:
        for chanel in list_OTC:
            try:
                app.send_message(chanel, need_text, parse_mode="html")
                print(f"Сообщение отправлено в {chanel}")
                sleep(1.5)
                counter += 1
            except SlowmodeWait:
                print(f"Error - Slowmode в {chanel}, ничего страшного")
                continue
            except ChatWriteForbidden:
                print(f"Error - Вам запретили писать в этом {chanel} чате или вы не зашли в него")
                continue
            except UsernameNotOccupied:
                print(f"\nДАННОГО КАНАЛА НЕ СУЩЕСТВУЕТ - {chanel}\n")
                continue

        print(f"\nУшел в сон на {int(need_time / 60)} минут. Написано {counter} сообщений\n")
        sleep(need_time)


if __name__ == "__main__":
    print("""
░█▀▀▀█ ░█▀▀█ ─█▀▀█ ░█▀▄▀█ ░█▀▀▀ ░█▀▀█ 　 ░█▀▀▀█ ▀▀█▀▀ ░█▀▀█ 
─▀▀▀▄▄ ░█▄▄█ ░█▄▄█ ░█░█░█ ░█▀▀▀ ░█▄▄▀ 　 ░█──░█ ─░█── ░█─── 
░█▄▄▄█ ░█─── ░█─░█ ░█──░█ ░█▄▄▄ ░█─░█ 　 ░█▄▄▄█ ─░█── ░█▄▄█
@asynco v: 0.2
    """)

    path_config = input("Введите путь до конфигурационных данных\n>> ")

    with open(path_config, "r", encoding="utf-8") as file:
        configurate = file.read().split("\n")

    print(f"\nВаш хэш - {configurate[1]}\n"
          f"Ваш ID - {configurate[0]}\n"
          f"Идет настройка, подождите...")

    api_id = configurate[0]
    api_hash = configurate[1]
    app = Client("SpamerOTC", api_id=api_id, api_hash=api_hash)
    app.start()

    text_OTC = input("\nВведите путь до txt с текстом для спама\n>> ")
    path = input("\nВведите путь до txt с каналами\n>> ")
    need_time = int(input("\nВведите среднее время сна по всем OTC в минутах\n>> ")) * 60
    print()
    spamer(text_OTC=text_OTC, need_time=need_time, path=path)
