class Les:
    def __init__(self, tamanho):
        self.tam = tamanho
        self.quant = 0
        self.vetor = [None] * self.tam

    def inserir_inicio(self, valor):
        for i in range(self.quant, 0 , -1):
            self.vetor[i] = self.vetor[i - 1]
        self.vetor[0] = valor
        self.quant += 1

    def remover_inicio(self):
        for i in range(self.quant - 1):
            self.vetor[i] = self.vetor[i + 1]
        self.quant -= 1

    def show(self):
        for i in range(self.quant):
            print(self.vetor[i])

    def esta_cheia(self):
        return self.quant == self.tam

    def inserir_apos(self, ValorApos, ValorAntes):    
        for i in range(self.quant, -1, -1):
            if self.vetor[i] == ValorAntes and i< self.quant:
                for j in range(self.quant, i, -1):
                    self.vetor[j] = self.vetor[j- 1]
                self.vetor[i + 1] = ValorApos
        self.quant += 1   
            
            

    def inserir_antes(self, valorApos, valorAntes):
        for i in range(self.quant, -1, -1):
            if self.vetor[i] == valorAntes and i < self.quant:
                for j in range(self.quant, i, -1):
                    self.vetor[j] = self.vetor[j - 1]
                self.vetor[i] = valorApos
        self.quant += 1
        
        


    def remover_fim(self):
        self.quant -= 1

    def inserir_fim(self, valor):
        self.vetor[self.quant] = valor
        self.quant += 1

    def get_prim(self):
        return self.vetor[0]
