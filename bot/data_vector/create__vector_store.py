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
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-visualizar-quais-clientes-est%C3%A3o-com-a-cobran%C3%A7a-pausada",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Posso-alterar-o-texto-do-SMS-de-cobran%C3%A7a",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Solucionando-a-n%C3%A3o-reabilita%C3%A7%C3%A3o-autom%C3%A1tica-de-contratos-negativados-ap%C3%B3s-migra%C3%A7%C3%A3o-de-M%C3%B3dulo-ou-ERP",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-negativar-clientes-inadimplentes",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Ap%C3%B3s-reabilitar-o-cliente-quanto-tempo-leva-para-o-registro-ser-exclu%C3%ADdo",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-acontece-a-reabilita%C3%A7%C3%A3o-de-um-cliente",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-visualizar-clientes-reabilitados",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-saber-se-houve-algum-erro-de-reabilita%C3%A7%C3%A3o",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-visualizar-quantos-clientes-pagaram-ap%C3%B3s-a-cobran%C3%A7a",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-visualizar-contato-registrado",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Para-que-serve-e-como-funciona-o-relat%C3%B3rio-Situa%C3%A7%C3%A3o-do-capital",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-visualizar-quais-clientes-pagaram-ap%C3%B3s-a-cobran%C3%A7a",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-verificar-qual-r%C3%A9gua-est%C3%A1-aplicada-para-determinado-cliente",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-marcar-um-cliente-como-reabilitado",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Cliente-pagou-e-permanece-negativado",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-reabilitar-um-cliente-manualmente",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/O-cliente-negativado-n%C3%A3o-quitou-todas-as-parcelas-em-atraso-devo-reabilit%C3%A1-lo",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-filtrar-quantas-negativa%C3%A7%C3%B5es-foram-realizadas-em-determinado-per%C3%ADodo",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-editar-o-cadastro-do-cliente",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-exportar-dados-dos-clientes-negativados",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-visualizar-clientes-a-negativar",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Com-quantos-dias-em-atraso-posso-negativar-um-cliente",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Ap%C3%B3s-a-negativa%C3%A7%C3%A3o-em-quanto-tempo-aparece-publicamente",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-visualizar-os-clientes-negativados",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/O-servi%C3%A7o-de-SMS-est%C3%A1-pausado-Por-que-meu-cliente-negativado-recebeu-SMS",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Por-que-devo-negativar",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Quais-informa%C3%A7%C3%B5es-preciso-para-negativar-um-cliente",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Quando-negativo-um-cliente-como-ele-%C3%A9-informado-desta-a%C3%A7%C3%A3o",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Negativei-o-cliente-e-quero-consultar-se-a-minha-negativa%C3%A7%C3%A3o-j%C3%A1-est%C3%A1-aparecendo",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/O-cliente-se-mudou-e-n%C3%A3o-tenho-o-novo-endere%C3%A7o-posso-negativ%C3%A1-lo",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-cobrar-um-cliente-ap%C3%B3s-a-negativa%C3%A7%C3%A3o",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-alterar-o-nome-da-loja-no-texto-do-SMS",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-alterar-o-contato-no-texto-do-SMS",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-verificar-quem-ativou-pausou-o-envio-de-SMSs-e-a-data-da-a%C3%A7%C3%A3o",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-ativar-SMS-para-cliente-com-cobran%C3%A7a-pausada",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-visualizar-o-texto-de-cada-SMS-que-ser%C3%A1-enviado",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-visualizar-as-respostas-dos-SMSs-de-cobran%C3%A7a",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-pausar-SMS-para-determinado-cliente",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-saber-quais-clientes-est%C3%A3o-em-determinada-fase-da-cobran%C3%A7a",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-enviar-mensagem-via-WhatsApp-para-clientes-inadimplentes-pelo-sistema-Meu-Credi%C3%A1rio",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-funcionam-as-R%C3%A9guas-de-cobran%C3%A7a",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-visualizar-os-SMSs-enviados",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-pausar-ativar-os-SMSs-autom%C3%A1ticos",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Quando-%C3%A9-feito-o-envio-do-SMS-de-cobran%C3%A7a",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/O-cliente-informou-que-recebeu-SMS-mas-n%C3%A3o-tem-parcelas-em-atraso-registradas-no-Meu-Credi%C3%A1rio",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-visualizar-os-juros-e-multa-de-cada-cliente",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-visualizar-configurar-os-percentuais-de-juros-e-multa-por-atraso",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-encontrar-um-cliente-no-M%C3%B3dulo-Cobran%C3%A7a",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-visualizar-os-clientes-de-acordo-com-a-promessa-de-pagamento-em-vigor",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-registrar-promessa-de-pagamento",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Cliente-pagou-e-permanece-na-cobran%C3%A7a",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-visualizar-um-resumo-dos-clientes-no-M%C3%B3dulo-Cobran%C3%A7a",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Quais-usu%C3%A1rios-podem-acessar-o-M%C3%B3dulo-Cobran%C3%A7a",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/A%C3%A7%C3%A3o-Cancelada-ao-negativar-cliente-Cadastro-n%C3%A3o-possui-logradouro-cadastrado",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/A%C3%A7%C3%A3o-Cancelada-ao-negativar-cliente-Contrato-j%C3%A1-registrado-por-Meu-Credi%C3%A1rio",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/A%C3%A7%C3%A3o-Cancelada-ao-negativar-cliente-Informa%C3%A7%C3%B5es-de-complemento-insuficientes",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/A%C3%A7%C3%A3o-Cancelada-ao-negativar-cliente-Voc%C3%AA-n%C3%A3o-possui-saldo-suficiente-para-realizar-a-opera%C3%A7%C3%A3o-Compre-agora-para-negativar-o-cliente",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/A%C3%A7%C3%A3o-Cancelada-ao-negativar-cliente-Cadastro-n%C3%A3o-possui-bairro-cadastrado",
]

