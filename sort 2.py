import os
import re
import shutil
sort_folder = ("C:\\Users\\kuzik\\Desktop\\Хлам")

files = {"audio": ["mp3", "ogg", "wav", "amr"],
         "video": ["mp4", "avi", "mov", "mkv", "MOV"],
         "documents": ["doc", "docx", "txt", "pdf", "xlsx", "pptx", "rtf", "PDF", "xls"],
         "images": ["jpeg", "png", "jpg", "svg", "bmp", "BMP"],
         "archives": ["zip", "gz", "tar", "tgz", "rar"]}


def normalize(name):   # Транслитерация c rbhbkbws
    dictionary = {ord("А"): "A", ord("Б"): "B", ord("В"): "V", ord("Г"): "G", ord("Д"): "D", ord("Е"): "E", ord("Ж"): "ZH", ord("З"): "Z",
                  ord("И"): "I", ord("Й"): "J", ord("К"): "K", ord("Л"): "L", ord("М"): "M", ord("Н"): "N", ord("О"): "O", ord("П"): "P",
                  ord("Р"): "R", ord("С"): "S", ord("Т"): "T", ord("У"): "U", ord("Ф"): "F", ord("Х"): "H", ord("Ц"): "TS", ord("Ч"): "CH",
                  ord("Ш"): "SH", ord("Щ"): "SHCH", ord("Ь"): "", ord("Э"): "E", ord("Ю"): "YU", ord("Я"): "YA", ord("Ъ"): "", ord("Ы"): "Y",
                  ord("Ё"): "E", ord("Є"): "E", ord("І"): "Y", ord("Ї"): "YI", ord("Ґ"): "G",
                  ord("а"): "a", ord("б"): "b", ord("в"): "v", ord("г"): "g", ord("д"): "d", ord("е"): "e", ord("ж"): "zh", ord("з"): "z",
                  ord("и"): "y", ord("й"): "j", ord("к"): "k", ord("л"): "l", ord("м"): "m", ord("н"): "n", ord("о"): "o", ord("п"): "p",
                  ord("р"): "r", ord("с"): "s", ord("т"): "t", ord("у"): "y", ord("ф"): "f", ord("х"): "h", ord("ц"): "c", ord("ч"): "ch",
                  ord("ш"): "sh", ord("щ"): "shsc", ord("ь"): "", ord("э"): "e", ord("ю"): "yu", ord("я"): "ya", ord("ъ"): "", ord("ы"): "y",
                  ord("ё"): "e", ord("є"): "e", ord("і"): "y", ord("ї"): "yi", ord("ґ"): "g",
                  ord("1"): "1", ord("2"): "2", ord("3"): "3", ord("4"): "4", ord("5"): "5", ord("6"): "6", ord("7"): "7", ord("8"): "8", ord("9"): "9", ord("0"): "0"}
    en_name = name.translate(dictionary)
    fin_name = re.sub(r"(\W)", '_', en_name)
    return fin_name


dict_keys = list(dict.keys(files)) # Создание папок
print (dict_keys)
for folder in dict_keys:
    os.chdir(sort_folder)
    folder = str(folder)
    if not os.path.isdir(folder):
        os.makedirs(folder)


def move(path):      # Перемещение файлов в папки по назначению
    file_list = os.listdir(path)
    sort_file = list(files.items())
    for el in file_list:
        sufix = el.split(".")[-1]
        file_name = el.split(".")[0:-1]
        for value in range(len(sort_file)):
            if sufix in sort_file[value][1]:
                print(f'Moving {el} in {sort_file[value][0]} folder\n')
                new_el = (normalize("".join(file_name)) + "." + sufix)
                os.rename(
                    el, f'{sort_folder}\\{sort_file[value][0]}\\{new_el}')
            elif sufix  not in sort_file[value][1]:
                continue


def folder_sort(path):  # Рекурсивный проход по папкам
    for folderName, subfolders, filenames in os.walk(path):
        if folderName != dict_keys:
            move(os.chdir(folderName))
        for subfolder in subfolders:
            if folderName != dict_keys:
                move(os.chdir(subfolder))
            for filename in filenames:
                if folderName != dict_keys:
                    move(os.chdir(path))


folder_sort(sort_folder)
x = str ("\\")
print (dict_keys)
def remove_empty_dirs(path):  # Удаление пустых директорий
    for folderName, subfolders, filenames in os.walk(path):
        if (os.path.isdir(folderName) == True) and (os.listdir(folderName) == []) and ((folderName in dict_keys) == False):
            os.rmdir(folderName)
        for subfolder in subfolders:
            if (os.path.isdir(subfolder) == True) and (os.listdir(subfolder) == []) and ((folderName in dict_keys) == False):
                os.rmdir(subfolder)
            for filename in filenames:
                if (os.path.isdir(filename) == True) and (os.listdir(filename) == []) and ((folderName in dict_keys) == False):
                    os.rmdir(filename)

remove_empty_dirs (sort_folder)

def unpackArchive (path):
    file_list = os.listdir(f'{path}\\archives')
    for el in file_list:
        sufix = el.split(".")[-1]
        file_name = el.split(".")[0:-1]
        if sufix in shutil.get_unpack_formats():
            shutil.unpack_archive (f'{path}\\archives\\{el}', f'{path}\\archives\\{file_name}\\{el}')

unpackArchive (sort_folder)
print (dict_keys)