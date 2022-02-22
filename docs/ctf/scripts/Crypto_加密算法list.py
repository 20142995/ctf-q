from Crypto.Util.Padding import pad
# pad(b'data', 16)


def pcap_find_sql():
    #请先将pcapng包另存为pcap
    keystr=r'.php?id=1%27and%20(select%20ascii(substr((select%20skyflag_is_here2333%20from%20flag%20limit%200,1),{0}'
     
    l=[None]*33
     
    with open(r'C:\Users\Crazy\Desktop\2.pcap','r',encoding='ISO-8859-1') as f:
        for i in f.readlines():
            for j in range(1,34,1):
                if keystr.format(j)+',' in i:
        
                    tmp=i
                    l[j-1]=tmp.split("=")[-1]
    for i in l:
        tmp=i.split(r'%23')[0]
        print (chr(int(tmp)),end='')


def fence():
    #!/usr/bin/env python
    # -*- encoding: utf-8 -*-
     
     
    string = input("输入:")
    frequency = [] # 获得栅栏的栏数
    result_len = len(string)        # 栅栏密码的总长度  25
    for i in range(2, result_len):   # 最小栅栏长度为2   逐个测试2,3,4....
        if(result_len % i == 0):        # 当栅栏密码的总长度 模 i 余数为0  则这个i就是栅栏密码的长度
            frequency.append(i)
     
    for numberOfColumn in frequency:   # 循环可能分的栏数
        RESULT = []                 #  保存各栏数的结果
        for i in range(numberOfColumn):     #   i : 开始取值的位置
            for j in range(i, result_len, numberOfColumn):  # 开始取值， 隔栏数取一个值， 起始位置是i
                RESULT.append(string[j])
        print("".join(RESULT))


def bacon():

    letters1 = [


        'A', 'B', 'C', 'D', 'E', 'F', 'G',
        'H', 'I', 'J', 'K', 'L', 'M', 'N',
        'O', 'P', 'Q', 'R', 'S', 'T',
        'U', 'V', 'W', 'X', 'Y', 'Z',
    ]
    letters2 = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g',
        'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't',
        'u', 'v', 'w', 'x', 'y', 'z',
    ]
    cipher1 = [
        "aaaaa", "aaaab", "aaaba", "aaabb", "aabaa", "aabab", "aabba",
        "aabbb", "abaaa", "abaab", "ababa", "ababb", "abbaa", "abbab",
        "abbba", "abbbb", "baaaa", "baaab", "baaba", "baabb",
        "babaa", "babab", "babba", "babbb", "bbaaa", "bbaab",
    ]
    cipher2 = [
        "AAAAA", "AAAAB", "AAABA", "AAABB", "AABAA", "AABAB", "AABBA",
        "AABBB", "ABAAA", "ABAAA", "ABAAB", "ABABA", "ABABB", "ABBAA",
        "ABBAB", "ABBBA", "ABBBB", "BAAAA", "BAAAB", "BAABA",
        "BAABB", "BAABB", "BABAA", "BABAB", "BABBA", "BABBB",
    ]
     
     
    def bacon1(string):
        lists = []
        # 分割，五个一组
        for i in range(0, len(string), 5):
            lists.append(string[i:i+5])
        # print(lists)
        # 循环匹配，得到下标，对应下标即可
        for i in range(0, len(lists)):
            for j in range(0, 26):
                if lists[i] == cipher1[j]:
                    # print(j)
                    print(letters1[j], end="")
        print("")
     
     
    def bacon2(string):
        lists = []
        # 分割，五个一组
        for i in range(0, len(string), 5):
            lists.append(string[i:i+5])
        # print(lists)
        # 循环匹配，得到下标，对应下标即可
        for i in range(0, len(lists)):
            for j in range(0, 26):
                if lists[i] == cipher2[j]:
                    # print(j)
                    print(letters2[j], end="")
        print("")

def rot5(txt):
    rot13 = str.maketrans(
        '0123456789',
        '5678901234')
    return txt.translate(rot13)


def rot13_1():
    rot13 = str.maketrans(
        'ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz',
        'NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm')
    'Hello World!'.translate(rot13)
    # 'Uryyb Jbeyq!'


def rot13_2():
    import codecs
    codecs.encode('foobar', 'rot_13')


