import os
import subprocess
import sys


def get_process_id(name):
    """
    Return process ids found by (partial) name or regex.
    """
    child = subprocess.Popen(['pgrep', '-f', name], stdout=subprocess.PIPE, shell=False)
    response = child.communicate()[0]
    return [int(pid) for pid in response.split()]


if __name__ == '__main__':
    pid_list = get_process_id('flvrec.py')
    # pid_list = get_process_id('http.server')
    pid_list = get_process_id('ffmpeg')
    # pid_list = get_process_id('SimpleHTTPServer')
    print(pid_list)
    print(pid_list[0])
    print(pid_list[-1])

if __name__ == '__main__':
    name = sys.argv[1]
    print(name)
    pid_list = get_process_id(name)
    print(pid_list)
    print(pid_list[0])
    print(pid_list[-1])
    while(1):
        continue