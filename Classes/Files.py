import json

class Files:
    def read_file(self, file):
        with open(file) as f:
            content = json.load(f)
            return content