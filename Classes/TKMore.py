import customtkinter

class TKMore:
    def __init__(self):
        pass

    def multi_pack(self, *items):
        return [item.pack(side=place) for item,place in items]