def hmac_encrypt():
    import hmac
    import hashlib

    str_encrypt = "hello！"
    key = "abc"
    # 第一个参数是密钥key，第二个参数是待加密的字符串，第三个参数是hash函数

    mac = hmac.new(key.encode(encoding="utf-8"), str_encrypt.encode("utf8"), hashlib.md5)

    value = mac.hexdigest()  # 加密后字符串的十六进制格式

    # 十六进制
    print("十六进制的字符串", value)


def des_encrypt():
    from Crypto.Cipher import DES
    import binascii

    # DES加密数据的长度须为8的的倍数，不够可以用其它字符填充
    text = 'Welcome to DES'
    if len(text) % 8 != 0:
        text = text + "+" * (8 - len(text) % 8)
    # 密钥：必须为8字节
    key = b'12345678'
    # 使用 key 初始化 DES 对象，使用 DES.MODE_ECB 模式
    des = DES.new(key, DES.MODE_ECB)
    # 加密
    result = des.encrypt(text.encode())

    print('加密后的数据：', result)
    # 转为十六进制    binascii 的 b2a_hex 或者 hexlify 方法
    print('转为十六进制：', binascii.b2a_hex(result))
    # 解密
    print('解密后的数据：', des.decrypt(result))



def aes_encrypt_ecb0():
    from Crypto.Cipher import AES
    from binascii import b2a_hex, a2b_hex
    mode = AES.MODE_ECB
    key = b'\xcb\x8d\x49\x35\x21\xb4\x7a\x4c\xc1\xae\x7e\x62\x22\x92\x66\xce'
    text = b'\xBC\x0A\xAD\xC0\x14\x7C\x5E\xCC\xE0\xB1\x40\xBC\x9C\x51\xD5\x2B\x46\xB2\xB9\x43\x4D\xE5\x32\x4B\xAD\x7F\xB4\xB3\x9C\xDB\x4B\x5B'
    cryptos = AES.new(key, mode)
    cipher_text = cryptos.decrypt(text)
    print(cipher_text)
    #b'flag{924a9ab2163d390410d0a1f670}'


def aes_encrypt_ecb():
    # ECB加密模式
    import base64
    from Crypto.Cipher import AES
    # 使用补0方法
    # # 需要补位，补足为16的倍数
    def add_to_16(s):
        while len(s) % 16 != 0:
            s += '\0'
        return str.encode(s)  # 返回bytes

    # 密钥长度必须为16、24或32位，分别对应AES-128、AES-192和AES-256
    key = 'abc4567890abc458'
    # 待加密文本
    text = 'hello'
    # 初始化加密器
    aes = AES.new(add_to_16(key), AES.MODE_ECB)
    # 加密
    encrypted_text = str(base64.encodebytes(aes.encrypt(add_to_16(text))), encoding='utf8').replace('\n', '')
    # 解密
    decrypted_text = str(
        aes.decrypt(base64.decodebytes(bytes(encrypted_text, encoding='utf8'))).rstrip(b'\0').decode("utf8"))

    print('加密值：', encrypted_text)
    print('解密值：', decrypted_text)


