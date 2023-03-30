"""Importações"""

import random
import itertools



"""Funções algorítimos genéticos"""

#Exp 1:
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


#Exp 3:

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


#Exp 4:
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

    
#Exp 3:

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


#Exp 5

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

    return 

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


