First Django project which had a practical learning purpouse.

To run the project in you PC:<br>
● pip install -r requirements.txt (to install dependencies).<br>
● python manage.py makemigrations (to create migrations).<br>
● python manage.py migrate (to send those migrations to db).<br>
● python manage.py runserver (to run test Django server)<br>
● See your project at http://localhost:8080 (default).<br>

References:<br>
"django-de-a-a-z..." = pág. 136<br>
"EBOOK-PythonAcademy..." = pág. 27<br>

Procedimentos:<br>
Feitas instalações (Python 3.11, pip, django, virtualenv, )<br>

Criado projeto no Django ("videoteca")<br>
  *Criar regras de negócio<br>
Arquivos de configuração do projeto (settings.py, development.py, production.py, testing.py, __init__.py)<br>
  *Pequisar como usar o SQLlite no Python<br>
  *Criar pastas sugeridas pelo "EBOOK"<br>
Criação do runserver e teste no localhost:8080<br>
Criação e configuração dos ambientes de um projeto Django (testing, production e development)<br>
Feita migração<br>
Criação e configuração do superuser (nfthiago, nfthiago@gmail.com, Videoteca123!)<br>
Criada a primeira app (aplicação) chamada "movieSearch"<br>
Feitas algumas configurações (criada pasta "models" e arquivos "__init__.py" e "Profile.py".<br>
Configurado arquivo "Profile.py"<br>
Configurado arquivo "__init__.py" com alteração nas "ROLE_CHOICE" - Médico por Filme e Paciente por Cliente<br>
Feito o "makemigrations" para criar o arquivo "001_initial.py" e depois o comando "migrate" para criar a tabela na bd.<br>
Edição do perfil do utilizador admin "nfthiago"<br>
Criação de um novo utilizador "Aline"<br>
Models criadas e quais elas substituem:<br>
Genre.py - (substitui "Speciality")<br>
DayWeek.py<br>
State.py<br>
City.py<br>
Neighborhood.py<br>
Address.py<br>
Rating.py<br>

Modelos adicionadas ao "__init__.py"<br>
Feito o "makemigrations" para criar o arquivo "0002_city_dayweek_genre_state_rating_neighborhood_and_more" e depois o comando "migrate" para criar a tabela na bd.<br>
Criados alguns "inserts", diretamente no site (/admin) para as tabelas recentemente criadas.<br>
Criado "Movie.py" e feito migration e migrate<br>

Feito a primeira versão do projeto no Github
