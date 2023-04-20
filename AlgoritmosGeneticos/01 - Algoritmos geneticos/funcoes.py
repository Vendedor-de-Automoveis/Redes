

#                   """""""""""""""""""""""""""""""""""""
#                   """          Importações          """
#                   """""""""""""""""""""""""""""""""""""

import random
import itertools



#                   """""""""""""""""""""""""""""""""""""
#                   """ Funções algorítimos genéticos """
#                   """""""""""""""""""""""""""""""""""""
    
    
#############################################################################
' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Experimento A.01 ~~~~~~~~~~~~~~~~~~~~~~~~~~~ '
#############################################################################

def func_objetivo_cb(indv):
    '''Computa uma métrica do objetivo do problema.
    
    Args:
    indv: uma lista que contém os genes, indivíduo
    
    return:
        soma dos genes dos indivíduos.
    '''
    return sum(indv)


def func_gene_cb():
    '''Gera um gene válido para o problema das caixas binárias.
    
    
    return:
        um valor 0 ou 1.
    '''
    lista = [0, 1]
    gene = random.choice(lista)
    return gene
    
    
def func_indviduo_cb(n):
    '''Gera um indíviduo para o problema.
    
    Args:
    n: numero de genes do indivíduo
    
    return:
        Uma lista com n genes. cada gene é um valor 0 ou 1.
    '''
    indv = []
    for i in range(n):
        gene = func_gene_cb()
        indv.append(gene)
    return indv


#############################################################################
' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Experimento A.03 ~~~~~~~~~~~~~~~~~~~~~~~~~~~ '
#############################################################################

def func_populacao_cb(TAMANHO_POP, n):
    '''Cria uma população para o problema das caixas binárias
    
    Args:
    TAMANHO_POP: tamanho da população
    NUM_GENES: numero de genes
    NUM_GERACOES: numero de geraçõe
    
    return:
        Uma lista onde cada item é um indivíduo. Indivíduo é um conjunto de genes
    '''
    populacao = []
    for _ in range(TAMANHO_POP):
        populacao.append(func_indviduo_cb(n))
    return populacao
                         

def func_selecao_roleta_max(populacao, fitness):
    '''Seleciona individuos para uma população usando o método de roleta.
    
    Args:
    populacao: lista com todos os indivídos de uma popuplção
    fitness: valor da funcao objetivo dos indiviuos da população (score)
    
    Nota: Apenas funciona para problemas de maximização
    
    return:
        População' dos indivíduos selecionados
        
    '''
    populacao_selecionada = random.choices(populacao, weights=fitness, k=len(populacao))
    return populacao_selecionada
                                                                            
                                           
def func_objetivo_pop_cb(populacao):
    '''Calcula a funcao objetivo para todos os indivíduos de uma população.
    
    Args:
    populacao: lista com todos os indivídos de uma popuplção
    
    retun:
        Lista de valores representando a fitness de cada  indivíduo da população
        
    '''
    fitness = []
    for indv in populacao:
        fobj = func_objetivo_cb(indv)
        fitness.append(fobj)
    return fitness


def func_cruzamento_ponto_simples(pai, mae):
    '''Operador de cruzamento de ponto simples.
    
    Args:
    pai: uma lista reperesentando um individuo
    mae: uma lista representando um outro individuo
    
    return:
        Duas listas, sendo que cada uma representa um filho do pais que foram argumentos.
    '''
    
    ponto_de_corte = random.randint(1, len(pai) - 1)
    
    filho1 = pai[:ponto_de_corte] + mae[ponto_de_corte:]
    filho2 = mae[:ponto_de_corte] + pai[ponto_de_corte:]
    
    return filho1, filho2
    
def func_mutacao_cb(indv):
    '''Realiza a mutacao de um gene no problema das caixas binárias
    
    Args:
    indv: uma lista que contém os genes, indivíduo
    
    return:
        Um indivíduo com o gene mutado.
    '''
    
    gene_a_ser_mutado = random.randint(0, len(indv)-1)
    indv[gene_a_ser_mutado] = func_gene_cb()
    return indv



#############################################################################
' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Experimento A.04 ~~~~~~~~~~~~~~~~~~~~~~~~~~~ '
#############################################################################

def func_gene_cnb(valor_max_caixa_cnb):
    '''Gera um gene válido para o problema das caixas não binárias.
    
    Args:
    valor_max_caixa_cnb:valor máximo que a caixa pode assumir
    
    return:
        um valor entre 0 e 'valor_max_caixa_cnb' (incluso).
    '''
    gene = random.randint(0, valor_max_caixa_cnb)
    return gene
    
    
