import random as r


class StrEn:

    def __init__(self, string= ''):
        self.ref = {'a':0,'b':1,'c':2,'d': 3, 'e': 4, 'f': 5, 'g': 6,'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm' :12, 'n': 13, 'o': 14, 'p': 15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25,'æ':26,'ø':27,'å':28, 0: 29, 1:30, 2:31, 3:32, 4:33, 5:34, 6:35, 7:36, 8:37, 9:38, ' ':39}
        self.alphabet = 'abcdefghijklmnopqrstuvwxyzæøå0123456789 '

        self.val = []
        for i in range(len(string)):
            self.val += self.ref.get(string[i])

        print(self.val)


t = StrEn('test')
