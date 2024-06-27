class Bicicleta:
    def __init__(self, cor, modelo, ano, valor ):
        self.cor = cor
        self.modelo = modelo
        self.ano= ano
        self.valor= valor 

    def buzinar(self):
        print("plim plim..")

    def parar(self):
        print("parando bicicleta....")
        print(" bicicleta parada!")

    def correr (self):
        print("vrummmm..")

   # def __str___(self):
    #    return  f"bicicleta : {self.cor},{self.modelo},{self.ano} "
        
        def __str__(self):
            return  f"{self. __class__.__name__}: {[[f'{chave} = {valor}' for chave,valor in self. __dict__.items()]]}"

caloi= Bicicleta(" vermelha", "caloi", 2022, 600)

caloi.buzinar()
caloi.correr()
caloi.parar()

print(caloi.cor, caloi.modelo,caloi.ano, caloi.valor)

b1= Bicicleta("verde", "monark", 2000,500)
Bicicleta.buzinar(b1)
print(b1.cor)