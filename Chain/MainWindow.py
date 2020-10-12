from Chain.Widget import Widget


### Zadanie nr 1 jest realizowane przez exit(), poniewaz w przypadku spotkania close kończy działanie

class MainWindow(Widget):

    def handle_close(self, event):
        print(f'MainWindow: {event}')
        exit()

    def handle_default(self, event):
        print(f'MainWindow Default: {event}')
