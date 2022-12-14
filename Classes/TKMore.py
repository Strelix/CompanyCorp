import customtkinter


class TKMore:
    def __init__(self):
        # pass
        print('[SERVER] TKMore Connected')

    def multi_pack(self, *items):
        for item in items:
            item[0].pack(side=item[1])

        return

    def button_purple(self, master, text='BTN') -> object:
        return customtkinter.CTkButton(master=master, text=text, fg_color='#2B2B2B', hover_color='medium purple')

    def container_main(self, master, main) -> object:
        return customtkinter.CTkFrame(master=master,
                                      width=main.main_screen.screensize[0] * 0.3,
                                      height=main.main_screen.screensize[1] * 0.1)

        # self.username_container.pack(side=TOP, pady=(main.main_screen.screensize[1] * 0.1, 0))
        # self.username_container.propagate(False)
