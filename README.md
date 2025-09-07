
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
  - Menyiapkan dependencies pada requirements.txt
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
  - Instalasi dependencies dari requirements.txt
    ```bash
    #Install dependencies
    pip install -r requirements.txt
    ```
  - Inisialisasi proyek Django
    ```bash
    django-admin startproject pacil-ballers .
    ```
  - Buat file .env dan .env.prod pada root proyek
    ```
    #.env
    PRODUCTION=False
    ```
    ```
    #.env.prod
    DB_NAME=<nama database>
    DB_HOST=<host database>
    DB_PORT=<port database>
    DB_USER=<username database>
    DB_PASSWORD=<password database>
    SCHEMA=tugas_individu
    PRODUCTION=True
    ```
  - Tambahkan kode berikut pada settings.py untuk menggunakan environment variables
    ```
    #settings.py  
    import os
    from dotenv import load_dotenv
    load_dotenv()
    ```
  - Konfigurasi DEBUG mode untuk keperluan development
    ```python
    PRODUCTION = os.getenv('PRODUCTION', 'False').lower() == 'true'
    ```
  - Konfigurasi DATABASE untuk development
    ```python
    if PRODUCTION:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': os.getenv('DB_NAME'),
                'USER': os.getenv('DB_USER'),
                'PASSWORD': os.getenv('DB_PASSWORD'),
                'HOST': os.getenv('DB_HOST'),
                'PORT': os.getenv('DB_PORT'),
                'OPTIONS': {
                    'options': f"-c search_path={os.getenv('SCHEMA', 'public')}"
                }
            }
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
        }
    ```
  - Lakukan migrasi database
     ```bash
     python manage.py migrate
     ```
  - Jalankan proyek secara lokal
    ```bash
    python manage.py runserver
    ```
- Membuat aplikasi dengan nama main pada proyek tersebut
    - Inisiasi aplikasi
      ```bash
      python manage.py startapp main
      ```
-  Melakukan routing pada proyek agar dapat menjalankan aplikasi main
    - Menambahkan main ke settings.py
      ```python
      INSTALLED_APPS = [..., 'main']
      ```
- Membuat model pada aplikasi main dengan nama Product serta atributnya pada models.py
   ```python
      #models.py
      import uuid
      from django.db import models
      
      class Product(models.Model):
          CATEGORY_CHOICES = [
              ('boots', 'Boots'),
              ('jersey', 'Jersey'),
              ('ball', 'Ball'),
              ('other', "Other")
          ]
    
      id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
      name = models.CharField(max_length=255)
      price = models.IntegerField()
      description = models.TextField()
      thumbnail = models.URLField(blank=True, null=True)
      category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
      is_featured = models.BooleanField(default=False)
      
      def __str__(self):
          return self.name
   ```
- Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
  - Membuat folder templates dan file main.html di dalamnya
      ```html
      <!--main.html-->
      <h1>{{app}}</h1>
      <h2>{{name}}</h2>
      <p>{{class}}</p>
      ```
  - Membuat fungsi pada views.py
    ```python
    #views.py
    from django.shortcuts import render
    
    def show_main(request):
        context = {
            'app': 'Pacil Ballers',
            'name': 'Ananda Gautama Sekar Khosmana',
            'class': 'PBP D'
        }
    
        return render(request, "main.html", context)
    ```
- Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
  ```python
      #urls.py
      from django.urls import path
      from main.views import show_main
      
      app_name = 'main'
      
      urlpatterns = [
          path('', show_main, name='show_main'),
      ]
  ```
- Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
  - Buat proyek baru di PWS dan setup environment variable nya
  - Menambahkan url deployment ke ALLOWED_HOST di settings.py
    ```python
    ALLOWED_HOSTS = [..., "ananda-gautama-pacilballers.pbp.cs.ui.ac.id"]
    ```
  - Deploy aplikasi ke PWS
    ```bash
    git remote add pws <link_proyek>
    git branch -M main
    git push pws main
    ```

### Alur Workflow Django
<img width="1920" height="1080" alt="django-workflow" src="https://github.com/user-attachments/assets/430c228a-4b2e-49f5-b2d5-93cde5d43a9e" />
Ketika user mengakses URL, request akan dikirimkan ke web server lalu diteruskan ke Django. Django akan memproses request melalui urls.py untuk mencocokkan pola URL dengan fungsi atau class view yang sesuai. Jika ada parameter pada URL, urls.py akan mengekstraknya dan meneruskannya ke views.py.

Di dalam views.py, request akan diproses: argumen divalidasi, logika bisnis dijalankan, dan jika diperlukan, data akan diambil atau diperbarui melalui models.py dengan bantuan Django ORM.

Hasil pengolahan data dari view kemudian akan dirender menggunakan template (HTML page) yang sesuai. Template ini berisi kombinasi antara HTML statis dan data dinamis dari view.

Akhirnya, Django mengembalikan hasil render tersebut sebagai HTTP response kepada user melalui browser.

### Peran settings.py pada proyek Django
settings.py merupakan file yang digunakan untuk melakukan konfigurasi terhadap proyek django. settings.py merupakan file yang digunakan untuk melakukan konfigurasi terhadap proyek Django. File ini berisi pengaturan penting seperti konfigurasi database, daftar aplikasi yang digunakan, middleware, lokasi template dan file statis, secret key, mode debug, daftar host yang diizinkan, serta pengaturan bahasa dan zona waktu. Semua komponen utama dalam proyek Django mengacu pada file ini agar dapat berjalan sesuai dengan kebutuhan developer.

### Cara kerja migrasi database di Django
Migrasi database pada Django merupakan mekanisme untuk menjaga kesesuaian antara definisi model di dalam kode program dengan struktur database yang digunakan. Proses ini dimulai ketika pengembang membuat atau memodifikasi model di file models.py. Perubahan tersebut belum langsung diterapkan ke database, sehingga perlu menjalankan perintah berikut. 
```bash
python manage.py makemigrations 
```
Perintah ini akan menghasilkan file migrasi yang berisi instruksi Python untuk merepresentasikan perubahan pada struktur database, misalnya pembuatan tabel baru, penambahan kolom, atau perubahan tipe data. Kemudian, jalankan perintah berikut ini.
```bash
python manage.py migrate
```
Perintah ini berfungsi untuk menerapkan instruksi dalam file migrasi ke database sebenarnya. Pada tahap ini Django akan mengeksekusi perintah SQL yang sesuai dengan isi file migrasi, sehingga struktur database berubah mengikuti definisi model terbaru. Mekanisme ini memudahkan pengembang untuk mengelola perubahan skema database secara teratur, konsisten, dan terdokumentasi dengan baik tanpa perlu menulis query SQL secara manual.

### Mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
