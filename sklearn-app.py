from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def sumarizar_texto(texto, n_sentencas=5):
    # Tokeniza o texto em sentenças
    sentencas = texto.split('.')
    
    # Remove sentenças vazias ou espaços extras
    sentencas = [s.strip() for s in sentencas if s.strip()]
    
    # Calcula a matriz de termos de frequência de cada sentença
    vectorizer = CountVectorizer().fit_transform(sentencas)
    vetores = vectorizer.toarray()
    
    # Calcula a similaridade de cosseno entre as sentenças
    cos_sim_matriz = cosine_similarity(vetores, vetores)
    
    # Calcula a pontuação de similaridade para cada sentença somando as similaridades de cosseno
    pontuacoes = cos_sim_matriz.sum(axis=1)
    
    # Ordena as sentenças de acordo com a pontuação em ordem decrescente
    sentencas_ordenadas = [sentencas[i] for i in np.argsort(pontuacoes, axis=0)[::-1]]
    
    # Seleciona as n_sentencas mais importantes
    resumo = '. '.join(sentencas_ordenadas[:n_sentencas])
    
    return resumo

# Exemplo de uso
texto = """
1. O que é PPR (Plano de Participação em Resultados)?
É o programa anual de participação em resultados da Companhia (Grupo UOL) e suas
empresas/unidades de negócios, que tem como principal objetivo recompensar o desempenho
dos profissionais pelo cumprimento de metas claras e objetivas. O programa é composto pelas
seguintes metas:
a) Gatilho: é meta principal da Companhia ou empresa/unidade de negócios, estabelecida para
o ano, de forma que todos os profissionais trabalhem com o mesmo foco. Se esta meta não for
atingida, não há pagamento de qualquer valor referente ao PPR.
b) Metas específicas: atingido o gatilho, o valor do prêmio será calculado com base no
atingimento de metas específicas anuais estabelecidas para cada área.
2. Condições gerais do programa
2.1. Elegibilidade
O programa se aplica a todos os profissionais efetivos. Não estão incluídos: estagiários,
terceiros, temporários, menores aprendizes e profissionais com contrato por prazo
determinado.
2.2. Apuração das metas e limites para pagamento
a) Os gatilhos, metas e limites das empresas para pagamentos de cada ano serão apurados
durante o mês de janeiro do ano subsequente.
b) O limite para pagamento de PPR em cada empresa será de 20% da GLC (Geração Livre de
Caixa) ou do LL (Lucro Líquido) no ano a que se refere o PPR. A regra válida para cada empresa
(GLC ou LL) será divulgada no anúncio das metas.
b.1.) Caso o valor total a ser pago, de acordo com atingimentos de gatilho e metas,
exceda o limite estipulado para a empresa, o valor a ser pago sofrerá o ajuste
proporcional.
b.2.) No do PagSeguro PagBank, companhia listada na NYSE (EUA), há ainda,
adicionalmente ao limite geral mencionado no caput deste item b, o limite anual referente
à parcela em ações do pagamento de PPR entregues anualmente aos Beneficiários,
que não pode exceder 1% (um por cento) do número total de Ações da Cia.
c) No caso das áreas corporativas que atendem a todas as empresas do Grupo UOL (ou parte
delas), a apuração levará em conta a ponderação do percentual de rateio adotado de cada área
corporativa às empresas atendidas e atingimentos das áreas atendidas correspondentes
(considerada inclusive a limitação de que trata o item 2.2.b, acima).
2.3. Pagamento em caso de atingimento das metas (total ou parcialmente)
a) A referência para o valor do prêmio é a fração ou múltiplo do salário do mês de dezembro do
ano ao qual se refere o PPR.
b) Caso sejam atingidos o gatilho (100%) e as metas específicas (total ou parcialmente), o
valor (ajustado pelo limite previsto no item 2.2.b, se for o caso) poderá ser pago aos
profissionais até o último dia útil de março do ano seguinte ao ano ao qual se refere o PPR.
2
Interna
Interna
c) A critério da Companhia (ou de comitê designado pela Companhia), a parcela do PPR poderá
ser paga em ações de empresas do Grupo UOL com capital aberto em bolsa de valores.
Pagamento em Ações: caso
seja definido pelo Comitê do PILP-Metas que o pagamento será em Ações, as Ações serão
entregues aos Beneficiários em até 10 (dez) dias úteis após a Data da Apuração."""

resumo = sumarizar_texto(texto, n_sentencas=20)
print(resumo)
