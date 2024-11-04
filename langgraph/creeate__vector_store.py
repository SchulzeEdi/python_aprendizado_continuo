from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

import time
from langchain.schema import Document

from langchain_community.vectorstores import Chroma
from langchain.tools.retriever import create_retriever_tool
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

#URL DE COBRANCA
urls_cobranca = [
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-visualizar-clientes-que-est%C3%A3o-na-fila-para-cobran%C3%A7a",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-visualizar-quais-clientes-est%C3%A3o-com-a-cobran%C3%A7a-pausada",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Posso-alterar-o-texto-do-SMS-de-cobran%C3%A7a",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Solucionando-a-n%C3%A3o-reabilita%C3%A7%C3%A3o-autom%C3%A1tica-de-contratos-negativados-ap%C3%B3s-migra%C3%A7%C3%A3o-de-M%C3%B3dulo-ou-ERP",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-negativar-clientes-inadimplentes",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Ap%C3%B3s-reabilitar-o-cliente-quanto-tempo-leva-para-o-registro-ser-exclu%C3%ADdo",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-acontece-a-reabilita%C3%A7%C3%A3o-de-um-cliente",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-visualizar-clientes-reabilitados",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-saber-se-houve-algum-erro-de-reabilita%C3%A7%C3%A3o",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-visualizar-quantos-clientes-pagaram-ap%C3%B3s-a-cobran%C3%A7a",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-visualizar-contato-registrado",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Para-que-serve-e-como-funciona-o-relat%C3%B3rio-Situa%C3%A7%C3%A3o-do-capital",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-visualizar-quais-clientes-pagaram-ap%C3%B3s-a-cobran%C3%A7a",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-verificar-qual-r%C3%A9gua-est%C3%A1-aplicada-para-determinado-cliente",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-marcar-um-cliente-como-reabilitado",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Cliente-pagou-e-permanece-negativado",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-reabilitar-um-cliente-manualmente",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/O-cliente-negativado-n%C3%A3o-quitou-todas-as-parcelas-em-atraso-devo-reabilit%C3%A1-lo",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-filtrar-quantas-negativa%C3%A7%C3%B5es-foram-realizadas-em-determinado-per%C3%ADodo",
]

names_cobranca = [
    "Cobranca"
]

#URL DE GESTAO
urls_gestao = [
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-ver-o-detalhamento-de-uma-an%C3%A1lise-de-cr%C3%A9dito",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/O-que-fazer-se-um-contrato-estiver-com-as-dados-diferentes-do-meu-sistema-frente-de-caixa",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-fazer-a-confer%C3%AAncia-dos-lotes-enviados-pelo-ERP-frente-de-caixa",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/A-import%C3%A2ncia-do-seu-ERP-frente-de-caixa-e-o-envio-dos-lotes-movimenta%C3%A7%C3%B5es-da-sua-loja",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Inadimpl%C3%AAncia-por-Safra",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/O-que-fazer-se-identificar-uma-inconsist%C3%AAncia-nos-lotes-recebidos-do-ERP",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/O-que-%C3%A9-Score-Base-e-Score-Proposta",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Resumo-da-loja-Quantidade-de-clientes-novos-por-m%C3%AAs",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Relat%C3%B3rios-de-Gest%C3%A3o"
]
names_gestao = [
    "Gestao", 
]

#URL DE ASSINATURA
urls_assinatura = [
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Posso-enviar-o-comprovante-de-pagamento-para-ter-a-libera%C3%A7%C3%A3o-do-meu-saldo",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/D%C3%A9bito-de-mensalidade-do-Meu-Credi%C3%A1rio",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-funciona-a-emiss%C3%A3o-da-nota-fiscal",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-assinar-o-Meu-Credi%C3%A1rio",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Quando-minha-nota-fiscal-de-servi%C3%A7o-%C3%A9-emitida",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-bloquear-um-usu%C3%A1rio-no-sistema",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Por-que-n%C3%A3o-estou-vendo-todos-os-bot%C3%B5es",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Utiliza%C3%A7%C3%A3o-das-an%C3%A1lises-e-negativa%C3%A7%C3%B5es",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/O-que-acontece-se-a-minha-mensalidade-n%C3%A3o-for-paga",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-verificar-o-extrato-de-consumos-dentro-da-plataforma"
]
names_assinatura = [
    "Assinatura"
]

