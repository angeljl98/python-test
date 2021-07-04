echo "ir a directorio de django"
cd C:\Users\Dell\Documents\django-dolar
echo "activar Django"
django-dolar\Scripts\activate.bat
echo "instalar Django en la version de lanzamiento"
py -m pip install Django
echo "version de Django"
django-admin --version
django-admin startproject Dolartomorrow
echo "entrar al proyecto Dolartomorrow"
cd Dolartomorrow
echo pedir informacion del archivo manage
manage.py help
