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
        print(self.tool)

    def get_string(self, image_path) -> str:
        txt = self.tool.image_to_string(
            Image.open(image_path),
            lang="eng",
            builder=pyocr.builders.TextBuilder(tesseract_layout=6)
        )
        return txt.replace("\n", " ").replace("  ", " ")

    def platic_txt(self, base_text) -> str:
        matches = re.findall(r"\([0-9]+-[0-9]+\)", base_text)
        for match in matches:
            base_text = base_text.replace(str(match), "\n" + str(match))
        base_text = re.sub(r"\. \d", ".", base_text)
        titles = re.findall(r"\(.+\) \n", base_text)
        for title in titles:
            base_text = base_text.replace(title, "")
        print(base_text)
        return base_text