def func_indviduo_cnb(n, valor_max_caixa_cnb):
    '''Gera um indíviduo para o problema das caixas não binárias.
    
    Args:
    n: numero de genes do indivíduo
    valor_max_caixa_cnb: valor máximo que a caixa pode assumir
    
    return:
        Uma lista com n genes. cada gene é um valor entre 0 e 'valor_max_caixa_cnb' (incluso)
    '''
    indv = []
    for _ in range(n):
        gene = func_gene_cnb(valor_max_caixa_cnb)
        indv.append(gene)
    return indv

def func_populacao_cnb(TAMANHO_POP, n, valor_max_caixa_cnb):
    '''Cria uma população para o problema das caixas não binárias
    
    Args:
    TAMANHO_POP: tamanho da população
    NUM_GENES: numero de genes
    valor_max_caixa_cnb: valor máximo que a caixa pode assumir

    
    return:
        Uma lista onde cada item é um indivíduo. Indivíduo é um conjunto de genes
    '''
    populacao = []
    for _ in range(TAMANHO_POP):
        indv= func_indviduo_cnb(n, valor_max_caixa_cnb)
        populacao.append(indv)
    return populacao
                                                                        
                     
def func_objetivo_cnb(indv):
    '''Computa uma métrica do objetivo do problema das caixas não binárias.
    
    Args:
    indv: uma lista que contém os genes, indivíduo
    
    return:
        soma dos genes dos indivíduos.
    '''
    fitness = sum(indv)
    return fitness

    
def func_objetivo_pop_cnb(populacao):
    '''Calcula a funcao objetivo para todos os indivíduos de uma população no problema das caixas não binárias.
    
    Args:
    populacao: lista com todos os indivídos de uma popuplção
    
    retun:
        Lista de valores representando o fitness de cada indivíduo da população.
        
    '''
    fitness_pop = []
    for indv in populacao:
        fobj = func_objetivo_cnb(indv)
        fitness_pop.append(fobj)
    return fitness_pop

def func_mutacao_cnb(indv, valor_max_caixa_cnb):
    '''Realiza a mutacao de um gene no problema das caixas não binárias
    
    Args:
    indv: uma lista que contém os genes, indivíduo
    valor_max_caixa_cnb: valor máximo que a caixa pode assumir
    
    return:
        Um indivíduo com o gene mutado.
    '''
    
    gene_a_ser_mutado = random.randint(0, len(indv)-1)
    indv[gene_a_ser_mutado] = func_gene_cnb(valor_max_caixa_cnb)
    return indv



#############################################################################
' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Experimento A.05 ~~~~~~~~~~~~~~~~~~~~~~~~~~~ '
#############################################################################

"""
testes iniciais

def funca_converte_senha_txt(senha):
    '''Converte a senha textual em valores numéricos reais
    #vou utilizar '0' como sendo separador de algarismo, visto que o alfabeto tem 27 letras e pode ser necessário utilizar um número com dezena para representar uma única letra.
    
    Args:
    senha: a senha correta
    
    return:
        Uma senha numérica
    
    '''

    for caractere in senha:
        numero = ord(caractere)
        print(f"O caractere '{caractere}' converte para o número {numero}")

def func_objetivo_senha_txt():
    '''Computa uma métrica do problema da senha semi-secreta textual

    Args:
    senha-indv: senha-individuo, um conjunto de genes representando o palpite da senha
    senha: a senha correta
    
    return:
        A distância entre a senha correta e a senha-individuo
    '''
"""

def individuo_senha(tamanho_senha, letras):
    """Cria um candidato para o problema da senha
    Args:
      tamanho_senha: inteiro representando o tamanho da senha.
      letras: letras possíveis de serem sorteadas.
    Return:
      Lista com n letras
    """

    candidato = []

    for n in range(tamanho_senha):
        candidato.append(gene_letra(letras))

    return candidato

def gene_letra(letras):
    """Sorteia uma letra.
    Args:
      letras: letras possíveis de serem sorteadas.
    Return:
      Retorna uma letra dentro das possíveis de serem sorteadas.
    """
    letra = random.choice(letras)
    return letra

