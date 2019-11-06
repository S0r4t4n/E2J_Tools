from FileSelector import FileSelector
from CharacterDetector import CharacterDetector
from googletrans import Translator
import re

if __name__ == '__main__':
    extensions = ["png", "PNG", "jpg", "jpeg", "JPEG"]
    translator = Translator()
    cd = CharacterDetector()
    fs = FileSelector("img")
    file_path = fs.get_file_path(extensions)
    txt = cd.get_string(file_path)
    txt = cd.platic_txt(txt)
    translated_txt = translator.translate(txt, dest='ja')
    translated_txt = re.sub(r"Tra.+text=", "", str(translated_txt))
    translated_txt = re.sub(r", pronu.+", "", str(translated_txt))
    print(translated_txt)