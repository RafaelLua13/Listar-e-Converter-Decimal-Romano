# Nome do projeto: Listar e Converter Romano Decimal
# Linguagem: Python
# Utilizações: Variáveis, Repetições, Listas e Funções
# Autor: Rafael Lua  - rafaellua13




# Menu
def tabuleiro():
  print("\n********************************")
  print("0 - Sair")
  print("1 - Listar romano de A a B")
  print("2 - Decimal para Romano")
  print("3 - Romano para Decimal")
  print("********************************")


  print("\nDigite a opção desejada :]\n")



# Converter Decimal para Romano
def romanoDecimal(s):

  romano = ["I","V","X","L","C","D","M"]
  valor = [1,5,10,50,100,500,1000]

  soma = 0



  for x in range(len(s)):
    #print(soma)
    if s[x] not in romano:
      soma = 0
      break
    ind = romano.index(s[x])
    
    somar = 0
    if s[x] == "I" or s[x] == "X" or s[x] == "C": 
      
      if x + 1 < len(s) and romano.index(s[x])+2 < len(romano):
     
          if romano.index(s[x+1]) == romano.index(s[x])+1 or romano.index(s[x+1]) == romano.index(s[x])+2:
            soma -= valor[ind]
               
          else:
            somar = 1
      else:
            somar = 1  
    else:
      somar = 1

    if somar == 1:
      soma += valor[ind]


  return soma

# Função converter Romano para Decimal
def decimalRomano(x):
  centena = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
  dezena = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
  unidade = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    
  final = ""
  while x >= 1000:
    x -= 1000
    final += "M"
  

  if x == 0:
    return final
  

  cent = (x - x%100)/100
  dez = (x%100 - x%10)/10
  unid = (x%10)


  final += centena[int(cent)]
  final += dezena[int(dez)]
  final += unidade[int(unid)]

  return final



def main():
  opcList = ["0","1","2","3"]

  while True:
    tabuleiro()

    opc = input("-> ")

    if opc not in opcList:
      print("Opção invalida :)")
    else:
      if opc == opcList[0]: # Sair
        print("\nVolte sempre :D")
        break
      elif opc == opcList[1]: # Listar Romanos

        print("\nListar numeros romanos de A até B:")
        A = input("\nDigite o inicio em decimal: ")
        B = input("Digite o destino em decimal: ")

        invalido = 0
        if A.isnumeric() == True: 
          if B.isnumeric() == True:
            print("\n")
            for num in range(int(A),int(B)+1):
              print(num,"->",decimalRomano(num))
          else:
            invalido = 1
        else:
          invalido = 1
        
        if invalido == 1:
          print("\nFormato Invalido :o")


      elif opc == opcList[2]: # Converter Decimal para Romano
        print("\nConverter decimal em romano (digite menu para voltar):")
        
        while True:

          dec = input("\nDigite o valor em decimal: ")

          if dec.upper() == "MENU":
            break
          else:
            
            
            if dec.isnumeric() == True:
              print("\n")
              if dec > 0:
                print(dec,"=",decimalRomano(int(dec)),"\n\n")
            else:
              print("\nFormato invalido :o")
              break



      elif opc == opcList[3]: # Converter Romano para Decimal
          print("\nConverter romano em decimal (digite menu para voltar) \n")
          while True:
            var = input("Digite o valor em romano: ").upper()

            if var.upper() == "MENU":
              break
            
            soma = romanoDecimal(var)

            print("\n")

            if soma > 0 and decimalRomano(soma) == var:
              print("\n\n",var,"=",soma,"\n\n\n\n")
            else:
              print(var,"= Numero inexistente\n\n\n")



##############
main()
