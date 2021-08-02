from PIL import Image
import os.path
from questionary import Separator, prompt, print
from pprint import pprint
import ctypes
import subprocess
from pydub import AudioSegment
import PyPDF2

image_types = ['JPG', 'JPEG', 'PNG', 'JFIF', 'TIF', 'TIFF', 'BMP', 'WEBP']
archive_types = ['7Z', 'JAR', 'RAR', 'ZIP']
document_types = ['PDF', 'TXT', 'HTML', 'MD', 'DOC', 'DOCX', 'JSON', 'XLS', 'CSV', 'TEX', 'RTF']
type_dict = {'Archive':archive_types, 'Image':image_types, 'Document':document_types}

def logo():
    print('''   __________   ____
  / __/  _/ /  / __/
 / _/_/ // /__/ _/
/_/_/___/____/___/____________  _  _____   _____  __
  /  |/  /  _/ __/ __/  _/ __ \/ |/ / _ | / _ \ \/ /
 / /|_/ // /_\ \_\ \_/ // /_/ /    / __ |/ , _/\  /
/_/  /_/___/___/___/___/\____/_/|_/_/ |_/_/|_| /_/
                                                    \n''', style="bold italic fg:yellow")
    print('CONVERT ANYTHING', style="bold italic fg:yellow")
    print('SY.MBA Development, 2021\n', style="bold italic fg:yellow")

def JPG_to_JPEG(filein):
    img = Image.open(filein)
    img.save(filein.replace('.jpg', '.jpeg'))

def JPG_to_PNG(filein):
    img = Image.open(filein)
    img.save(filein.replace('.jpg', '.png'))

def JPG_to_JFIF(filein):
    img = Image.open(filein)
    img.save(filein.replace('.jpg', '.jfif'))

def JPG_to_TIF(filein):
    img = Image.open(filein)
    img.save(filein.replace('.jpg', '.tif'))

def JPG_to_TIFF(filein):
    img = Image.open(filein)
    img.save(filein.replace('.jpg', '.tiff'))

def JPG_to_BMP(filein):
    img = Image.open(filein)
    img.save(filein.replace('.jpg', '.bmp'))

def JPG_to_WEBP(filein):
    img = Image.open(filein)
    img.save(filein.replace('.jpg', '.webp'))

def MP3_to_WAV(filein):
    sound = AudioSegment.from_mp3(filein)
    sound.export(dst.replace('.mp3', '.wav'), format="wav")

def PDF_to_TXT(filein):
    pdfFileObject = open(filein, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
    pageObject = pdfReader.getPage(0)
    text = pageObject.extractText()
    pdfFileObject.close()
    f = open(filein.replace('.pdf', '.txt'), 'w')
    f.write(text)
    f.close()


def HTML_to_TXT(filein):
    f = open(filein, 'r')
    data = f.read()
    f.close()
    f = open(filein.replace('.html', '.txt'), 'w')
    f.write(data)
    f.close()


def det_file(**kwargs):
    questions = [
        {
            "qmark": "FM",
            "type": "select",
            "name": "filetype",
            "message": "Which type of file would you like to convert?",
            "choices": ["Audio", "Archive", "Document", "Image", "Video"],
        },
        {
            "qmark": "FM",
            "type": "text",
            "name": "myfile",
            "message": "Please enter the file you would like to use >",
            "validate": lambda val: os.path.isfile(val) ,
        },
    ]
    return prompt(questions)

def det_types_from(*args):
    questions = [
        {
            "qmark": "FM",
            "type": "select",
            "name": "extension_a",
            "message": "Which file extension would you like to convert from?",
            "choices": type_dict[args[0]],
        },
    ]
    return prompt(questions)

def det_types_to(*args):
    questions = [
        {
            "qmark": "FM",
            "type": "select",
            "name": "extension_b",
            "message": "Which file extension would you like to convert to?",
            "choices": args[1][0:args[1].index(args[0])]+args[1][args[1].index(args[0])+1:],
        },
    ]
    return prompt(questions)

def repeat(*args):
    questions = [
        {
            "qmark": "FM",
            "type": "confirm",
            "name": "repeat",
            "message": "Would you like to convert another file?",
            "default": True
        },
    ]
    x = prompt(questions)
    if x['repeat'] == True:
        return menu()
    exit()
    return 0

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')




if __name__ == "__main__":
    def menu():
        choices = det_file()
        myfile = choices['myfile']
        fromfile = det_types_from(choices['filetype'])['extension_a']
        tofile = det_types_to(fromfile, type_dict[choices['filetype']])['extension_b']
        eval(fromfile+'_to_'+tofile+'('+'myfile'+')')
        print("Conversion Success!", style="bold italic fg:darkgreen")
        return repeat()
    clear()
    logo()
    menu()
