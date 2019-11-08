from PIL import Image
import pyocr
import pyocr.builders
import sys
import re


class CharacterDetector:
    def __init__(self):
        tools = pyocr.get_available_tools()
        if len(tools) == 0:
            print("No OCR tool found")
            sys.exit(1)
        self.tool = tools[0]
        self.text = None

    def get_string(self, image_path: str, language: str = "eng") -> str:
        base_text: str = self.tool.image_to_string(
            Image.open(image_path),
            lang=language,
            builder=pyocr.builders.TextBuilder(tesseract_layout=6)
        ).replace("\n", " ").replace("  ", " ")
        self.text = base_text
        return base_text

    def plastic_txt(self, base_text: str) -> str:
        matches = re.findall(r"\([0-9]+-[0-9]+\)", base_text)
        for match in matches:
            base_text = base_text.replace(match, "\r\n" + match)
        base_text = re.sub(r"\. \d", ".", base_text)
        titles = re.findall(r"\([a-zA-Z]+ *[a-zA-Z]+\) ", base_text)
        for title in titles:
            base_text = base_text.replace(title, "")
        print(base_text)
        self.text = base_text
        return base_text

    def edit_txt(self, base_text: str) -> str:
        while True:
            self.text = base_text
            want_replace = input("Enter the text you want to replace [0:exit] : ")
            if want_replace == "0":
                return base_text
            else:
                replaced_text = input("Enter the replacement text : ")
                base_text = base_text.replace(want_replace, replaced_text)

    def get_now_text(self) -> str:
        return self.text
