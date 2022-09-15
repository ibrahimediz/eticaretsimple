# Env Kurulumu
########################
## MAC
1. python3 -m venv env <br>
Aktif hale getirmek için 
2. source env/bin/activate
########################
## Windows
1. python -m venv env <br>
Aktif Hale Getirmek için
2. env\Scripts\activate
########################
# Kütüphanelerin Listesini Alırken
pip freeze > requirements.txt
# Kütüphane listesini env içerisine kurabilmek için
pip install -r requirements.txt