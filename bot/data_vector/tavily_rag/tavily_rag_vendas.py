from bot.data_vector.tool_tavily_search_url import tavily_search_tool

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

rag_urls_tavily_vendas = tavily_search_tool(urls_vendas)