def populacao_inicial_senha(tamanho, tamanho_senha, letras):
    """Cria população inicial no problema da senha
    Args
      tamanho: tamanho da população.
      tamanho_senha: inteiro representando o tamanho da senha.
      letras: letras possíveis de serem sorteadas.
    Returns:
      Lista com todos os indivíduos da população no problema da senha.
    """
    populacao = []
    for n in range(tamanho):
        populacao.append(individuo_senha(tamanho_senha, letras))
    return populacao

def funcao_objetivo_senha(individuo, senha_verdadeira):
    """Computa a funcao objetivo de um individuo no problema da senha
    Args:
      individiuo: lista contendo as letras da senha
      senha_verdadeira: a senha que você está tentando descobrir
    Returns:
      A "distância" entre a senha proposta e a senha verdadeira. Essa distância
      é medida letra por letra. Quanto mais distante uma letra for da que
      deveria ser, maior é essa distância.
    """
    diferenca = 0

    for letra_candidato, letra_oficial in zip(individuo, senha_verdadeira):
        diferenca = diferenca + abs(ord(letra_candidato) - ord(letra_oficial))

    return diferenca

def funcao_objetivo_pop_senha(populacao, senha_verdadeira):
    """Computa a funcao objetivo de uma populaçao no problema da senha.
    Args:
      populacao: lista com todos os individuos da população
      senha_verdadeira: a senha que você está tentando descobrir
    Returns:
      Lista contendo os valores da métrica de distância entre senhas.
    """
    resultado = []

    for individuo in populacao:
        resultado.append(funcao_objetivo_senha(individuo, senha_verdadeira))

    return resultado

def selecao_torneio_min(populacao, fitness, tamanho_torneio=3):
    """Faz a seleção de uma população usando torneio.
    Nota: da forma que está implementada, só funciona em problemas de
    minimização.
    Args:
      populacao: população do problema
      fun_objetivo: função objetivo
      tamanho_torneio: quantidade de invidiuos que batalham entre si
    Returns:
      Individuos selecionados. Lista com os individuos selecionados com mesmo
      tamanho do argumento `populacao`.
    """
    selecionados = []

    # criamos essa variável para associar cada individuo com seu valor de fitness
    par_populacao_fitness = list(zip(populacao, fitness))

    # vamos fazer len(populacao) torneios! Que comecem os jogos!
    for _ in range(len(populacao)):
        combatentes = random.sample(par_populacao_fitness, tamanho_torneio)

        # é assim que se escreve infinito em python
        minimo_fitness = float("inf")

        for par_individuo_fitness in combatentes:
            individuo = par_individuo_fitness[0]
            fit = par_individuo_fitness[1]

            # queremos o individuo de menor fitness
            if fit < minimo_fitness:
                selecionado = individuo
                minimo_fitness = fit

        selecionados.append(selecionado)

    return selecionados

def mutacao_senha(individuo, letras):
    """Realiza a mutação de um gene no problema da senha.
    Args:
      individuo: uma lista representado um individuo no problema da senha
      letras: letras possíveis de serem sorteadas.
    Return:
      Um individuo (senha) com um gene mutado.
    """
    gene = random.randint(0, len(individuo) - 1)
    individuo[gene] = gene_letra(letras)
    return individuo

def cruzamento_ponto_simples(pai, mae):
    """Operador de cruzamento de ponto simples.
    Args:
      pai: uma lista representando um individuo
      mae : uma lista representando um individuo
    Returns:
      Duas listas, sendo que cada uma representa um filho dos pais que foram os
      argumentos.
    """
    ponto_de_corte = random.randint(1, len(pai) - 1)

    filho1 = pai[:ponto_de_corte] + mae[ponto_de_corte:]
    filho2 = mae[:ponto_de_corte] + pai[ponto_de_corte:]

    return filho1, filho2



#############################################################################
' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Experimento A.06 ~~~~~~~~~~~~~~~~~~~~~~~~~~~ '
#############################################################################

def distancia_entre_dois_pontos(a, b):
    """Computa a distância Euclidiana entre dois pontos em R^2
    Args:
      a: lista contendo as coordenadas x e y de um ponto.
      b: lista contendo as coordenadas x e y de um ponto.
    Returns:
      Distância entre as coordenadas dos pontos `a` e `b`.
    """

    x1 = a[0]
    x2 = b[0]
    y1 = a[1]
    y2 = b[1]

    dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2)

    return dist


