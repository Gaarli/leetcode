# Verificar se tem ciclo, se tiver ciclo, não é feliz. Se chegar em 1, é feliz.
class Solution:
    def isHappy(self, n: int) -> bool:

        seen = set()

        while True:
            aux = str(n)
            
            soma = 0
            for char in aux:
                soma = soma + (int(char))**2

            if soma == 1:
                return True
            elif soma in seen:
                return False

            seen.add(soma)	
            n = soma	
