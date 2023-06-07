import tkinter as tk


class App:
    def __init__(self, master):
        self.master = master
        self.master.iconbitmap("icon.ico")
        self.master.title("Заказ кодов")
        self.master.geometry("800x600")
        self.master.resizable(False, False)

        # Создание контейнера для других виджетов
        self.frame = tk.Frame(self.master)

        self.button_first_workshop = tk.Button(text="Первый цех")
        self.button_first_workshop.place(x=10, y=350)

        self.button_kmc = tk.Button(text="Кисломолочный цех")
        self.button_kmc.place(x=10, y=400)

        self.button_csm = tk.Button(text="Цех стерилизованного молока")
        self.button_csm.place(x=10, y=450)

        self.button_tv = tk.Button(text="Творожный цех")
        self.button_tv.place(x=10, y=500)

        self.button_exit = tk.Button(text="Выход", command=self.close_window)
        self.button_exit.place(x=10, y=550)



    def close_window(self):
        self.master.destroy()


# Создание главного окнка
root = tk.Tk()
app = App(root)

# Запуск главного окна в бесконечном цикле
root.mainloop()