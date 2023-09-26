#exercicio-palindromo
"""palavra=input("Digite uma palvra: ")
palavrasemespaco=palavra.replace(" ","")
contador=0
for x in palavrasemespaco:
    if x==len(palavrasemespaco):
        x==len(palavrasemespaco)-1"""
        
#resolucao1 (comparar a primeira letra com a ultima, a segunda com a penultima...)

palavra=input("Digite uma palvra: ")
palavrasemespaco=palavra.replace(" ","")
ultimo=len(palavrasemespaco)-1
for x in range(len(palavrasemespaco)):
    if palavrasemespaco[x]!=palavrasemespaco[ultimo - x]:
        print("nao é um palindromo")
        break
else:
    print("é um palindromo") 
    
#resolucao2 (reverse)

palavra=input("Digite uma palvra: ")
palavrasemespaco=palavra.replace(" ","")
invertida=""
ultimo=len(palavrasemespaco)-1
for x in range(len(palavrasemespaco)):
    invertida= invertida+palavrasemespaco[ultimo-x] #operador de + com 2 strings ele junta essas 2 strings
if palavrasemespaco==invertida:
    print("é um palindromo")
else:
    print("não é um palindromo")
    
#exercicio-palavras longas

readlines le todo o programa e retorna quantas linhas ele tem

texto=open("AULA10-string\\Python.txt","r")
lista=[]
y=0
contador=0
for x in texto.readlines(): 
    x.strip()
    lista=x.split(" ")
    print(x)

    for x in range(len(lista)):
        lista[x]= lista[x].replace(".","")
        lista[x]=lista[x].replace(",","")
        y=len(lista[x])
        if y>=contador:
            contador=y
            maior=lista[x]
print("O maior número de palavras foi: ", contador)
print("A maior palavra foi: ", maior)

texto.close()           
    
#correção
arquivo=open("AULA10-string\\Python.txt","r")
linhas= arquivo.readlines()

max=0
for x in linhas:
    palavras=x.split(" ") #separa as palavras com espaco entre cada letra
    for s in palavras:
        s=s.replace(",","")
        s=s.replace(".","")
        s=s.strip() #tira caracteres do final
        if len(s)>max:
            max=len(s)
print(max)
listamaiores=[]
for x in linhas:
    palavras=x.split(" ") #separa as palavras com espaco entre cada letra
    for s in palavras:
        s=s.replace(",","")
        s=s.replace(".","")
        s=s.strip() #tira caracteres do final
        if len(s)==max:
            listamaiores.append(s)
print(listamaiores)

arquivo.close()

#exercicio-frequencia de palavras

#if dicionario.get(x)==None: (get verifica c tem a palavra no dicionario)
texto=open("AULA10-string\\teste.txt","r")
contador=0
repete={}
for x in texto.readlines():
    lista=x.split(" ")
    print(x)
    for y in lista:  
    #for x in range(len(lista)):
      #  lista[x]=lista[x].replace(",","")
      #  lista[x]=lista[x].replace(".","")
      #  lista[x]=lista[x].lower()
        if  repete.get(y)==None:
            repete[y]=1
        else:
            repete[y]=repete[y]+1
print(repete)

#execicio remover espaço da string
    
    