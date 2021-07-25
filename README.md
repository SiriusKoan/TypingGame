# TypingGame
<img alt="Python" src="https://img.shields.io/badge/python-%2314354C.svg?style=for-the-badge&logo=python&logoColor=white"/>

A simple typing game made with python built-in modules tkinter and socket.  
It is made for CRSC originally.

## Setup
There is no need to install any additional packages.
### Server
Modify the IP address and port in `server.py` and then run it.
```
$ python3 server.py
```
### Client
Modify the IP address and port in `client.py` and run `main.py`
```
$ python3 main.py
```

## Play
There are two modes: `single player` and `multiple players`.  
You have to fill a room_id in the entry before clicking the `multiple players` button.  
The connection will be closed after you close the window, and your competitor will see `No connection now` on the screen, and vice versa.