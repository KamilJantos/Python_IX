from Chain.Widget import Widget


class SendDialog(Widget):
    def handle_paint(self, event):
        print(f'SendDialog: {event}')
