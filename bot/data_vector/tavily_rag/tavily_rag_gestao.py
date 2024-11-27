from bot.data_vector.tool_tavily_search_url import tavily_search_tool

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

rag_urls_tavily_gestao = tavily_search_tool(urls_gestao)