from Chain.Event import Event
from Chain.MainWindow import MainWindow
from Chain.MsgText import MsgText
from Chain.SendDialog import SendDialog


def main():
    mw = MainWindow()
    sd = SendDialog(mw)
    msg = MsgText(sd)

    for e in ('down', 'paint', 'unhandled', 'close'):
        evt = Event(e)
        print(f'Sending event -{evt}- to MainWindow')
        mw.handle(evt)
        print(f'Sending event -{evt}- to SendDialog')
        ### zadanie 2
        new_event = Event(input(f'define new event e.g. close'))
        mw.handle(new_event)
        sd.handle(evt)
        print(f'Sending event -{evt}- to MsgText')
        msg.handle(evt)


if __name__ == '__main__':
    main()
