# -*- coding: utf-8 -*-#
2
3  #------------------------------------
4  # Name:         RosWebsocketTest
5  # Description:  
6  # Author:       17621158197
7  # Date:         2019/10/15
8  #------------------------------------

import websocket
# try:
#     import thread #thread类再python3中已经启用，为了兼容用 _thread替代
# except ImportError:
#     import _thread as thread
import time
import threading
from datetime import datetime

def on_message(ws, message):
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'), message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")


def on_open(ws):
    def run(*args):
        parmas = input('请输入查询接口: \n')
        ws.send(parmas)
        time.sleep(1)
        # ws.close()
    # thread.start_new_thread(run,())
    thread = threading.Thread(target=run())
    thread.start()

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://192.168.50.51:9090",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever(ping_interval=60, ping_timeout=30)