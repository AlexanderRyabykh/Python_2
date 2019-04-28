# Задание 1. Каждое из слов «разработка», «сокет», «декоратор»
# представить в строковом формате и проверить тип и
# содержание соответствующих переменных. Затем с помощью
# онлайн-конвертера преобразовать строковые представление
# в формат Unicode и также проверить тип и содержимое
# переменных.
print('\nЗадание 1')
words = ['разработка', 'сокет', 'декоратор']

for word in words:
    print(f'{word} - тип {type(word)}')

converted_words = ['\xd1\x80\xd0\xb0\xd0\xb7\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xba\xd0\xb0',
                   '\x63\x6a\x72\x74\x6e',
                   '\xd0\xb4\xd0\xb5\xd0\xba\xd0\xbe\xd1\x80\xd0\xb0\xd1\x82\xd0\xbe\xd1\x80']

for word in converted_words:
    print(f'{word} - тип {type(word)}')



# Задание 2. Каждое из слов «class», «function», «method» записать в
# байтовом типе без преобразования в последовательность
# кодов (не используя методы encode и decode) и определить
# тип, содержимое и длину соответствующих переменных.
print('\nЗадание 2')
words_2 = [b'class', b'function', b'method']

for word in words_2:
    print(f'{word} - тип {type(word)} - длина {len(word)}')

print()

# Задание 3. Определить, какие из слов «attribute», «класс», «функция», «type»
# невозможно записать в байтовом типе.
print('\nЗадание 3')
# try:
#     print(b'класс')
# except SyntaxError:
#     print('Увы')
# # except почему-то не срабатывает

# print(b'функция') # ошибка

print(b'attribute', b'type')

print()

# Задание 4. Преобразовать слова «разработка», «администрирование»,
# «protocol», «standard» из строкового представления в байтовое и
# выполнить обратное преобразование (используя методы encode и decode).
print('\nЗадание 4')
words_4 = ['разработка', 'администрирование', 'protocol', 'standard']
encoded_words_4 = []

for word in words_4:
    enc_word = word.encode('utf-8')
    print(f'{enc_word} - тип {type(enc_word)}')
    encoded_words_4.append(enc_word)

for word in encoded_words_4:
    dec_word = word.decode('utf-8')
    print(f'{dec_word} - тип {type(dec_word)}')

# Задание 5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из
# байтовового в строковый тип на кириллице.
print('\nЗадание 5')
import subprocess

def ping(site):
    args = ['ping', site]
    subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
    for line in subproc_ping.stdout:
        print(line)
        line = line.decode('cp866').encode('utf-8')
        print(line.decode('utf-8'))


ping('yandex.ru')
ping('youtube.com')

# Задание 6. Создать текстовый файл test_file.txt, заполнить его
# тремя строками: «сетевое программирование», «сокет», «декоратор».
# Проверить кодировку файла по умолчанию. Принудительно открыть файл
# в формате Unicode и вывести его содержимое.
print('\nЗадание 6')
import locale


def_coding = locale.getpreferredencoding()
print(def_coding)

lines = ['сетевое программирование', 'сокет', 'декоратор']
file = open('test_file.txt', 'w')
for item in lines:
    file.write(item)
file.close()

with open('test_file.txt', 'r', encoding='utf-8') as tf:
    try:
        for line in tf:
            print(line)
    except UnicodeDecodeError:
        print('Строка в файле не в utf-8')