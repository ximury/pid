from tcping import Ping


def ping_check():
    ping = Ping('192.168.17.161', 80, 5)
    ping.ping(10)

    ret = ping.result.rows
    print(ret)
    for r in ret:
        print(r)

    ret = ping.result.raw
    print(ret)

    ret = ping.result.table
    print(ret)


if __name__ == '__main__':
    ping_check()
