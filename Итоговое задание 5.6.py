import random


# draw_field - выводит на консоль поле игры
def draw_field():
    # Вывод заголовка с номерами столбцов
    print()
    row = ' '
    for j in range(dim):
        row = row + ' ' + str(j)
    print(row)

    # Построчный вывод на консоль поля с номером строки в начале каждой строки
    for i in range(dim):
        row = str(i)
        for j in range(dim):
            ch = str(field[i][j]) if field[i][j] is not None else '-'
            row = row + ' ' + ch
        print(row)


# check_win - проверка условий победы для игрока, играющего символами 'marker'
def check_win(marker):
    pattern = [marker for i in range(dim)]
    rotated_field = list(zip(*field))
    left_diag = []
    right_diag = []

    for i in range(dim):
        if field[i] == pattern or rotated_field[i] == tuple(pattern):
            return True
        left_diag.append(field[i][i])
        right_diag.append(field[i][dim-1-i])

    if left_diag == pattern or right_diag == pattern:
        return True

    return False


# get_comp_move - выбирает случайную свободную ячейку на поле для генерации хода компьютера
def get_comp_move():
    for i in random.sample(range(dim), dim):
        for j in random.sample(range(dim), dim):
            if field[i][j] is None:
                yield i, j
    yield -1, -1


def say_as_comp(str_):
    print(f">> {str_}")


# Глобальные переменные
dim = 3         # Размерность поля для игры
field = [[None for j in range(dim)] for i in range(dim)]

print("\nДобро пожаловать в Игру «Крестики-нолики»!\n")
human_marker = str(input("Для начала выберите, за кого будете играть - Х или 0? ")).lower()

if human_marker in ['x', 'х', '+']:
    say_as_comp("Отлично, ваши КРЕСТИКИ")
    human_marker, comp_marker = 'x', 'o'
elif human_marker in ['0', 'o']:
    say_as_comp("Отлично, ваши НОЛИКИ")
    human_marker, comp_marker = 'o', 'x'
else:
    say_as_comp("Ок, если не смогли определиться, то значит ваши КРЕСТИКИ )))")
    human_marker, comp_marker = 'x', 'o'

while True:
    draw_field()

    str_ = input("Ваш ход. Введите две цифры, первая цифра - номер строки, вторая - номер столбца (q для выхода): ")

    if str_ == '':
        say_as_comp("Все-таки введити что-нибудь...")
        continue

    if str_[0] == 'q':
        say_as_comp("Bye-bye!")
        break

    if len(str_) == 2 and str_.isdigit():
        i, j = map(int, str_)
    else:
        say_as_comp("Не, это для другой игры... Мы играем в «Крестики-нолики». Будьте внимательны!")
        continue

    if i < dim and j < dim:
        if field[i][j] is None:
            field[i][j] = human_marker
        else:
            say_as_comp("Похоже, тут уже занято. Выберите другую ячейку")
            continue
    else:
        say_as_comp("Уууу, это где-то за пределами поля. Выберите другую ячейку")
        continue

    if check_win(human_marker):
        draw_field()
        say_as_comp("Вы победили!")
        break

    i, j = next(get_comp_move())
    if i < 0 or j < 0:
        draw_field()
        say_as_comp("Похоже, игра подошла к концу. Победила дружба!!")
        break
    else:
        field[i][j] = comp_marker
        if check_win(comp_marker):
            draw_field()
            say_as_comp("Наконьец-то! Побьеда!!!")
            break

