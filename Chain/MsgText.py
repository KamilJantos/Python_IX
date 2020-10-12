from Chain.Widget import Widget


class MsgText(Widget):
    def handle_down(self, event):
        print(f'MsgText: {event}')
