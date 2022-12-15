class PartidaBolos:
        
    def resultadoPartida(self, partida):
        resultado = 0
        for numero_ronda, ronda in partida.items():
            if numero_ronda == 10:
                if ronda[0] == 10 or (ronda[0]+ronda[1]) == 10:
                    resultado += self.ronda_diez(ronda)
                else:
                    resultado += self.sumarPuntos(partida, numero_ronda, ronda)
            elif ronda[1] == '-': #check for strike
                resultado += self.sumarStrike(partida, numero_ronda, ronda)
            else:
                resultado += self.sumarPuntos(partida, numero_ronda, ronda)
                
        return resultado

    
    def sumarPuntos(self, partida, num_ronda, ronda):
        score = sum(ronda)
        if score == 10: #check for current spare
            return self.sumarSpare(partida, num_ronda)
        else:
            return score 


    def sumarStrike(self, partida, num_ronda, ronda):
        score = 10
        score += partida[num_ronda+1][0]

        second_throw = partida[num_ronda+1][1]
        if  second_throw != '-':
            score += second_throw
        else:
            score += partida[num_ronda+2][0]

        return score

    def sumarSpare(self, partida, num_ronda):
        score = 10
        score += partida[num_ronda+1][0]
        return score

    def ronda_diez(self, ronda):
        return sum(ronda)
