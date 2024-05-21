<h1 align="center">Desafio 3 - 1º Semestre ADS 2024 </h1>

##🎯 Objetivo

Você deve criar uma página da web responsiva, a partir do desafio 2, usando Bootstrap e Flexbox.
Seu objetivo é projetar uma página que se destaque pelo design, usabilidade e responsividade.
Você deve aplicar pelo menos 5 recursos do Bootstrap e usar Flexbox para organizar o conteúdo
de forma eficaz. Seja criativo(a)!


## 📍 Requisitos


•Utilize o framework Bootstrap para criar a estrutura básica da página.
•Aplique o recurso @media para criar um layout responsivo.
•Use pelo menos 5 componentes do Bootstrap (por exemplo, navbar, carrossel, modal, etc.).
•Implemente um menu de navegação que se adapte a diferentes tamanhos de tela.
•Use Flexbox para organizar os elementos em seções da página, como cabeçalho, conteúdo e rodapé.
•Adicione estilos personalizados para tornar a página única. Cadê os alunos criativos!!!
•Certifique-se de que a página seja totalmente responsiva, funcionando bem em telas de tamanhos variados, desde smartphones até desktops.



## ❓ Como usar o site no seu computador

• O Github permite que você baixe os arquivos do projeto como uma pasta zip, o que facilita o acesso à plataforma pelo seu terminal.

• Para baixar, basta clicar em <>Code no GitHub e fazer o download do arquivo zip.

• Para simplificar, mova o arquivo zip para a área de trabalho e extraia-o.

• No explorador de arquivos do seu computador, abra a pasta do projeto e clique na barra de endereço para digitar cmd e abrir o terminal naquela localização.

• Nele, digite os seguintes comandos:

```
1- python -m venv venv 
2- .\venv\Scripts\activate 
3- pip install -r requirements.txt 
4- flask run

```

• Copie o link do site e cole-o em seu navegador.

• Existem dois possíveis erros que podem ocorrer durante essas etapas. O primeiro é a falta de permissão de execução em seu computador. Para corrigir isso, abra o PowerShell do seu computador como administrador e digite os seguintes comandos:

```
1- Set-ExecutionPolicy -ExecutionPolicy AllSigned

2- Pressione 'S' e 'Enter' para confirmar.


```

Para Linux

Va ate a pasta do projeto

```
sudo apt install python3-pip
sudo apt install python3-venv
python3 -m venv venv
source venv/bin/activate
pip install flask_mysqldb
sudo apt install python3-dev default-libmysqlclient-dev build-essential pkg-config


```

Rodando Via AWS

flask run --host=0.0.0.0