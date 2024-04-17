Projeto de Cadastro e Ativação/Desativação de Restaurantes no App Sabor Express.
Este projeto foi desenvolvido no curso Ptyhon: Criando a sua primeira aplicação da Alura.
O projeto trabalhou o uso das estruturas:
- if/elif e else;
- Explicou como deve se usar o import;
- Uso das funções para melhorar a legibilidade e o reuso do código.
- Utilizou bastante o uso do dicionário para armazenar os dados.
- Implemetou o uso das f-strings.
- utilização da estrutura try e except


A minha versão do projeto tem algumas alterações do que foi proposto.
Eu utilizei o macth em substituição os uso do if/elif e else. Por ser uma estrutura que ainda não tinha utilizado. Aprendi um pouco mais do seu uso. 
Como no programa pedimos que o usuário informe dados para que o programa seja executado corretamente. Utilizei na extrutura Try e except o ValueError para que quando o input tenha que ser um número inteiro e o usuário coloca uma letra ou um float retorne como opção invalida. Assim o programa pode continuar em execução.
No opção de cadastrar fiz algumas alterações do projeto base:
- Utilizei no input o método .title() para que o nome do Restaurante tenha as inicias maiúsculas. Caso o usuário cadestre com todas as letras minúsculas o método ira corrigir.
- Utilizei da estrutura if/else para evitar que insira no sistema restaurante sem nome ou que acidentalmente o usuário aperte a enter e cadestre um restaurante sem nome. Assim, na condicional do if implementei o strip() =="" para verificar se o problema descrito ocorra. Se ocorrer ele informa o erro e retorna ao menu principal.
 - Inclui uma tomada de decisão em  continuar cadastrando mais restaurantes ou não. Evitando assim que o usuário tenha que voltar ao menu principal.
- Inseri também informações adicionais para as telas das opções "Cadastrar Restaurante", "Listar Restaurante" e "Alterar estado do Restaurante".  Para que o usuário saiba o que se espera naquela tela.

Na opção Alternar estado do Restaurante as alterações que fiz foram as mesmas descritas acima com o  uso do title() e strip() e o if e else.

Quando souber mais sobre banco de dado quero implementar a vinculação a ele.
