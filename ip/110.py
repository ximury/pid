import datetime
import socket
import time

server_ip = '192.168.17.161'
# socket.setdefaulttimeout(2)
while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    print(s.gettimeout())
    try:
        # 只能检测端口使得否开启，不能检测网络断开，若是开启状态中，网络中断，状态不变
        # s.settimeout(2000)
        status = s.connect_ex((server_ip, 22))
        time.sleep(1)
        print('status: ', status, 'time: ', datetime.datetime.now())
        if status != 0:
            # s.close()
            print('Port is Not Open')
            # break
    except Exception as e:
        print(e)
    s.close()