# NOVIDADE
def cria_cidades(n):
    """Cria um dicionário aleatório de cidades com suas posições (x,y).
    Args:
      n: inteiro positivo
        Número de cidades que serão visitadas pelo caixeiro.
    Returns:
      Dicionário contendo o nome das cidades como chaves e a coordenada no plano
      cartesiano das cidades como valores.
    """

    cidades = {}

    for i in range(n):
        cidades[f"Cidade {i}"] = (random.random(), random.random())

    return cidades

def individuo_cv(cidades):
    """Sorteia um caminho possível no problema do caixeiro viajante
    Args:
      cidades:
        Dicionário onde as chaves são os nomes das cidades e os valores são as
        coordenadas das cidades.
    Return:
      Retorna uma lista de nomes de cidades formando um caminho onde visitamos
      cada cidade apenas uma vez.
    """
    nomes = list(cidades.keys())
    random.shuffle(nomes)
    return nomes

def populacao_inicial_cv(tamanho, cidades):
    """Cria população inicial no problema do caixeiro viajante.
    Args
      tamanho:
        Tamanho da população.
      cidades:
        Dicionário onde as chaves são os nomes das cidades e os valores são as
        coordenadas das cidades.
    Returns:
      Lista com todos os indivíduos da população no problema do caixeiro
      viajante.
    """
    populacao = []
    for _ in range(tamanho):
        populacao.append(individuo_cv(cidades))
    return populacao


def cruzamento_ordenado(pai, mae):
    """Operador de cruzamento ordenado.
    Neste cruzamento, os filhos mantém os mesmos genes que seus pais tinham,
    porém em uma outra ordem. Trata-se de um tipo de cruzamento útil para
    problemas onde a ordem dos genes é importante e não podemos alterar os genes
    em si. É um cruzamento que pode ser usado no problema do caixeiro viajante.
    Ver pág. 37 do livro do Wirsansky.
    Args:
      pai: uma lista representando um individuo
      mae : uma lista representando um individuo
    Returns:
      Duas listas, sendo que cada uma representa um filho dos pais que foram os
      argumentos. Estas listas mantém os genes originais dos pais, porém altera
      a ordem deles
    """
    corte1 = random.randint(0, len(pai) - 2)
    corte2 = random.randint(corte1 + 1, len(pai) - 1)
    
    filho1 = pai[corte1:corte2]
    for gene in mae:
        if gene not in filho1:
            filho1.append(gene)
            
    filho2 = mae[corte1:corte2]
    for gene in pai:
        if gene not in filho2:
            filho2.append(gene)
            
    return filho1, filho2         
    
def mutacao_de_troca(individuo):
    """Troca o valor de dois genes.
    Args:
      individuo: uma lista representado um individuo.
    Return:
      O indivíduo recebido como argumento, porém com dois dos seus genes
      trocados de posição.
    """
    indices = list(range(len(individuo)))
    lista_sorteada = random.sample(indices, k=2)
    
    indice1 = lista_sorteada[0]
    indice2 = lista_sorteada[1]
    
    individuo[indice1], individuo[indice2] = individuo[indice2], individuo[indice1]
    
    return individuo
    
def funcao_objetivo_cv(individuo, cidades):
    """Computa a funcao objetivo de um individuo no problema do caixeiro viajante.
    Args:
      individiuo:
        Lista contendo a ordem das cidades que serão visitadas
      cidades:
        Dicionário onde as chaves são os nomes das cidades e os valores são as
        coordenadas das cidades.
    Returns:
      A distância percorrida pelo caixeiro seguindo o caminho contido no
      `individuo`. Lembrando que após percorrer todas as cidades em ordem, o
      caixeiro retorna para a cidade original de onde começou sua viagem.
    """

    distancia = 0
    
    for posicao in range(len(individuo) -1):
        
        partida = cidades[individuo[posicao]]
        chegada = cidades[individuo[posicao+1]]

        percurso = distancia_entre_dois_pontos(partida, chegada)
        distancia = distancia + percurso
        
    # Calculando o caminho de volta para a cidade inicial
    partida = cidades[individuo[-1]]
    chegada = cidades[individuo[0]]
    
    percurso = distancia_entre_dois_pontos(partida, chegada)
    distancia = distancia + percurso
    
    return distancia

