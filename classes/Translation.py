import urllib.parse
import urllib.request


class Translation:
    def __init__(self, url: str, src: str = "en", target: str = "ja"):
        self.url = url
        self.param = [
            ("source", src),
            ("target", target),
        ]

    def get_translated_text(self, text: str) -> str:
        self.param.append(("text", text))
        self.url += f"{urllib.parse.urlencode(self.param)}"
        print(self.url)
        try:
            result = urllib.request.urlopen(self.url).read()
            return result.decode('utf-8')
        except ValueError:
            print("Access Error")
            return "Error"