names_cobranca = [
    "Cobranca","Cobranca","Cobranca","Cobranca","Cobranca","Cobranca","Cobranca","Cobranca","Cobranca","Cobranca",
    "Cobranca","Cobranca","Cobranca","Cobranca","Cobranca","Cobranca","Cobranca","Cobranca","Cobranca","Cobranca",
    "Cobranca","Cobranca","Cobranca","Cobranca","Cobranca","Cobranca","Cobranca","Cobranca","Cobranca","Cobranca",
    "Cobranca","Cobranca","Cobranca","Cobranca","Cobranca","Cobranca","Cobranca","Cobranca","Cobranca","Cobranca",
    "Cobranca","Cobranca","Cobranca","Cobranca","Cobranca","Cobranca","Cobranca","Cobranca","Cobranca","Cobranca",
    "Cobranca","Cobranca","Cobranca","Cobranca","Cobranca","Cobranca","Cobranca","Cobranca"
]

#URL DE GESTAO
urls_gestao = [
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-ver-o-detalhamento-de-uma-an%C3%A1lise-de-cr%C3%A9dito",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/O-que-fazer-se-um-contrato-estiver-com-as-dados-diferentes-do-meu-sistema-frente-de-caixa",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-fazer-a-confer%C3%AAncia-dos-lotes-enviados-pelo-ERP-frente-de-caixa",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/A-import%C3%A2ncia-do-seu-ERP-frente-de-caixa-e-o-envio-dos-lotes-movimenta%C3%A7%C3%B5es-da-sua-loja",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Inadimpl%C3%AAncia-por-Safra",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/O-que-fazer-se-identificar-uma-inconsist%C3%AAncia-nos-lotes-recebidos-do-ERP",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/O-que-%C3%A9-Score-Base-e-Score-Proposta",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Resumo-da-loja-Quantidade-de-clientes-novos-por-m%C3%AAs",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Relat%C3%B3rios-de-Gest%C3%A3o"
]
names_gestao = [
    "Gestao", "Gestao", "Gestao",
    "Gestao", "Gestao", "Gestao",
    "Gestao", "Gestao", "Gestao"
]

