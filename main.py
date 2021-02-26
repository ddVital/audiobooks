import os
import pyttsx3, PyPDF2, os

book = open('makinggames.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(book)
pages = pdf_reader.numPages

speaker = pyttsx3.init()
print(pages)

def voice_speed():
    print(
        """
        after you chose the audiobook will start.
        [ 1 ] - Slow
        [ 2 ] - Normal
        [ 3 ] - Fast
        """
    )

    while True:
        option = int(input('chosen option: '))

        if option == 1:
            speaker.setProperty('rate', 120)
            get_page()
        elif option == 2:
            get_page()
        elif option == 3:
            speaker.setProperty('rate', 210)
            get_page()
        else:
            print('please choose one of the options (1, 2 or 3)')
            continue

def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def get_page():
    cls()
    for page in range(0, pages):
        current_page = pdf_reader.getPage(page)
        print(f'page number: {page}')
        page_text = current_page.extractText()
        reader(page_text)


def reader(page_text):
    speaker.say(page_text)
    speaker.runAndWait()

def menu():
    print(
        """
        choose one of the options below:

        [ 1 ] - Start
        [ 2 ] - Speed Settings
        """
    )

    while True:
        option = int(input('chosen option: '))
        if option == 1:
            # cls()
            get_page()
        elif option == 2:
            # cls()
            voice_speed()
        else:
            print('please choose one of the two options (1 or 2)')
            continue

menu()