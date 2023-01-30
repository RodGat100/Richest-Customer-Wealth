class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        sumlist = []                        #cria uma lista com somas de cada CPF
        for CPF in accounts:                #loop para cara cada CPF 
            somacontas = 0                  #reseta a somatoria de cada CPF para zero
            for conta in CPF:               #loop para cada conta de um CPF
                somacontas = somacontas + conta     #faz a somatoria das contas
            sumlist.append(somacontas)      # poe na lista a somatória de cada CPF
        return max(sumlist)                 #retorna o maior da lista
