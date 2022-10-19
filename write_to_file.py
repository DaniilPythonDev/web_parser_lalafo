"""
В этом файле выполняется запись и чтение файлов.
"""

import csv
import json


class WriteRead:

    @staticmethod
    def html_file(req=None, file_name='data.html', mods='w', encoding='utf-8'):
        """
        Функция записовает;читоет HTML файлы!
        :param req: - Принимает обекты модуля "requests" в текстовом формате
        :param file_name: - Имя файла
        :param mods: - Режим работы (чтение;запись)
        :param encoding: - Кодировка
        :return: Сообшения;Возврошает донные из файлов
        """
        with open(f'file/{file_name}', mods, encoding=encoding) as file:
            if mods == 'w':
                file.write(req.text)
            elif mods == 'a':
                file.write(req.text)
            elif mods == 'r':
                read = file.read()
                return read
        return f'Создан HTML файл file/{file_name}!'

    @staticmethod
    def json_file(dict_=None, file_name='data.json', mods='w', nocirilic=False, indent=4):
        """
        Функция записовает;читоет JSON файлы!
        :param dict_:  - Принимает банные типа DICT
        :param file_name: - Имя файла
        :param mods: - Режим работы (чтение;запись)
        :param nocirilic: - Принимает банные типа BOOL (Для корректнаго отображения текста)
        :param indent: - Принимает банные типа INT, число отступа (Для корректнаго отображения текста)
        :return: Сообшения;Возврошает донные из файлов
        """
        with open(f'file/{file_name}', mods, encoding='utf-8') as file:
            if mods == 'w':
                json.dump(dict_, file, indent=indent, ensure_ascii=nocirilic)
            elif mods == 'a':
                pass
            elif mods == 'r':
                read = json.load(file)
                return read
        return f'Создан JSON файл file/{file_name}!'

    @staticmethod
    def text_file(dict_=None, file_name='data.html', mods='w'):
        """
        Функция записовает;читоет TXT файлы!
        :param dict_:  - Принимает банные типа DICT
        :param file_name: - Имя файла
        :param mods: - Режим работы (чтение;запись)
        :return: Сообшения;Возврошает донные из файлов
        """
        with open(f'file/{file_name}', mods, encoding='utf-8') as file:
            if mods == 'w':
                for k, v in dict_.items():
                    file.write(f'{k}: {v}\n')
            elif mods == 'a':
                for k, v in dict_.items():
                    file.write(f'{k}: {v}\n')
            elif mods == 'r':
                read = file.read()
                return read
        return f'Создан TXT файл file/{file_name}!'

    @staticmethod
    def csv_file(dict_=None, file_name='data.csv', mods='w', os_windows=True):
        """
        Функция записовает;читоет TXT файлы!
        :param dict_:  - Принимает банные типа DICT
        :param file_name: - Имя файла
        :param mods: - Режим работы (чтение;запись)
        :param os_windows: (Для корректной зописи)
        :return: Сообшения;Возврошает донные из файлов
        """
        try:
            if os_windows:
                encoding = 'cp1251'
                delimiter = ';'
            else:
                encoding = 'utf-8'
                delimiter = ';'
            with open(f'file/{file_name}', mods, encoding=encoding, newline='') as file:
                if mods == 'w':
                    writer = csv.writer(file, delimiter=delimiter)
                    rasd = csv.list_dialects()
                    print(rasd)
                    writer.writerow(['katigoies', 'links'])
                    for k, v in dict_.items():
                        for e in [' ', '-', ',']:
                            if e in k:
                                k.replace(e, '_')
                            elif k not in [' ', '-', ',']:
                                writer.writerow([k, v])
                                break
                elif mods == 'a':
                    writer = csv.writer(file, delimiter=delimiter)
                    rasd = csv.list_dialects()
                    print(rasd)
                    writer.writerow(['katigoies', 'links'])
                    for k, v in dict_.items():
                        for e in [' ', '-', ',']:
                            if e in k:
                                k.replace(e, '_')
                            elif k not in [' ', '-', ',']:
                                writer.writerow([k, v])
                                break
                elif mods == 'r':
                    read = file.read()
                    return read
            return f'Создан CSV файл file/{file_name}!'
        except PermissionError:
            return 'ERROR!(Закройте программы!)'


if __name__ == '__main__':
    # p = write_read().csv_file({'a1': 'a2', 'a3': 'a4', 'a5': 'a6'})
    # p = WriteRead().json_file(mods='r')
    # print(p)
    print(type(None))
