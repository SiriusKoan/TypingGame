from ui import window
from utils import client


def end():
    try:
        client.end()
    except:
        pass
    window.destroy()


if __name__ == "__main__":
    window.protocol("WM_DELETE_WINDOW", end)
    window.mainloop()
