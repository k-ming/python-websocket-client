# python-websocket-client
python 订阅websocket消息

## 需要用到的类
python -m pip install websocket-client

### 步骤详解
'''python
# -*- coding: utf-8 -*-#

#------------------------------------
# Name:         connect
# Description:  
# Author:       17621158197
# Date:         2019/10/11
#------------------------------------

import websocket
# try:
#     import thread #thread类再python3中已经启用，为了兼容用 _thread替代
# except ImportError:
#     import _thread as thread
import time
import threading



def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")


def on_open(ws):
    def run(*args):
        ws.send("")
        time.sleep(1)
        # ws.close()
    # thread.start_new_thread(run,())
    thread = threading.Thread(target=run())
    thread.start()

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://10.7.5.88:8089/gs-robot/notice/status",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever(ping_interval=60, ping_timeout=30)
