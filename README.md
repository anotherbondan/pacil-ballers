
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
    ```bash
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
