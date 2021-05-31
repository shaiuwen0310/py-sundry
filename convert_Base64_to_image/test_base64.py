import base64

def img_to_base64(imgName, base64TXT):
    with open(imgName, "rb") as f:
        base64_data = base64.b64encode(f.read()).decode('ascii')
    f = open(base64TXT, "w")
    f.write(base64_data)
    f.close()


def base64_to_img(base64TXT, imgName):
    file = open(base64TXT, 'rb').read()

    decodeit = open(imgName, 'wb')
    decodeit.write(base64.b64decode((file)))
    decodeit.close()


if __name__ == '__main__':

    img_to_base64('DSC00375.JPG', 'DSC00375.txt')

    base64_to_img('DSC00375.txt', 'DSC00375.JPG')