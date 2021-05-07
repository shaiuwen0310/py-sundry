import paramiko

def images_name_on_server():

    hostname = "192.168.101.252"
    username = "ㄎㄎ"
    password = "hihihi"

    commands = [
        "ls /ㄎㄎ/Desktop/file/images",
    ]

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client.connect(hostname=hostname, username=username, password=password, timeout=30)
    except:
        print("Cannot connect to the SSH Server!!!")
        exit()

    try:
        for command in commands:
            stdin, stdout, stderr = client.exec_command(command)
            
            img_name = stdout.read().decode().split("\n") # 範例結果: ['1023315882.jpg', '45new.jpg', 'image21mm.jpg', '']
            print(stderr.read().decode())
            return list(filter(None, img_name))# filter掉''
    finally:
        client.close()
        # 連線完後必須手動刪除變數以釋放資源，若無釋放，執行時容易噴錯誤訊息
        del client, stdin, stdout, stderr

s = images_name_on_server()
print(s) # 範例結果: ['1023315882.jpg', '45new.jpg', 'image21mm.jpg']
