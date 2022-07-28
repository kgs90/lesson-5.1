my_text = 'Напишите программуабв удаляющую из этогоабв текса все "абв"'

def del_some_words(my_text):
    my_text = list(filter(lambda x: 'абв'  in x, my_text.split()))
    return " ".join(my_text)

my_text = del_some_words(my_text)
print(my_text)