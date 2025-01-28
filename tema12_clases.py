class OperasBas:
    #declaracion de propeidadess de clases
    num1=0;
    num2=0;
    num3=0;

    #declaracion de constructor de la clase this
    def __init__(self,a,b):
        self.num1=a
        self.num2=b

    def suma(self):
        self.res=self.num1+self.num2
        print("La suma es:{}".format(self.res))


def main():
    obj=OperasBas(3,5)
    obj.suma()

if __name__=="__main__":
    main()
    #declaracion de metodos de la clase