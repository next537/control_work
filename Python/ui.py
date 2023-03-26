import Note
def create_note(number):
    title = check_len_text_input(
        input('Введите Название заметки: '), number)
    body = check_len_text_input(
        input('Введите Описание заметки: '), number)
    return Note.Note(title=title, body=body)
def menu():
    print("\nЭто программа 'Заметки'. Имеются следующие функции:\n\n1 - вывод всех заметок\n2 - добавление заметки\n3 - удаление заметки\n4 - редактирование заметки\n\nВведите номер функции: ")
def check_len_text_input(text, n):
    while len(text) <= n:
        print(f'Текст должен быть больше {n} символов\n')
        text = input('Введите текcт: ')
    else:
        return text