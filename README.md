
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
    

