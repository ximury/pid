import process
import sys


def is_defunct(pid, name):
    cmd_str = "ps -aux | grep %s | grep %s | grep -v grep | grep -v python | awk '{print $8}'" % (pid, name)
    output = process.check_output(cmd_str, shell=True)
    # print(output, end='..')
    print(output)
    if output == '':
        return ''
    return output.replace(b'\n', b'').replace(b'\r', b'').replace(b' ', b'')[0]

    # cmd_str = "ps -aux | grep %s | grep %s | grep -v grep | grep -v python" % (pid, name)
    #      p = subprocess.Popen(cmd_str, shell=True, executable='bash')
    # p = subprocess.Popen(cmd_str, shell=True, stdout=subprocess.PIPE)
    # subprocess.getoutput(cmd_str)
    # print(p.communicate()[0], type(p.communicate()[0]))
    # p.wait()

    # subprocess.Popen(['ps', '-aux', '|', 'grep', pid, '|', 'grep', name,
    #                   '|', 'grep', '-v', 'grep', '|', 'grep', '-v', 'python'], stdout=subprocess.PIPE, shell=False)
    # print(p.communicate()[0], type(p.communicate()[0]))


if __name__ == '__main__':
    pid = sys.argv[1]
    name = sys.argv[2]
    out_put = is_defunct(pid, name)
    # print(out_put, type(out_put))
    print(out_put is 'S+')
