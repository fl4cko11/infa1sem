from itertools import cycle

alp = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

def encode_vijn(text, keytext):
    f = lambda arg: alp[(alp.index(arg[0])+alp.index(arg[1])%33)%33]
    return ''.join(map(f, zip(text, cycle(keytext))))


def decode_vijn(coded_text, keytext):
    f = lambda arg: alp[alp.index(arg[0])-alp.index(arg[1])%33]
    return ''.join(map(f, zip(coded_text, cycle(keytext))))

coded_text=str(input('зашифрованное: '))
keytext=str(input('ключ: '))
print(decode_vijn(coded_text, keytext))