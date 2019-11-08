from classes.FileSelector import FileSelector
from classes.CharacterDetector import CharacterDetector
from classes.Translation import Translation

if __name__ == '__main__':
    url = "https://script.google.com/macros/s/AKfycbyalI7byYy5rEzcqVb1WUOWyLAH08e5eLGP98eR4saMZ5KSPG8/exec?"
    extensions = ["png", "PNG", "jpg", "jpeg", "JPEG"]
    cd = CharacterDetector()
    fs = FileSelector("img")
    file_path = fs.get_file_path(extensions)
    txt = cd.get_string(file_path)
    txt = cd.plastic_txt(txt)
    txt = cd.edit_txt(txt)
    ts = Translation(url)
    translated_txt = ts.get_translated_text(txt)
    print(translated_txt)