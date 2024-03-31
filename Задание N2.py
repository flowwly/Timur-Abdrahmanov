
player_name = ""
key_found = False
art1_found = False
art2_found = False
art3_found = False
lockpick_found = False

while True:
    if not player_name:
        print("Вы просыпаетесь в комнате. Введите свое имя:")
        player_name = input().strip()
        if not player_name:
            print("Имя не может быть пустым. Попробуйте еще раз.")
            continue

        print(f"{player_name}, вы просыпаетесь в комнате. Что вы хотите сделать?")
        print("1. Открыть дверь")
        print("2. Заглянуть под кровать")
        print("3. Открыть ящик в углу комнаты")
        print("4. Открыть вентиляцию")
        print("5. Взглянуть на тумбочку")
        print("6. Взглянуть на статую рядом с дверью")

        choice = input("Выберите действие: ")
    

    if choice == "1":
        if lockpick_found:
            print(f"{player_name}, вы успешно сбежали!.")
        else:
            print("Дверь заперта. Найдите отмычку.")
    elif choice == "2" and not art1_found:
        print(f"{player_name}, под кроватью вы нашли первый артефакт.")
        art1_found = True
    elif choice == "3" and not lockpick_found:
        if key_found:
            print(f"{player_name}, вы открыли ящик и нашли отмычку.")
            lockpick_found = True
        else:
            print("Ящик заперт. Вам нужно найти ключ.")
    elif choice == "4" and not art2_found:
        print(f"{player_name}, вы открыли вентиляцию и нашли второй артефакт.")
        art2_found = True
    elif choice == "5" and not art3_found:
        print(f"{player_name}, вы взглянули на тумбочку и нашли третий артефакт.")
        art3_found = True
    elif choice == "6":
        if art1_found and art2_found and art3_found:
            print(f"{player_name}, вы активировали статую и получили ключ от ящика.")
            key_found = True
        else:
            print("Статуя не активирована. Для активации найдите три артефакта.")
    else:
        print("Неверный выбор. Попробуйте еще раз.")