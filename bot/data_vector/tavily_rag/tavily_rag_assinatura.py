from bot.data_vector.tool_tavily_search_url import tavily_search_tool

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

rag_urls_tavily_assinatura = tavily_search_tool(urls_assinatura)