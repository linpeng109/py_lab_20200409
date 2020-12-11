import binascii
import pyDes


class TDes:
    def __init__(self):
        self.secret_key = '12345678'.encode('utf8')

    def des_encrpt(self, str):
        key = pyDes.des(self.secret_key, pyDes.triple_des, pad=None, padmode=pyDes.PAD_PKCS5)
        en = key.encrypt(str.encode('utf8'), padmode=pyDes.PAD_PKCS5)
        return binascii.b2a_base64(en)

    def des_descrpt(self, str):
        key = pyDes.des(self.secret_key, pyDes.triple_des, pad=None, padmode=pyDes.PAD_PKCS5)
        de = key.decrypt(binascii.a2b_base64(str))
        return de


if __name__ == '__main__':
    tdes = TDes()
    en = tdes.des_encrpt('abcdefghklmnopqrst')
    print('en=%s' % en)
    de=tdes.des_descrpt(en)
    print('de=%s' % de)
