
class Output():
    def __init__(self):
        self._types = {'bin' : Bin(), 'hex' : Hex(), 'oct' : Oct()}
        self._num = None
        self.setNum()

    def setNum(self):
        tmp_val = int(input('Enter the number:\n'))
        tmp_type = input('Enter type of number (bin, oct, hex, dec = default)\n')
        if (tmp_val == '')

        if (tmp_val >= 0) and (tmp_val <=9):
            if (tmp_type in self._types):
                self._num = self._types[tmp_type]
            else:
                raise ValueError
        else:
            raise ValueError


    def getNum(self):
        self._num.getNum()


class Number():
    def __init__(self):
        self._value = None
        self._type = None



    def setNum(self):


    def getNum(self):
        self._type.getNum(self._value)


class Bin(Number):
    def getNum(self, value):
        print(bin(value))


class Hex(Number):
    def getNum(self, value):
        print(hex(value))


class Oct(Number):
    def getNum(self, value):
        print(oct(value))


if __name__ == '__main__':
    out = Output()
