# Python aprendizado continuo

## Segue como o projeto foi estruturado e como colocar ele em funcionamento:

O projeto consiste em instalar as dependências necessárias, caso rode com Linux, alguns erros podem ocorrer por causa
do Selenium, caso use windows, fica mais tranquilo.

Após as instalações das dependências, caso queira ver como foi feito o webscraping e como retirei os dados do site,
podem verificar no arquivo "create_vector_store.py" dentro da pasta "langgraph". OBS: Não é preciso rodar este arquivo.

Como o banco vetorial é armazenado e já está no projeto quando realiza um clone, não se torna necessário fazer a realização
do banco vetorial novamente. Ele fica persistido na pasta "data", realizado com ChromaDB.

Foi realizado o front-end com Streamlit para a criação do Chat.

Para a questão do bot, ele foi criado e desenvolvido com langchain e langgraph. Langgraph é usado para criar todo o "roteamento"
de como o bot deve buscar essas informações.

Ele foi separado em 5 rotas diferentes. Cada um por módulo da empresa Meu Crediário, além do "Aleatórios", que são perguntas genéricas.
A ideia é separar cada setor por nó dentro da árvore criada. Começando com um bot de roteamento do qual decide para qual banco vetorial deve
ser buscado a informação. Após isto, se a dúvida é relacionada a um módulo, busca a informação no nó do módulo que contém o banco vetorial que entrega para um outro nó que se chama "generate"
do qual vai receber a resposta do documento e gerar uma outra resposta em cima disto, tornando o bot mais humanizado, deixando ele menos preso
a informação do documento.

Para rodar o projeto após as bibliotecas instaladas, basta estiver na pasta raiz do projeto (python_aprendizado_continuo)
e rodar o seguinte comando:

python -m streamlit run app.py

Quando o projeto estiver rodando, deixo algumas possíveis perguntas de exemplo que podem ser feitas:
[coloco o módulo, pois algumas funcionalidades contém em mais de um módulo e o bot também acaba se confundindo.]

"Como visualizo clientes que estão na fila de cobrança? No módulo de cobrança"
"Como que eu envio comprovante de pagamento para ter a liberação do meu saldo? No módulo de assinatura"
"Como que eu olho o detalhamento de uma análise de crédito? No módulo de gestão"
"Como que eu cadastro um cliente? No Módulo de vendas?"

OBSERVAÇÃO: Usei tudo de forma gratuita, raramente ele gerou um erro, acredito que seja por request algo assim. Porém, reiniciei a aplicação e ele funciona normalmente.