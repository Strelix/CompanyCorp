import customtkinter

class TKMore:
    def __init__(self):
        pass

    def multi_pack(self, *items):
        for item in items:
            item[0].pack(side=item[1])

        return