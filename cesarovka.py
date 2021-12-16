
class Cesar():

    def __init__(self,message,n):
        self.message = message
        self.n = int(n)
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.cifer = ""

    def encode(self):
        self.message = self.message.upper()
        for i in self.message:
            count = 0
            for j in self.alphabet:
                if i == j:
                    self.cifer += self.alphabet[count + self.n]
                    break
                count += 1
        return self.cifer


    def decode(self):
        self.message = ""
        for i in self.cifer:
            count = 0
            for j in self.alphabet:
                if i == j:
                    self.message += self.alphabet[count - self.n]
                    break
                count += 1
        return self.message

    #Tohle nefunguje, jinak fajn
    def decodeAll(self):
        list = []
        for n in range(27):
            if n == 0:
                continue
            self.message = ""
            for i in self.cifer:
                count = 0
                for j in self.alphabet:
                    if i == j:
                        self.message += self.alphabet[count - n]
                        break
                    count += 1
            list.append(self.message)
        return list


#Takhle si definuju main v Pythonu
if __name__ == '__main__':

    print("Zadej zpravu:")
    message = input()
    print("O kolik znaku chces posunout sifru?")
    n = input()
    c = Cesar(message,n)
    print(c.encode())
    print(c.decode())
    print(c.decodeAll())