from subprocess import check_output


def get_pid(name):
    return map(int, check_output(["pidof", name]).split())


if __name__ == '__main__':
    print(list(get_pid('flvrec.py')))
