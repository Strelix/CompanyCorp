import json
class Files:
    def read_file(self, file):
        with open(file) as f:
            content = json.load(f)
            return content

    def append_to_file(self, item, file):
        f = open(file, 'w')
        contents = self.read_file('users.json')
        print(contents)
        list(contents).append(item)
        f.write(contents)
        print(self.read_file(file))