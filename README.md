# QuizIgualdadeGenero
Quiz sobre Igualdade de Gênero. Trabalho final da disciplina de POO do curso de Engenharia de Informática da Universidade Aberta de  Lisboa

README - Quiz de Igualdade de Gênero (3° versão) 

Sobre o programa:
Esse é um quiz interativo para testar o conhecimento do usuário sobre igualdade de gênero.
Esta disponível em 3 idiomas (Português, inglês e Alemão). O idioma pode ser selecionado no início do quiz. Em seguida, poderá visualizar uma tela com opção de login, registro ou jogar sem registrar. Caso opte por se registrar, deverá preencher com seu nome, idade, gênero e criar um pin de até 8 números. Das próximas vezes que jogar poderá fazer login com seu nome de usuário e pin. Se optar por jogar sem se registrar bastará preencher com seu nome e começar o quiz. Também existe a opção de jogar sem inserir um nome, neste caso, por padrão será usado o nome "User" na mensagem final.

O Quiz utiliza um banco de dados em nuvem MySQL para buscar as perguntas e alternativas de respostas. Além de salvar os dados do usuário.

A maioria das perguntas é de múltipla escolha, mas também inclui algumas questões de verdadeiro ou falso.
As alternativas tem pesos diferentes, existem respostas mais distantes e outras mais próximas do 100% adequado a um mundo de igualdade de gênero.
clique na alternativa que mais faz sentido pra você. E siga para a questão seguinte.

No final o sistema exibirá uma mensagem e porcentagem obtida no jogo atual junto com a maior porcentagem registrada em jogadas anteriores para usuários registrados.

Tente novamente para melhorar sua performance!

Requisitos do Sistema:
Python: Versão 3.10 ou superior (completo com todas as dependências tcl/tk)

Biblioteca tkinter: Já vem embutido no Python, não precisa ser instalado separadamente	
Biblioteca MySQL e pygame: Você precisará instalar, caso ainda não possua pode instalar com comando no terminal:

        pip install mysql-connector-python pygame


As credenciais de acesso do Banco de dados já estão configuradas no código.


Fluxo do Programa:
1. Execute o programa: corra o código diretamente no arquivo App.py

2. Selecione o idioma desejado. 

3. Escolha entre Login, Registro ou Jogar sem Registro.

4. Responda as perguntas exibidas.

5. Veja a mensagem final junto a sua pontuação no final e confira também a maior pontuação obtida anteriormente, caso ja tenha jogado antes.

6. Tente novamente para melhorar sua performance!

7. Ou clique em sair se não quiser jogar novamente.

* A qualquer momento pode controlar a música através do ícone no canto superior direito


Estrutura do Código:
Classes:
Alternativa: Cria estrutura encapsulada das alternativas com os pesos.
App: Inicia o Quiz, conecta ao Banco de dados e gerencia transição entre telas.
BancoDeDados: Gerencia a conexão e consultas ao banco de dados.
Jogador: Gerencia as informações do jogador, como idioma e nome.
MensagensAlemao: Classe filha que guarda todas as mensagens de interação com  usuário em alemão 
MensagensIngles: Classe filha que guarda todas as mensagens de interação com  usuário em inglês 
MensagensPortugues: Classe filha que guarda todas as mensagens de interação com  usuário em português 
MensagensInteracaoUsuario: Classe base para mensagens em diferentes idiomas.
MostrarResultado: Processa o resultado final do quiz, exibe a porcentagem máxima obtida pelo usuário e a pontuação do jogo atual.
Pergunta: Estrutura as questões e as mostra.
Quiz: Controle principal do jogo, incluindo fluxo de perguntas e acúmulo de pontuação.
TelaLogin: Tela de interface para login
TelaPerguntas: Tela de interface para apresentar as perguntas
TelaREsultado: Tela de interface para apresentar o resultado
TelaSelecaoIdioma: Tela de interface para apresentas as opções de idioma
Musica: Acrescenta música de fundo ao quiz em loop. Pode ser ligado e desligado.


Contacto:
Entre em contato para relatar problemas ou sugerir melhorias.
Envie um e-mail para barbara.it.noli@gmail.com
Grata pelo seu feedback!
