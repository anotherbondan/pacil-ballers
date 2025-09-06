
# pacil-ballers

### Step-by-step melengkapi checklist

- Membuat sebuah proyek Django baru
  - Membuat direktori baru untuk pacil-ballers
    ```bash
    #Buat direktori
    mkdir pacil-ballers
    
    #Pindah root direktori
    cd pacil-ballers
    
    #Buka VSCode
    code . 
    ```
  - Mengaktifkan virtual environment
    ```bash
    #Buat virtual env
    python -m venv env

    #Aktifkan virtual env
    source env/Scripts/activate
    ```
  - Menyiapkan dan meng-install dependencies
    ```txt
    #requirements.txt
    django
    gunicorn
    whitenoise
    psycopg2-binary
    requests
    urllib3
    python-dotenv
    ```
    ```bash
    #Install dependencies
    pip install -r requirements.txt
    ```
  - Inisialisasi proyek Django
    ```bash
    django-admin startproject pacil-ballers .
    ```
- Membuat aplikasi dengan nama main pada proyek tersebut
    - Inisiasi aplikasi
      ```bash
      python manage.py startapp main
      ```
    - Menambahkan main ke settings.py
      ```python
      INSTALLED_APPS = [..., 'main']
      ```
-  Melakukan routing pada proyek agar dapat menjalankan aplikasi main
    - Membuat folder templates dan file main.html di dalamnya
      ```html
      <h1>{{app}}</h1>
      <h2>{{name}}</h2>
      <p>{{class}}</p>
      ```
    - Menambahkan path pada urls.py
      ```python
      from django.urls import path
      from main.views import show_main
      
      app_name = 'main'
      
      urlpatterns = [
          path('', show_main, name='show_main'),
      ]
      ```
