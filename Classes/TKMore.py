import customtkinter


class TKMore:
    def multi_pack(self, *items) -> None:
        for item in items:
            item[0].pack(side=item[1])
        return

    def button_purple(self, master, text='BTN') -> object:
        return customtkinter.CTkButton(master=master,
                                       text=text, fg_color='purple', hover_color='medium purple')

    def container_main(self, master: object, main: object) -> object:
        """

        :rtype: object
        self.username_container.pack(side=TOP, pady=(main.main_screen.screensize[1] * 0.1, 0))
        self.username_container.propagate(False)
        """
        return customtkinter.CTkFrame(master=master,
                                      width=main.main_screen.screensize[0] * 0.3,
                                      height=main.main_screen.screensize[1] * 0.1)


    def test(self):
        self.container_main()