def aes_encrypt_cbc_pkcs7():
    from cryptography.hazmat.primitives import padding
    from cryptography.hazmat.primitives.ciphers import algorithms
    from Crypto.Cipher import AES
    from binascii import b2a_hex, a2b_hex
    import json

    '''
    AES/CBC/PKCS7Padding 加密解密
    环境需求:
    pip3 install pycryptodome==3.9.0

    '''

    class PrpCrypt(object):

        def __init__(self, key='0000000000000000'):
            # self.key = key.encode('utf-8')
            self.key = b'1234123412ABCDEF'
            self.mode = AES.MODE_CBC
            self.iv = b'ABCDEF1234123412'
            # block_size 128位

        # 加密函数，如果text不足16位就用空格补足为16位，
        # 如果大于16但是不是16的倍数，那就补足为16的倍数。
        def encrypt(self, text):
            cryptor = AES.new(self.key, self.mode, self.iv)
            text = text.encode('utf-8')

            # 这里密钥key 长度必须为16（AES-128）,24（AES-192）,或者32 （AES-256）Bytes 长度
            # 目前AES-128 足够目前使用

            text = self.pkcs7_padding(text)

            self.ciphertext = cryptor.encrypt(text)

            # 因为AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题
            # 所以这里统一把加密后的字符串转化为16进制字符串
            return b2a_hex(self.ciphertext).decode().upper()

        @staticmethod
        def pkcs7_padding(data):
            if not isinstance(data, bytes):
                data = data.encode()

            padder = padding.PKCS7(algorithms.AES.block_size).padder()

            padded_data = padder.update(data) + padder.finalize()

            return padded_data

        @staticmethod
        def pkcs7_unpadding(padded_data):
            unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
            data = unpadder.update(padded_data)

            try:
                uppadded_data = data + unpadder.finalize()
            except ValueError:
                raise Exception('无效的加密信息!')
            else:
                return uppadded_data

        # 解密后，去掉补足的空格用strip() 去掉
        def decrypt(self, text):
            #  偏移量'iv'
            cryptor = AES.new(self.key, self.mode, self.iv)
            plain_text = cryptor.decrypt(a2b_hex(text))
            # return plain_text.rstrip('\0')
            return bytes.decode(plain_text).rstrip("\x01"). \
                rstrip("\x02").rstrip("\x03").rstrip("\x04").rstrip("\x05"). \
                rstrip("\x06").rstrip("\x07").rstrip("\x08").rstrip("\x09"). \
                rstrip("\x0a").rstrip("\x0b").rstrip("\x0c").rstrip("\x0d"). \
                rstrip("\x0e").rstrip("\x0f").rstrip("\x10")

        def dict_json(self, d):
            '''python字典转json字符串, 去掉一些空格'''
            j = json.dumps(d).replace('": ', '":').replace(', "', ',"').replace(", {", ",{")
            return j

    # 加解密
    if __name__ == '__main__':
        import json
        pc = PrpCrypt()  # 初始化密钥
        a = "0d2fd588668054da021349541e5cb64f55979d02e41c75e0ce0233f6d10e31251b40cb8e197404f9e261fba573e09191"
        b = pc.decrypt(a)
        print(b)


def aes_encrypt_cbc1():
    # CBC加密模式
    import base64
    from Crypto.Cipher import AES
    from urllib import parse
    AES_SECRET_KEY = 'helloBrook2abcde'  # 此处16|24|32个字符
    IV = 'helloBrook2abcde'
    # padding算法
    BS = len(AES_SECRET_KEY)
    # 填充方案
    pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
    # 解密时删除填充的值
    unpad = lambda s: s[0:-ord(s[-1:])]

    def cryptoEn(string, key, iv):
        # param string: 原始数据
        # param key: 密钥
        # param iv: 向
        mode = AES.MODE_CBC
        cipher = AES.new(key.encode("utf8"), mode, iv.encode("utf8"))
        encrypted = cipher.encrypt(bytes(pad(string), encoding="utf8"))
        return base64.b64encode(encrypted).decode("utf-8")

    # CBC模式的解密代码
    def cryptoDe(destring, key, iv):
        # param destring: 需要解密的数据
        # param key: 密钥
        # param iv: 向量
        mode = AES.MODE_CBC
        decode = base64.b64decode(destring)
        cipher = AES.new(key.encode("utf8"), mode, iv.encode("utf8"))
        decrypted = cipher.decrypt(decode)
        return unpad(decrypted).decode("utf-8")

    secret_str = cryptoEn('hello', AES_SECRET_KEY, IV)
    print(secret_str)
    clear_str = cryptoDe(secret_str.encode("utf8"), AES_SECRET_KEY, IV)
    print(clear_str)