#URL DE ASSINATURA
urls_assinatura = [
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Posso-enviar-o-comprovante-de-pagamento-para-ter-a-libera%C3%A7%C3%A3o-do-meu-saldo",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/D%C3%A9bito-de-mensalidade-do-Meu-Credi%C3%A1rio",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-funciona-a-emiss%C3%A3o-da-nota-fiscal",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-assinar-o-Meu-Credi%C3%A1rio",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Quando-minha-nota-fiscal-de-servi%C3%A7o-%C3%A9-emitida",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-bloquear-um-usu%C3%A1rio-no-sistema",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Por-que-n%C3%A3o-estou-vendo-todos-os-bot%C3%B5es",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Utiliza%C3%A7%C3%A3o-das-an%C3%A1lises-e-negativa%C3%A7%C3%B5es",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/O-que-acontece-se-a-minha-mensalidade-n%C3%A3o-for-paga",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-verificar-o-extrato-de-consumos-dentro-da-plataforma",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/O-sistema-est%C3%A1-bloqueado-como-fa%C3%A7o-para-recuperar-minha-conta",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-cadastrar-um-novo-usu%C3%A1rio",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Por-que-cadastrar-todos-os-funcion%C3%A1rios-no-sistema",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-editar-os-dados-de-um-usu%C3%A1rio-cadastrado",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-editar-as-permiss%C3%B5es-de-um-usu%C3%A1rio",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-alterar-a-senha-de-um-usu%C3%A1rio",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-alterar-o-e-mail-que-recebo-a-notifica%C3%A7%C3%A3o-das-Notas-Fiscais",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/O-que-%C3%A9-carteira-centralizada",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-recarregar-via-Mobile",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-configurar-as-a%C3%A7%C3%B5es-inteligentes-recarga-autom%C3%A1tica-e-notifica%C3%A7%C3%B5es",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-fazer-uma-recarga-manual",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Paguei-a-recarga-mas-o-sistema-continua-bloqueado-O-que-est%C3%A1-acontecendo",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/O-que-%C3%A9-Contrato-M%C3%ADnimo-Valor-contratado-n%C3%A3o-consumido",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-saber-o-valor-total-dos-servi%C3%A7os-utilizados-em-determinado-per%C3%ADodo",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-visualizar-e-interpretar-o-extrato-de-consumo",
]
names_assinatura = [
    "Assinatura", "Assinatura", "Assinatura","Assinatura", "Assinatura", "Assinatura","Assinatura", "Assinatura", "Assinatura", "Assinatura",
    "Assinatura", "Assinatura", "Assinatura","Assinatura", "Assinatura", "Assinatura","Assinatura", "Assinatura", "Assinatura", "Assinatura",
    "Assinatura", "Assinatura", "Assinatura","Assinatura"
]

