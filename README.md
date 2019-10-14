# python-websocket-client
python 订阅websocket消息

## 需要用到的类
python -m pip install websocket-client

### 步骤详解
```python
# -*- coding: utf-8 -*-#

#------------------------------------
# Name:         connect
# Description:  
# Author:       kingming
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
   
# 长连接关键方法：ws.run_forever(ping_interval=60,ping_timeout=5)
# 如果不断开关闭websocket连接，会一直阻塞下去。另外这个函数带两个参数，如果传的话，启动心跳包发送。
# ping_interval:自动发送“ping”命令，每个指定的时间(秒),如果设置为0，则不会自动发送。
# ping_timeout:如果没有收到pong消息，则为超时(秒)。
# ping_interval心跳发送间隔时间
# ping_timeout 设置，发送ping到收到pong的超时时间
# 我们看源代码，会发现这样一断代码：ping的超时时间，要大于ping间隔时间