#URL DE VENDAS
urls_vendas = [
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Por-que-solicitar-os-documentos-originais-para-abertura-do-credi%C3%A1rio",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-cadastrar-um-cliente",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-desbloquear-um-cliente",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Existe-um-percentual-limite-para-trabalhar-a-cobran%C3%A7a-de-juros",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-configurar-os-juros-por-parcela-em-minha-loja",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-fazer-um-acordo-no-sistema",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-cancelar-um-acordo",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-alterar-a-data-de-recebimento",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-fazer-um-recebimento-com-Desconto-Manual",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-fazer-um-recebimento-com-Desconto-Autom%C3%A1tico"
]
names_vendas = [
    "Vendas"
]

#URL DE PERGUNTAS FREQUENTES
urls_perguntas_frequentes = [
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/O-que-acontece-com-meus-clientes-negativados-se-eu-cancelar-a-assinatura",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Posso-negativar-os-clientes-que-j%C3%A1-estavam-em-atraso-quando-implantei-o-sistema",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/A-negativa%C3%A7%C3%A3o-%C3%A9-feita-em-que-%C3%B3rg%C3%A3o",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Posso-negativar-o-cliente-pelo-Meu-Credi%C3%A1rio",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-criar-um-atalho-do-Meu-Credi%C3%A1rio-na-%C3%A1rea-de-trabalho",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Introdu%C3%A7%C3%A3o-ao-Meu-Credi%C3%A1rio",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-fa%C3%A7o-para-solicitar-um-atendimento-de-suporte-do-Meu-Credi%C3%A1rio",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Qual-loja-consultou-meu-CPF",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-cancelar-a-plataforma",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-fazer-um-print-captura-de-tela-em-meu-computador"
]

driver = webdriver.Chrome()

docs_cobranca = []
for url in urls_cobranca:
    driver.get(url)
    time.sleep(5)
    content = driver.find_element(By.TAG_NAME, "body").text
    docs_cobranca.append(Document(page_content=content))

docs_gestao = []
for url in urls_gestao:
    driver.get(url)
    time.sleep(5)
    content = driver.find_element(By.TAG_NAME, "body").text
    docs_gestao.append(Document(page_content=content))

docs_assinatura = []
for url in urls_assinatura:
    driver.get(url)
    time.sleep(5)
    content = driver.find_element(By.TAG_NAME, "body").text
    docs_cobranca.append(Document(page_content=content))

docs_vendas = []
for url in urls_vendas:
    driver.get(url)
    time.sleep(5)
    content = driver.find_element(By.TAG_NAME, "body").text
    docs_vendas.append(Document(page_content=content))

driver.quit()

text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(chunk_size=500, chunk_overlap=200)

docs_list_cobranca = [text_splitter.split_documents([doc]) for doc in docs_cobranca]
docs_list_gestao = [text_splitter.split_documents([doc]) for doc in docs_gestao]
docs_list_assinatura = [text_splitter.split_documents([doc]) for doc in docs_assinatura]
docs_list_vendas = [text_splitter.split_documents([doc]) for doc in docs_vendas]

docs_list_cobranca = [chunk for sublist in docs_list_cobranca for chunk in sublist]
docs_list_gestao = [chunk for sublist in docs_list_gestao for chunk in sublist]
docs_list_assinatura = [chunk for sublist in docs_list_assinatura for chunk in sublist]
docs_list_vendas = [chunk for sublist in docs_list_vendas for chunk in sublist]

retrievers_cobranca = {}
retrievers_gestao = {}
retrievers_assinatura = {}
retrievers_vendas = {}
retrievers_perguntas_frequentes = {}

def create_retrievers_system(retrievers, names, docs_list):
  for doc, name in zip(docs_list, names):
    split = text_splitter.split_documents([doc])
    vectorstore = Chroma.from_documents(
      documents=split,
      collection_name=name,
      embedding= HuggingFaceEmbeddings(),
      persist_directory="./data"
    )
    retriever_tool = create_retriever_tool(vectorstore.as_retriever(search_kwargs={"k": 3}), f"retrieve_{name}_posts", f"Ferramenta para buscar informações sobre {name}")
    retrievers.update({name: retriever_tool})
  return retrievers

retrievers_cobranca = create_retrievers_system(retrievers_cobranca, names_cobranca, docs_list_cobranca)
retrievers_gestao = create_retrievers_system(retrievers_gestao, names_gestao, docs_list_gestao)
retrievers_vendas = create_retrievers_system(retrievers_vendas, names_vendas, docs_list_vendas)
retrievers_assinatura = create_retrievers_system(retrievers_assinatura, names_assinatura, docs_list_assinatura)