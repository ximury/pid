import socket
import threading
import time

server_ip = '192.168.17.5'


class CheckNetworkThread(threading.Thread):
    """
    客户端网络断开，远程连接断开的处理逻辑
    """

    def __init__(self, ):
        threading.Thread.__init__(self)

    def run(self):
        while True:
            # socket.AF_INET, socket.SOCK_DGRAM
            # socket.AF_INET,socket.SOCK_STREAM
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # time.sleep(1)
            try:
                # 只能检测端口使得否开启，不能检测网络断开，若是开启状态中，网络中断，状态不变
                # s.settimeout(2000)
                status = s.connect_ex((server_ip, 5901))
                if status != 0:
                    s.close()
                    print('Port is Not Open')
            except Exception as e:
                print(e)


if __name__ == '__main__':
    check_network_status = CheckNetworkThread()
    check_network_status.run()
