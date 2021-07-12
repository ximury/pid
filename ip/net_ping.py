import subprocess
import time
from subprocess import run, PIPE, Popen

cnt = 1
server_ip = '192.168.17.58'


def execute_cmd(cmd):
    """执行shell命令"""
    p = subprocess.call(cmd, shell=True,
                        # stdin=subprocess.PIPE,
                        # stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE
                        )
    # stdout, stderr = p.communicate()
    print(p.numerator)
    # if p.returncode != 0:
    #     return p.returncode, stderr
    # return p.returncode, stdout


while 0:
    print("8888")
    r = subprocess.Popen('ping 192.168.17.5',
                         stdout=PIPE,
                         stderr=PIPE,
                         stdin=PIPE,
                         shell=False)
    print(r.returncode)
    if r.returncode:
        print('relogin 第{}次'.format(cnt))
        cnt += 1
    else:
        print('正常联网')
    time.sleep(1)

while True:
    print('---')
    print(execute_cmd('ping -c 3 {}'.format(server_ip)))
