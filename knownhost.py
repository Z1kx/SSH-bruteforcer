import paramiko

def main():
    ip="127.0.0.1"
    user="test"
    password="aaah"
    timeout=5

    ssh_client=paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(ip,username=user,password=password,timeout=timeout)
    print(ssh_client)

if __name__ == '__main__':
    main()