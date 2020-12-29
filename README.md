Configurando uma API em *Python* com *Django* e *Django Rest*
---

As configurações a seguir ultilizarão *Django* e *Django Rest*. O *Django* é um framework *Python* feito para facilitar a criação de aplicações web. O *Django Rest* é um framework que se pluga ao *Django* para criar APIS Rest com maior facilidade. Apesar dos nomes parecidos, os projetos são mantidos por equipes completemente distintas, e portanto, não devem ser considerados "a mesma coisa". A seguir deixarei os links das paginas oficiais de ambos os projetos:

* [Página oficial do projeto *Django*](https://www.djangoproject.com/)
* [Página oficial do projeto *Django Rest*](https://www.django-rest-framework.org/)

Preparando o Ambiente de Desenvolvimento - *Python 3.6* no *Ubuntu*
---

1. Crie um diretorio para o projeto:
    ` mkdir [nome_do_diretorio] `.

2. Entre no diretorio criado:
    ` cd [nome_do_diretorio] `.

3. Instale o suporte a criacao e gerenciamento de ambiente virtual (Venv - isola as libs do projeto das do sistema operacional para evitar conflitos) no *Python 3.6*:
    `sudo apt-get install python3.6-venv`.

4. Crie uma nova Venv (ambiente virtual):
	`python3 -m venv [nome_da_venv]`.

5. Ative a Venv criada:
	`source [diretorio_da_venv_criada]/bin/activate`.

6. Com a Venv ativada, agora é hora de instalar o *Django* por meio do pip3 (gerenciador de pacotes do *Python*):
	`pip3 install django`.

7. Com o *Django* instalado, agora é a vez do *Django Rest*:
	`pip3 install djangorestframework`.

8. Voce tambem pode usar para instalart tudo de uma vez um requirements.txt:
    `pip3 install -r requirements.txt`    

9. Com o *Django* instalado, podemos inicializar um projeto *Django* dentro do diretorio raiz do projeto. O ponto (`.`) no final do comando é facultativo, mas ele tem a função de indicar ao *Django* que crie as estruturas do projeto na pasta corrente:
	`django-admin startproject [nome_do_projeto] [.]` .

10. Agora é necessário registrar o *Django Rest* no projeto inicializado anteriormente, para isso você precisa abrir o arquivo `settings.py` e adicionar `'rest_framework'` na lista `INSTALLED_APPS`.

IDE - PyCharm
---

- Voce pode Baixar o [PyCharm](https://www.jetbrains.com/pycharm/) ou simplesmente instalar o pluguin do PyCharm no [Intelij](https://www.jetbrains.com/idea/)

- Importe projeto na IDE

- Configure o SDK. O SDK do projeto deve **ultilizar o interpretador da Venv**, caso contrário a IDE não reconhecerá as dependências instaladas anteriormente: `[diretorio_da_venv]/bin/python`

Comandos Importantes Para o Inicio do Projeto
--

**Atenção: Os comandos a seguir dependem dos frameworks instalados e da venv ativada. Eles serão ultilizados apenas 1 vez - no início do projeto.**

* *Comando createsuperuser (ultilizado para criar o superusuario da aplicacao)*
    `python3 manage.py createsuperuser `.

Comandos Importantes Para Desenvolvimento
---

* Comando which python (importante para verificar se a Venv está ativada):
    `which python`.

* Ativar Venv:
    `source [diretorio_da_venv_criada]/bin/activate` ou 
    `. [diretorio_da_venv_criada]/bin/activate`.	

* Desativar Venv:
    `deactivate`.

* Comando migrate (ultilizado para criar o bancos na aplicacao. Sempre que uma nova app for criada esse comando devera ser disparado):*
    `python3 manage.py migrate`.

* Comando makemigrations (ultilizado para atualizar o banco do projeto):
    `python3 manage.py makemigrations`.
    
* Comando runserver (ultilizado para iniciar o servidor):
    `python3 manage.py runserver`.
    
* Comando startapp (ultilizado para criar apps *Django*):
    `python3 manage.py startapp`.

Dicas de Desenvolvimento
---

* Quando voce criar uma nova app voce deve registra-la colocando seu nome na lista `INSTALLED_APPS`, arquivo `settings.py`, caso contrario o *Django* nao conseguira encontrar sua app e as migracoes nao poderao ser realizadas.

* Sempre que voce criar uma nova app voce deve ter o cuidado de adicionar a pasta migrations no `.gitignore`.

* Sempre que um novo model for criado, lembre-se de registrá-lo no arquivo admin.py da app Exemplo: `admin.site.register(NomeDaClasseDeModelo)`

Deploy
---
python3 manage.py runserver 0.0.0.0:8000