from .DMA import decompile as dma
from .rule.url import get_url
from .rule.static_vuln import vuln_match_all


class MATCH:
    def __init__(self, path, out_path):
        self.path = path
        self.out_path = out_path
        self.source_path = []
        self.status_list = []
        self.match_rule = ""
        self.decompile()

    def decompile(self):
        result = dma.decompile(self.path, self.out_path)
        if "ERROR" not in result[0]:
            self.source_path = result
        else:
            print("decompile error: ", result[0])

    def status(self):
        with open("result", "r", encoding="utf-8") as f:
            result = f.read()
            self.status_list = result.split("\n")
        return self.status_list

    def match_url(self):
        return get_url(self.source_path)

    def match_vuln_all(self):
        return vuln_match_all(self.source_path)


if __name__ == '__main__':
    out_path = r"/Users/ios/Downloads/out"
    file_path = r"/Users/ios/Downloads/wifi.apk"
    match = MATCH(file_path, out_path)
    #match_result = match.match_url()
    match_result = match.match_vuln_all()
    print(match_result)
