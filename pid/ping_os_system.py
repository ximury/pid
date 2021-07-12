import os
server_ip = '192.168.17.161'

result = os.system('ping -c 2 {}>>/home/wyj/0001/null'.format(server_ip))
# result = os.system('ping -c 2 {}'.format(server_ip))
print(result)
if result:
    print('ping fail')
else:
    print('ping ok')