#URL DE VENDAS
urls_vendas = [
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Importei-uma-venda-e-quero-negativar-como-eu-fa%C3%A7o",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-visualizar-o-relat%C3%B3rio-listagem-de-clientes",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/N%C3%A3o-tenho-Excel-em-meu-computador-e-preciso-exportar-um-relat%C3%B3rio",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-visualizar-a-listagem-dos-acordos-cancelados",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Posso-alterar-a-data-de-vencimento-da-parcela-no-carn%C3%AA-j%C3%A1-emitido",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Por-que-solicitar-os-documentos-originais-para-abertura-do-credi%C3%A1rio",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-cadastrar-um-cliente",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-desbloquear-um-cliente",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Existe-um-percentual-limite-para-trabalhar-a-cobran%C3%A7a-de-juros",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-configurar-os-juros-por-parcela-em-minha-loja",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-fazer-um-acordo-no-sistema",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-cancelar-um-acordo",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-alterar-a-data-de-recebimento",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-fazer-um-recebimento-com-Desconto-Manual",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-fazer-um-recebimento-com-Desconto-Autom%C3%A1tico",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Apareceu-a-mensagem-A%C3%A7%C3%A3o-Cancelada-o-que-eu-fa%C3%A7o",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/O-limite-sugerido-%C3%A9-por-venda-ou-por-parcela",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-ver-o-detalhamento-da-an%C3%A1lise-de-cr%C3%A9dito",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-habilitar-o-desconto-manual-de-capital",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-funciona-o-armazenamento-das-minhas-informa%C3%A7%C3%B5es-no-sistema",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-configurar-as-a%C3%A7%C3%B5es-por-perfil-de-risco-em-minha-loja",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-configurar-os-juros-para-o-acordo",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-habilitar-o-desconto-autom%C3%A1tico-de-capital",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-configurar-o-prazo-m%C3%A1ximo-para-o-1%C2%BA-vencimento",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-configurar-o-per%C3%ADodo-para-1%C2%BA-vencimento-em-minha-loja",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-configurar-a-car%C3%AAncia-para-cobran%C3%A7a-de-juros-e-multa-por-atraso-da-minha-loja",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-configurar-os-Juros-e-Multa-por-atraso",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Concentrar-parcelas-em-menos-vezes-configurando-no-sistema",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-configurar-as-condi%C3%A7%C3%B5es-de-parcelamento-da-minha-loja",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-cadastrar-ou-alterar-o-endere%C3%A7o-da-minha-loja",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-alterar-o-telefone-comercial-da-minha-loja",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-alterar-o-e-mail-da-minha-loja",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-configurar-os-dados-obrigat%C3%B3rios-para-cadastro-de-clientes",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Impress%C3%A3o-do-carn%C3%AA",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-atualizar-o-cadastro-de-um-cliente",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-bloquear-um-cliente",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-visualizar-e-imprimir-o-Espelho-do-Cliente",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Contatos-de-Refer%C3%AAncia-no-cadastro-do-cliente-a-loja-tem-direito-de-solicitar",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Observa%C3%A7%C3%B5es-na-tela-de-cadastro-do-cliente-para-que-serve-e-onde-visualiz%C3%A1-las",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Qual-a-import%C3%A2ncia-das-informa%C3%A7%C3%B5es-do-cadastro-do-cliente",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Quando-o-sistema-pede-atualiza%C3%A7%C3%A3o-cadastral-do-cliente",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/N%C3%A3o-consigo-cadastrar-cliente-apresenta-mensagem-CPF-inv%C3%A1lido",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Erro-ao-cancelar-venda-ou-estornar-recebimento-O-que-fazer",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Erro-ao-imprimir-carn%C3%AA-recibo-O-que-fazer",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Importei-uma-venda-errada-o-que-eu-fa%C3%A7o",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-solicitar-importa%C3%A7%C3%B5es-em-lote",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-importar-uma-venda-para-o-sistema",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-receber-parcelas-via-Mobile",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-realizar-vendas-via-Mobile",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-converter-uma-planilha-em-Excel-do-formato-csv-para-xlsx",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-fazer-a-exporta%C3%A7%C3%A3o-dos-meus-dados-do-sistema",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-visualizar-o-relat%C3%B3rio-resumo-da-loja",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-visualizar-o-relat%C3%B3rio-extrato-de-parcelas-em-aberto",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-fechar-o-caixa-utilizando-os-relat%C3%B3rios-do-sistema",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-visualizar-o-relat%C3%B3rio-extrato-de-recebimentos",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-visualizar-o-usu%C3%A1rio-autorizador-de-uma-venda",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-visualizar-o-relat%C3%B3rio-extrato-de-vendas",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/como-visualizar-o-relat%C3%B3rio-de-aniversariantes",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-visualizar-o-relat%C3%B3rio-de-clientes-bloqueados",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-visualizar-qual-usu%C3%A1rio-realizou-an%C3%A1lise",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-verificar-o-valor-que-o-Meu-Credi%C3%A1rio-evitou-de-perder-na-minha-loja",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/resumo-da-loja-quantidade-de-clientes-novos-por-mes",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-exportar-o-detalhamento-da-an%C3%A1lise",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-visualizar-os-acordos-vencidos",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-cancelar-um-acordo-com-recebimento",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-visualizar-um-relat%C3%B3rio-de-Acordos",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-visualizar-um-acordo-na-movimenta%C3%A7%C3%A3o-di%C3%A1ria",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-visualizar-os-SMSs-manuais-enviados",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-visualizar-se-um-SMS-manual-foi-respondido-e-a-sua-resposta",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Vendas-Como-fa%C3%A7o-para-enviar-SMS-manual-para-meus-clientes",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-visualizar-a-listagem-dos-recebimentos-estornados",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-estornar-um-recebimento",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-reimprimir-um-recibo",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-fazer-um-recebimento-parcial",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-fazer-um-recebimento",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-reimprimir-o-carn%C3%AA",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Impress%C3%A3o-e-formato-do-carn%C3%AA-e-recibo",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-visualizar-a-listagem-das-vendas-canceladas",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-cancelar-uma-venda-com-recebimentos",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-cancelar-uma-venda-carn%C3%AA",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Por-que-analisar-todas-as-vendas-no-credi%C3%A1rio",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/O-Meu-Credi%C3%A1rio-utiliza-o-cadastro-positivo-em-sua-an%C3%A1lise-de-cr%C3%A9dito",
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Quais-os-modelos-de-an%C3%A1lise-do-Meu-Credi%C3%A1rio",
    
]
names_vendas = [
    "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas",
    "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas",
    "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas",
    "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas",
    "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas",
    "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas",
    "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas",
    "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas",
    "Vendas", "Vendas"


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

text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(chunk_size=300, chunk_overlap=100)

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

create_retrievers_system(retrievers_cobranca, names_cobranca, docs_list_cobranca)
create_retrievers_system(retrievers_gestao, names_gestao, docs_list_gestao)
create_retrievers_system(retrievers_vendas, names_vendas, docs_list_vendas)
create_retrievers_system(retrievers_assinatura, names_assinatura, docs_list_assinatura)