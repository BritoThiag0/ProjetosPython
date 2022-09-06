#Projeto 2
#Contador de palavras de um texto.

texto = '''      Isaias 55.8-13
8 - “Pois os meus pensamentos são muito diferentes dos seus; a minha maneira de agir é muito diferente da sua”, declara o Senhor.
9 - “Porque assim como os céus são mais altos do que a terra, os meus caminhos são mais altos do que os seus caminhos, e os meus pensamentos mais altos que os seus pensamentos.
10 - Como a chuva e a neve caem do céu e não voltam para lá sem regar a terra, fazê-la brotar, produzir e dar semente ao lavrador e pão aos famintos,
11 - assim é a minha palavra. Quando eu falo, ela sempre produz o fruto que desejo, sempre traz o resultado que determinei.
12 - Vocês sairão com alegria, e serão levados de volta à sua terra em paz. Montes e colinas cantarão de alegria à sua volta e todas as árvores do campo baterão palmas enquanto vocês caminharem.
13 - Onde havia espinheiros crescerão ciprestes; onde crescia a roseira brava, crescerá a murta. Isso trará glória ao nome do Senhor e será uma lembrança eterna que nunca desaparecerá”.
'''

#print(texto)

palavra_cont = {}

for palavra in texto.split():
    if palavra in palavra_cont:
        palavra_cont[palavra] += 1
    else:
        palavra_cont[palavra] = 1
    
print(palavra_cont)