def aes_encrypt_cbc2():
    import base64
    from Crypto.Cipher import AES
    from urllib import parse

    AES_SECRET_KEY = 'helloBrook2abcde'  # 此处16|24|32个字符
    IV = 'helloBrook2abcde'

    # padding算法
    BS = len(AES_SECRET_KEY)
    pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
    unpad = lambda s: s[0:-ord(s[-1:])]

    class AES_ENCRYPT(object):
        def __init__(self):
            self.key = AES_SECRET_KEY
            self.mode = AES.MODE_CBC

        # 加密函数
        def encrypt(self, text):
            cryptor = AES.new(self.key.encode("utf8"), self.mode, IV.encode("utf8"))
            self.ciphertext = cryptor.encrypt(bytes(pad(text), encoding="utf8"))
            # AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题，使用base64编码
            return base64.b64encode(self.ciphertext).decode("utf-8")

        # 解密函数
        def decrypt(self, text):
            decode = base64.b64decode(text)
            cryptor = AES.new(self.key.encode("utf8"), self.mode, IV.encode("utf8"))
            plain_text = cryptor.decrypt(decode)
            return unpad(plain_text).decode("utf-8")

    if __name__ == '__main__':
        aes_encrypt = AES_ENCRYPT()
        text = "Python中中"
        # 如果字符串包含中文，先对文本转ascii码，将支持中文加密
        is_unicode = any(ord(c) > 255 for c in text)
        text = base64.b64encode(text.encode('utf-8')).decode('ascii') if is_unicode else text
        e = aes_encrypt.encrypt(text)
        d = aes_encrypt.decrypt(e)
        d = base64.b64decode(text.encode()).decode('utf8') if is_unicode else d
        print(text)
        print(e)
        print(d)


def rc4(data, key):
    # https://code.activestate.com/recipes/576736-rc4-arc4-arcfour-algorithm/
    x = 0
    box = list(range(256))
    for i in range(256):
        x = (x + box[i] + ord(key[i % len(key)])) % 256
        box[i], box[x] = box[x], box[i]
    x = 0
    y = 0
    out = []
    for char in data:
        x = (x + 1) % 256
        y = (y + box[x]) % 256
        box[x], box[y] = box[y], box[x]
        out.append(chr(ord(char) ^ box[(box[x] + box[y]) % 256]))

    return ''.join(out)

    if __name__ == '__main__':
        key = '12345678abcdefghijklmnopqrspxyz'
        data = b'\xc2\xbc\xc3\x85\x12}\xc2\x85#\xc2\x84q{9(\x02\xc3\x93Q\xc3\xb3,\xc2\x89+\xc2\xa6,\xc2\xaf\t'.decode()
        print(rc4(data, key))

def openssl_aes_256_cbc():
    # echo -n 'Hello World!' | openssl aes-256-cbc -e -a -salt -pbkdf2 -iter 10000 -k 123
    import binascii
    import base64
    import hashlib
    from Crypto.Cipher import AES  # requires pycrypto

    # inputs
    openssloutputb64 = 'U2FsdGVkX1+QwThiBeTj7Fy/Foqq8kypIAzBtDwBVxo='
    password = '123'
    pbkdf2iterations = 10000

    # convert inputs to bytes
    openssloutputbytes = base64.b64decode(openssloutputb64)
    passwordbytes = password.encode('utf-8')

    # salt is bytes 8 through 15 of openssloutputbytes
    salt = openssloutputbytes[8:16]

    # derive a 48-byte key using pbkdf2 given the password and salt with 10,000 iterations of sha256 hashing
    derivedkey = hashlib.pbkdf2_hmac('sha256', passwordbytes, salt, pbkdf2iterations, 48)

    # key is bytes 0-31 of derivedkey, iv is bytes 32-47 of derivedkey
    key = derivedkey[0:32]
    iv = derivedkey[32:48]

    # ciphertext is bytes 16-end of openssloutputbytes
    ciphertext = openssloutputbytes[16:]

    # decrypt ciphertext using aes-cbc, given key, iv, and ciphertext
    decryptor = AES.new(key, AES.MODE_CBC, iv)
    plaintext = decryptor.decrypt(ciphertext)

    # remove PKCS#7 padding.
    # Last byte of plaintext indicates the number of padding bytes appended to end of plaintext.  This is the number of bytes to be removed.
    plaintext = plaintext[:-plaintext[-1]]

    # output results
    print('openssloutputb64:', openssloutputb64)
    print('password:', password)
    print('salt:', salt.hex())
    print('key: ', key.hex())
    print('iv: ', iv.hex())
    print('ciphertext: ', ciphertext.hex())
    print('plaintext: ', plaintext.decode('utf-8'))


if __name__ == '__main__':
    # hmac_encrypt()
    # des_encrypt()
    # aes_encrypt_ecb()
    # aes_encrypt_cbc1()
    aes_encrypt_cbc2()
    # rc4()
