<h1 align="center"> Waiter Robot </h1>

## Sobre o Projeto
O Waiter Robot é um projeto desenvolvido pelos alunos Daniel Messias Santos, Thiago Pereira Freire e Vitor Pires Zini para a disciplina de Inteligência Artificial na Universidade Federal de Lavras. Nesse projeto, foi desenvolvido uma versão inicial de um código para um robô que faz o papel de um garçom em um estabelecimento comercial.

## Organização do Código
O projeto foi organizado utilizando o conceito MVC(Model, View, Controller). Na pasta "Controller" está localizado o código "control.py", que realiza as ações necessárias do robô, como andar e falar. Na pasta "View" estão localizados os códigos "act.py" e "sense.py", que fazem as configurações necessárias para o uso da funcionalidade de fala do robô. Fora das pastas, se encontra o programa "main.py", que deve ser executado para rodar o projeto como um todo.

## Principais Bibliotecas Utilizadas
Para a funcionalidade de fala do robô, foram utilizadas as bibliotecas "Speech Recognition" da Google e a biblioteca "Eleven Labs". Para conectar ao robô e enviar os comandos de movimento, foi utilizada a biblioteca "Serial".

## Principais dificuldades
As maiores dificuldades encontradas durante a criação do projeto se tratam de problemas com o robô utilizado. A primeira delas se trata da conexão bluetooth com o robô, uma vez que a conexão necessitava de configurações específicas no computador para aparecer como conexão disponível. O segundo problema se trata de um problema com as rodas do robô; ao comandar ao robô que ele ande para frente, ele faz uma tragetória levemente inclinada para a esquerda, sendo necessárias ajustes durante seu movimento.
