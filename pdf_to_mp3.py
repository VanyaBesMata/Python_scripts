import pdfplumber
from gtts import gTTS
from pathlib import Path
from art import tprint


def main():
    tprint('PDF>>TO>>MP3', font='bulbhead')
    file_path = input('\n Enter a file path: ')
    language = input("Choose language, for example 'en' or 'ru': ")
    print(pdf_to_mp3(file_path=file_path, language=language))


def pdf_to_mp3(file_path='test.pdf', language='en'):
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':

        print(f'[*] Original file: {Path(file_path).name}')
        print('[*] Processing ...')

        # Разделяем на строки теста.
        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]

        # Соединяем строки текста в единый блок.
        text = ''.join(pages)
        # Убираем переход на новую строку.
        text = text.replace('\n', '')

        # Обрабатываем текстовый файл в аудио файл.
        my_audio = gTTS(text=text, lang=language)
        file_name = Path(file_path).stem
        my_audio.save(f'{file_name}.mp3')

        return f'[*] {file_name}.mp3 save success!!'

    else:
        return 'File not exists, check file!!!'


if __name__ == '__main__':
    main()
