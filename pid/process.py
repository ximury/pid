import subprocess


def execute_cmd(cmd):
    """执行shell命令"""
    p = subprocess.Popen(cmd, shell=True,
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    if p.returncode != 0:
        return p.returncode, stderr
    return p.returncode, stdout


def get_process_id(name):
    """
    Return process ids found by (partial) name or regex.
    """
    child = subprocess.Popen(['pgrep', '-f', name], stdout=subprocess.PIPE, shell=False)
    response = child.communicate()[0]
    return [int(pid) for pid in response.split()]


if __name__ == '__main__':
    # print(execute_cmd('cd /test'))
    print(execute_cmd('flvrec.py 192.168.240.132:0'))
    print(execute_cmd('flvrec.py 192.168.240.132:1'))
    pid_list = get_process_id('flvrec.py')
    print(pid_list)
