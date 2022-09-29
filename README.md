![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)

# Stack Underflow - Curso Python - Entrega Final Coderhouse

Video de prueba: <https://www.youtube.com/watch?v=E_s-mRAsok8>

Este proyecto busca reproducir funcionalidades y estructuras de Stack Overflow utilizando Django.

Realizado en conjunto con *Matias Pizzi.*

Aunque no haya un registro de qué hizo cada uno, se puede decir que ambos hicimos de todo un poco. Matias Chavez se enfoco más que nada en desarrollo de las vistas y el CRUD, mientras que Matias Pizzi se enfocó en el desarrollo de los modelos, templates y en unificar las partes.

## *Instalación*

Es necesario tener instalado Python previamente.

### 1- Clona este repositorio

`git clone https://github.com/racomaty/Stack-Underflow`

### 2- Instala los requerimientos

`pip install -r requirements.txt`

### 3- Migra la base de datos

`py manage.py migrate`

### 4- Crea un superuser

`python manage.py createsuperuser`

### 5- Inicia el servidor

`python manage.py runserver`
