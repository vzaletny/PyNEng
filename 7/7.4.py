#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pprint import pprint

ignore_list = ['duplex', 'alias', 'Current configuration']


def config_to_dict(conf_file):
    """
    Создать функцию, которая обрабатывает конфигурационный файл коммутатора
    и возвращает словарь:
    * Все команды верхнего уровня (глобального режима конфигурации), будут ключами.
    * Если у команды верхнего уровня есть подкоманды, они должны быть в значении у соответствующего ключа, в виде списка (пробелы в начале строки можно оставлять).
    * Если у команды верхнего уровня нет подкоманд, то значение будет пустым списком

    Функция ожидает в качестве аргумента имя конфигурационного файла.

    Проверить работу функции на примере файла config_sw1.txt

    При обработке конфигурационного файла, надо игнорировать строки, которые начинаются с '!',
    а также строки в которых содержатся слова из списка ignore.

    Для проверки надо ли игнорировать строку, использовать функцию ignore_command.


    Ограничение: Все задания надо выполнять используя только пройденные темы.
    """
    try:
        with open(conf_file, 'r', encoding='utf-8') as f:
            conf_dict = {}
            cmd = ''
            for line in f:
                if line.strip() and not line.startswith('!') and not ignore_command(line, ignore_list):
                    if not line.startswith(' '):
                        cmd = line.strip()
                        conf_dict[cmd] = []
                    else:
                        conf_dict[cmd].append(line.strip())
            return conf_dict
    except FileNotFoundError:
        print('File not found')
        return


def ignore_command(command, ignore):
    """
    Функция проверяет содержится ли в команде слово из списка ignore.

    command - строка. Команда, которую надо проверить
    ignore - список. Список слов

    Возвращает
    * True, если в команде содержится слово из списка ignore
    * False - если нет
    """
    return any(word in command for word in ignore)
    # return not bool(i for i in ignore if i in command)


ifile = './PyNEng/7/config_sw1.txt'
config_dict = config_to_dict(ifile)
pprint(config_dict)
