# Python aprendizado continuo

O projeto consiste em instalar as dependências necessárias com o comando:
"pip install -r requirements.txt"

Após as instalações das dependências, caso queira ver como foi feito o webscraping, como criei o banco vetorial,
podem verificar no arquivo "create_vector_store.py" dentro da pasta "langgraph". OBS: Não é preciso rodar este arquivo.

No requirements.txt está para instalar o Selenium, pois realizei o webscraping todo com ele, pois o site estava renderizando
o html em Javascript, deixando de funcionar o BeautifulSoup4. Caso queira gerar do zero o banco vetorial (não contém necessidade).
Tem que instalar o ChromeDriver e o Google Chrome, caso esteja usando linux, tem que usar a versão 114 tanto do ChromeDriver como do
Google Chrome.

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

Para rodar o projeto após as bibliotecas instaladas, basta você estiver na pasta raiz do projeto (python_aprendizado_continuo) e rodar o seguinte comando:

"python -m streamlit run app.py"

Quando o projeto estiver rodando, deixo algumas possíveis perguntas de exemplo que podem ser feitas:
[coloco o módulo, pois algumas funcionalidades contém em mais de um módulo e o bot também acaba se confundindo.]

"Como visualizo clientes que estão na fila de cobrança? No módulo de cobrança"
"Como que eu envio comprovante de pagamento para ter a liberação do meu saldo? No módulo de assinatura"
"Como que eu olho o detalhamento de uma análise de crédito? No módulo de gestão"
"Como que eu cadastro um cliente? No Módulo de vendas?"

OBSERVAÇÃO: Usei tudo de forma gratuita, raramente ele gerou um erro, acredito que seja por request algo assim. Porém, quando reinicia a aplicação ele funciona normalmente.