def funcao_objetivo_pop_cv(populacao, cidades):
    """Computa a funcao objetivo de uma população no problema do caixeiro viajante.
    Args:
      populacao:
        Lista com todos os inviduos da população
      cidades:
        Dicionário onde as chaves são os nomes das cidades e os valores são as
        coordenadas das cidades.
    Returns:
      Lista contendo a distância percorrida pelo caixeiro para todos os
      indivíduos da população.
    """

    resultado = []
    for individuo in populacao:
        resultado.append(funcao_objetivo_cv(individuo, cidades))

    return resultado



#############################################################################
' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Experimento A.07 ~~~~~~~~~~~~~~~~~~~~~~~~~~~ '
#############################################################################

def computa_mochila(individuo, objetos, ordem_dos_nomes):
    """Computa o valor total e peso total de uma mochila
    Args:
      individiuo:
        Lista binária contendo a informação de quais objetos serão selecionados.
      objetos:
        Dicionário onde as chaves são os nomes dos objetos e os valores são
        dicionários com a informação do peso e valor.
      ordem_dos_nomes:
        Lista contendo a ordem dos nomes dos objetos.
    Returns:
      valor_total: valor total dos itens da mochila em unidades de dinheiros.
      peso_total: peso total dos itens da mochila em unidades de massa.
    """

    valor_total=0
    peso_total=0
    
    for pegou_o_item_ou_nao, nome_do_item in zip(individuo, ordem_dos_nomes):
        if pegou_o_item_ou_nao == 1:
            valor_do_item = objetos[nome_do_item]["valor"]
            peso_do_item = objetos[nome_do_item]["peso"]
            
            valor_total = valor_total + valor_do_item
            peso_total = peso_total + peso_do_item

    return valor_total, peso_total

def func_objetivo_mochila(individuo, objetos, limite, ordem_dos_nomes):
    """Computa a funcao objetivo de um candidato no problema da mochila.
    Args:
      individiuo:
        Lista binária contendo a informação de quais objetos serão selecionados.
      objetos:
        Dicionário onde as chaves são os nomes dos objetos e os valores são
        dicionários com a informação do peso e valor.
      limite:
        Número indicando o limite de peso que a mochila aguenta.
      ordem_dos_nomes:
        Lista contendo a ordem dos nomes dos objetos.
    Returns:
      Valor total dos itens inseridos na mochila considerando a penalidade para
      quando o peso excede o limite.
    """

    valor_mochila, peso_mochila = computa_mochila(individuo, objetos, ordem_dos_nomes)
    
    if peso_mochila > limite:
        return 0.01
    else:
        return valor_mochila
    

def func_objetivo_pop_mochila(populacao, objetos, limite, ordem_dos_nomes):
    """Computa a fun. objetivo de uma populacao no problema da mochila
    Args:
      populacao:
        Lista com todos os individuos da população
      objetos:
        Dicionário onde as chaves são os nomes dos objetos e os valores são
        dicionários com a informação do peso e valor.
      limite:
        Número indicando o limite de peso que a mochila aguenta.
      ordem_dos_nomes:
        Lista contendo a ordem dos nomes dos objetos.
    Returns:
      Lista contendo o valor dos itens da mochila de cada indivíduo.
    """

    resultado = []
    for individuo in populacao:
        resultado.append(
            func_objetivo_mochila(
                individuo, objetos, limite, ordem_dos_nomes
            )
        )

    return resultado

def selecao_torneio_max(populacao, fitness, tamanho_torneio=3):
    """Faz a seleção de uma população usando torneio.
    Nota: da forma que está implementada, só funciona em problemas de
    minimização.
    Args:
      populacao: população do problema
      fun_objetivo: função objetivo
      tamanho_torneio: quantidade de invidiuos que batalham entre si
    Returns:
      Individuos selecionados. Lista com os individuos selecionados com mesmo
      tamanho do argumento `populacao`.
    """
    selecionados = []

    # criamos essa variável para associar cada individuo com seu valor de fitness
    par_populacao_fitness = list(zip(populacao, fitness))

    # vamos fazer len(populacao) torneios! Que comecem os jogos!
    for _ in range(len(populacao)):
        combatentes = random.sample(par_populacao_fitness, tamanho_torneio)

        # é assim que se escreve infinito em python
        minimo_fitness = 0.01

        for par_individuo_fitness in combatentes:
            individuo = par_individuo_fitness[0]
            fit = par_individuo_fitness[1]

            # queremos o individuo de menor fitness
            if fit > minimo_fitness:
                selecionado = individuo
                minimo_fitness = fit

        selecionados.append(selecionado)

    return selecionados
