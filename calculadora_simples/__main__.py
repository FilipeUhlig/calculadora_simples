import es

def main():
    #Atribuição de variáveis
    numeros = []
    soma = 0
    vezes = 0
    divisao = 0
    menos = 0
    calc = 0
    
    #Entrada de dados 
    numeros = es.leitora_numeros()
    calc = es.leitora_calc()
    
    # Processamento de dados
    if calc == "+":      ##Calculando
        import adicao 
        op = adicao.soma(numeros[0],numeros[1])
        fun = "soma"
    
    
    elif calc == "-":
        import subtracao
        op = subtracao.menos(numeros[0],numeros[1])
        fun = "subtração"
    
    elif calc == "/" and numeros[1] != 0:
        import divisao
        op = divisao.divisao(numeros[0],numeros[1])
        fun = "divisão"
       
    
    elif calc == "*":
        import multiplicacao
        op = multiplicacao.vezes(numeros[0],numeros[1])
        fun = "multiplicação"
        
    else:
        print("Você digitou uma operação inválida.")
          
    #Saida de dados
    
    if calc == "+" or calc == "-" or (calc == "/" and numeros[1] !=0) or calc == "*":
        es.escritora_numeros(numeros[0], numeros[1], op, fun)

        
#Invocando main
if __name__ == "__main__":
    main()
    
        