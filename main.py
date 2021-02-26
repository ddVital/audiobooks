import os
import pyttsx3, PyPDF2, os

book = open('makinggames.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(book)
pages = pdf_reader.numPages

speaker = pyttsx3.init()
print(f'total pages: {pages}')


# change the voice speed
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

        if option == 1: # slow
            speaker.setProperty('rate', 120)
            get_page()
        elif option == 2: # normal
            get_page()
        elif option == 3: # fast
            speaker.setProperty('rate', 220)
            get_page()
        else:
            print('please choose one of the options (1, 2 or 3)')
            continue

def cls():
    os.system('cls' if os.name=='nt' else 'clear')


# get the page and call the reader function
def get_page():
    cls()
    for page in range(0, pages):
        current_page = pdf_reader.getPage(page)
        print(f'page number: {page}')
        page_text = current_page.extractText()
        reader(page_text)


# function to read the book
def reader(page_text):
    speaker.say(page_text)
    speaker.runAndWait()


# when the program runs it shows a menu to the user
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
            get_page()
        elif option == 2:
            voice_speed()
        else:
            print('please choose one of the two options (1 or 2)')
            continue


menu() # call the menu