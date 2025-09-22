
# pacil-ballers
- [Tugas 2](#tugas-2)
- [Tugas 3](#tugas-3)
- [Tugas 4](#tugas-4)
## Tugas 2
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
- Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas
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
- Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py
  ```python
      #urls.py
      from django.urls import path
      from main.views import show_main
      
      app_name = 'main'
      
      urlpatterns = [
          path('', show_main, name='show_main'),
      ]
  ```
- Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet
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
Django merupakan web framework berbasis Python. Menurut saya Django merupakan pilihan yang tepat untuk memulai pembelajaran pengembangan perangkat lunak karena mahasiswa sudah mempelajari Python di DDP1. Mahasiswa dapat fokus untuk mempelajari alur kerja pengembangan web tanpa terkendala bahasa pemrograman yang digunakan. Selain itu, Django menawarkan banyak fitur bawaan yang memudahkan pemula, mulai dari autentikasi, manajemen admin, hingga ORM untuk pengelolaan database, sehingga mahasiswa tidak perlu membangun segalanya dari awal. Django juga menggunakan arsitektur Model–View–Template (MVT) yang membantu mahasiswa dalam memahami pemisahan antara logika bisnis, data, dan tampilan secara terstruktur. Dari sisi teknis, Django memiliki performa yang cukup baik untuk aplikasi skala kecil hingga besar, serta didukung oleh dokumentasi yang lengkap dan mudah dipahami, sehingga sangat mendukung proses pembelajaran yang terarah dan efektif.

### Feedback untuk asdos tutorial 1
Asdos selalu siap menerima pertanyaan ketika sesi tutorial berlangsung. Jawaban yang diberikan juga sudah cukup jelas dan sangat membantu. Semoga performa asdos tetap konsisten untuk sesi tutorial lainnya.

## Tugas 3
### Step-by-step melengkapi checklist
- Menambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID
  ```python
  def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")

  def show_xml_by_id(request, product_id):
      try:
          product_item = Product.objects.filter(pk=product_id)
          xml_data = serializers.serialize("xml", product_item)
          return HttpResponse(xml_data, content_type="application/xml")
      except Product.DoesNotExist:
          return HttpResponse(status=404)
  
  
  def show_json(request):
      product_list = Product.objects.all()
      json_data = serializers.serialize("json", product_list)
      return HttpResponse(json_data, content_type="application/json")
  
  def show_json_by_id(request, product_id):
      try:
          product_item = Product.objects.filter(pk=product_id)
          json_data = serializers.serialize("json", product_item)
          return HttpResponse(json_data, content_type="application/json")
      except Product.DoesNotExist:
          return HttpResponse(status=404)
  ```
- Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 1
  ```python
  urlpatterns = [
      ...
      path('xml/', show_xml, name='show_xml'),
      path('json/', show_json, name='show_json'),
      path('/xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
      path('/json/<str:id>/', show_json_by_id, name='show_json_by_id')
  ]
  ```
- Membuat halaman yang menampilkan data objek model yang memiliki tombol "Add" yang akan redirect ke halaman form, serta tombol "Detail" pada setiap data objek model yang akan menampilkan halaman detail objek
  - Membuat base.html
    ```html
    {% load static %}
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        {% block meta %} {% endblock meta %}
      </head>
    
      <body>
        {% block content %} {% endblock content %}
      </body>
    </html>
    ```
  - Konfigurasi base directory untuk templates
    ```python
    TEMPLATES = [
      ...
            'DIRS': [BASE_DIR / 'templates'],
      ...
    ]
    ```
  - Menambahkan elemen pada main.html
    ```html
    {% extends 'base.html' %}{% block content %}
    <h1>{{app}}</h1>
    <h4>Name: {{name}}</h4>
    <h4>Class: {{class}}</h4>
    
    <a href="{% url 'main:create_product' %}">
      <button>+ Add Product</button>
    </a>
    
    {% if not product_list %}
    <p>Belum ada produk.</p>
    {% else %} 
    {% for product in product_list %}
    <hr />
    {% endblock content %}
    <h3>{{product.name}}</h3>
    <p>
      <b>{{ product.get_category_display }}</b>{% if product.is_featured %} |
      <b>Featured</b>{% endif %} 
    </p>
    {% if product.thumbnail %}
    <img src="{{product.thumbnail}}" alt="{{product.name}}" width="200"/>
    {% endif %}
    <h3><i>IDR {{product.price}}</i></h3>
    <p>{{product.description}}</p>
    <a href="{% url 'main:show_product' product.id %}">
      <button>Show detail</button>
    </a>
    {% endfor %} {% endif %} {% endblock content %}
    ```
- Membuat halaman form untuk menambahkan objek model pada app sebelumnya
  - Membuat forms.py
    ```python
    from django.forms import ModelForm
    from main.models import Product
    
    class ProductForm(ModelForm):
        class Meta:
            model = Product
            fields = ["name", "price", "description", "thumbnail", "category", "is_featured"]
    ```
  - Menambahkan function untuk menambahkan product pada views.py
    ```python
    def create_product(request):
        form = ProductForm(request.POST or None)
        
        if form.is_valid() and request.method == 'POST':
            form.save()
            return redirect('main:show_main')
        
        context = {'form': form}
        return render(request, "create_product.html", context)
    ```
  - Menambahkan url route untuk halaman menambahkan product
    ```python
    urlpatterns = [
    ...
    path('create-product/', create_product, name='create_product')
    ]
    ```
  - Membuat create_product.html
    ```html
    {% extends 'base.html' %} {% block content %}
    <a href="{% url 'main:show_main' %}">
      <button>← Back to home</button>
    </a>
    <h3>Add Product</h3>
    <form method="POST">
      {% csrf_token %}
      <table>
        {{ form.as_table }}
        <tr>
          <td></td>
          <td>
            <input type="submit" value="Add Product" />
          </td>
        </tr>
      </table>
    </form>
    {% endblock content %}
    ```
- Membuat halaman yang menampilkan detail dari setiap data objek model
  - Menambahkan function untuk melihat detail product pada views.py
    ```python
    def show_product(request, id):
        product = get_object_or_404(Product, pk=id)
        
        context = {
            'product': product
        }
        
        return render(request, 'product_detail.html', context)
    ```
  - Menambahkan url route untuk halaman detail product
    ```python
    urlpatterns = [
    ...
        path('show-product/<str:id>', show_product, name='show_product')
    ]
    ```
  - Membuat product_detail.html
    ```html
    {% extends 'base.html' %} {% block content %}
    <a href="{% url 'main:show_main' %}">
      <button>← Back to home</button>
    </a>
    <h3>{{product.name}}</h3>
    
    {% if product.thumbnail %}
    <img src="{{product.thumbnail}}" alt="{{product.name}}" width="200"/>
    {% endif %}
    <h3>
      <i>IDR {{product.price}}</i>
    </h3>
    <p>{{product.description}}</p>
    
    {% endblock content %}
    ```
    
### Mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery sangat penting dalam pengimplementasian sebuah platform karena berperan sebagai jembatan antara database dan client. Dengan mekanisme data delivery yang efektif, data dapat tersedia tepat waktu sehingga mendukung pengambilan keputusan yang cepat dan proses bisnis yang responsif. Selain itu, data delivery mempermudah integrasi antar sistem, serta memastikan setiap bagian memiliki informasi yang sama dan konsisten. Lebih dari itu, data delivery memastikan kualitas dan konsistensi data melalui validasi dan transformasi sebelum diterima pengguna. Tanpa data delivery yang baik, platform berisiko mengalami latensi tinggi, inkonsistensi informasi, dan pengalaman pengguna yang buruk, sehingga keberhasilan implementasi platform dapat terganggu.

### Manakah yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
JSON memiliki kelebihan utama berupa struktur yang ringkas, mudah dibaca, serta efisien dalam ukuran data. Formatnya berbasis objek dengan pasangan key-value sehingga mudah dipahami oleh developer. JSON juga cepat diproses karena parsing-nya lebih ringan dan umumnya sudah didukung secara native, terutama di JavaScript

XML memiliki keunggulan dalam fleksibilitas dan kemampuan mendeskripsikan data yang kompleks. Struktur berbasis tag memungkinkan XML menyimpan data, metadata serta hierarki informasi yang kaya. XML juga mendukung validasi dengan skema (DTD atau XSD) sehingga cocok untuk aplikasi yang membutuhkan keandalan tinggi dalam memastikan format data.

JSON menjadi lebih populer karena memiliki dukungan yang sangat luas dari berbagai teknologi modern. Hampir semua framework web, mobile, maupun database sudah menyediakan dukungan bawaan untuk JSON. Hal tersebut memudahkan integrasi dan pertukaran data di dalam sistem. Selain itu, JSON juga telah menjadi standar utama dalam API modern, seperti REST API, GraphQL, hingga berbagai layanan cloud, yang secara langsung mendorong penggunaannya sebagai format pertukaran data utama di berbagai aplikasi masa kini.

### Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Method is_valid() pada Django forms digunakan untuk memeriksa apakah data input sesuai dengan aturan validasi yang didefinisikan pada form. Method ini mengembalikan True jika semua field valid. Jika ada error, maka akan mengembalikan False. Method ini dibutuhkan untuk memastikan data yang diproses sudah bersih dan valid. Dengan demikian, data aman untuk disimpan ke database.

### Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
csrf_token merupakan mekanisme bawaan Django untuk mencegah Cross-Site Request Forgery (CSRF). Token unik ini disisipkan ke dalam form dan diverifikasi kembali oleh server saat request dikirim, sehingga hanya request dari halaman sah yang diterima. Tanpa csrf_token, server tidak bisa membedakan antara request asli dari user dan request palsu yang dikirim situs berbahaya. Hal ini membuka peluang bagi penyerang untuk mengeksploitasi sesi login user  tanpa sepengetahuan user. Misalnya dengan membuat form tersembunyi yang secara otomatis melakukan transfer uang, mengganti password, atau menghapus data penting.

### Feedback untuk asdos tutorial 2
Asdos selalu siap menerima pertanyaan ketika sesi tutorial berlangsung. Jawaban yang diberikan juga sudah cukup jelas dan sangat membantu.

### Screenshot Postman
- URL: [show_json](https://ananda-gautama-pacilballers.pbp.cs.ui.ac.id/json/)
<img width="1920" height="1128" alt="Screenshot 2025-09-16 192935" src="https://github.com/user-attachments/assets/3766b8ea-437a-4b75-927c-9308281bbe53" />

- URL: [show_json_by_id](https://ananda-gautama-pacilballers.pbp.cs.ui.ac.id/json/1e26463d-1386-47f7-aae9-041c6ea2bc03)
<img width="1920" height="1128" alt="Screenshot 2025-09-16 194953" src="https://github.com/user-attachments/assets/d6102a26-7a00-4c3a-8b7c-ad77408afb2a" />

- URL: [show_xml](https://ananda-gautama-pacilballers.pbp.cs.ui.ac.id/xml/)
<img width="1920" height="1128" alt="Screenshot 2025-09-16 192948" src="https://github.com/user-attachments/assets/3d10ab61-e220-4884-9bcb-43f6a68fc65b" />

- URL: [show_xml_by_id](https://ananda-gautama-pacilballers.pbp.cs.ui.ac.id/xml/1e26463d-1386-47f7-aae9-041c6ea2bc03)
<img width="1920" height="1128" alt="Screenshot 2025-09-16 193932" src="https://github.com/user-attachments/assets/ccca2384-a1a2-4a87-864e-674f50f73643" />


## Tugas 4

### Step-by-step melengkapi checklist
-  Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna mengakses aplikasi sebelumnya sesuai dengan status login/logoutnya
   - Membuat fungsi baru untuk registrasi, login, dan logout
     ```python
     def register(request):
          form = UserCreationForm()
      
          if request.method == "POST":
              form = UserCreationForm(request.POST)
              if form.is_valid():
                  form.save()
                  messages.success(request, 'Your account has been successfully created!')
                  return redirect('main:login')
          context = {'form':form}
          return render(request, 'register.html', context)
      
     def login_user(request): 
         if request.method == 'POST':
             form = AuthenticationForm(data=request.POST)
              
             if form.is_valid():
                 user = form.get_user()
                 login(request, user)
                 response = HttpResponseRedirect(reverse('main:show_main'))
                 response.set_cookie('last_login', str(datetime.datetime.now()))
                 return response
              
         else:
             form = AuthenticationForm(request)
          
         context = {'form': form}
         return render(request, 'login.html', context)
      
     def logout_user(request): 
         logout(request)
         response = HttpResponseRedirect(reverse('main:login'))
         response.delete_cookie('last_login')
         return response
     ```
   - Menambahkan route untuk masing-masing function
     ```python
     urlpatterns = [
         ...
         path('login/', login_user, name='login'),
         path('logout/', logout_user, name='logout'),
         path('register/', register, name='register'),
         ...
     ]
     ```
-  Membuat dua (2) akun pengguna dengan masing-masing tiga (3) dummy data menggunakan model yang telah dibuat sebelumnya untuk setiap akun di lokal
   - Buat halaman register.html untuk membuat akun baru
     ```html
     {% extends 'base.html' %} {% block meta %}
     <title>Register</title>
     {% endblock meta %} {% block content %}
      
     <div>
       <h1>Register</h1>
      
       <form method="POST">
         {% csrf_token %}
         <table>
           {{ form.as_table }}
           <tr>
             <td></td>
             <td><input type="submit" name="submit" value="Daftar" /></td>
           </tr>
         </table>
       </form>
      
       {% if messages %}
       <ul>
         {% for message in messages %}
         <li>{{ message }}</li>
         {% endfor %}
       </ul>
       {% endif %}
     </div>
      
     {% endblock content %}
     ```
   - Buat halaman login.html untuk user login
     ```html
     {% extends 'base.html' %} {% block meta %}
     <title>Login</title>
     {% endblock meta %} {% block content %}
     <div class="login">
       <h1>Login</h1>
      
       <form method="POST" action="">
         {% csrf_token %}
         <table>
           {{ form.as_table }}
           <tr>
             <td></td>
             <td><input class="btn login_btn" type="submit" value="Login" /></td>
           </tr>
         </table>
       </form>
     
       {% if messages %}
       <ul>
         {% for message in messages %}
         <li>{{ message }}</li>
         {% endfor %}
       </ul>
       {% endif %} Don't have an account yet?
       <a href="{% url 'main:register' %}">Register Now</a>
     </div>
      
     {% endblock content %}
     ```
   - Jalankan server di local dan buka http://localhost:8000/register
     ```bash
     python manage.py runserver
     ```
   - Masukkan username dan password untuk membuat akun baru
-  Menghubungkan model Product dengan User
   - Menambahkan field user pada model Product sebagai foreign key
   ```python
   ...
   user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
   ...
   ```
   - Lakukan migrasi
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
-  Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last_login pada halaman utama aplikasi
   - Modifikasi function show_main
     ```python
     @login_required(login_url='/login')
     def show_main(request):
         filter_type = request.GET.get("filter", "all")  # default 'all'
     
         if filter_type == "all":
             product_list = Product.objects.all()
         else:
             product_list = Product.objects.filter(user=request.user)
            
         context = {
             'app': 'Pacil Ballers',
             'name': request.user.username,
             'npm': '2406352613',
             'class': 'PBP D',
             'product_list': product_list,
             'last_login': request.COOKIES.get('last_login', 'Never')
         }
    
         return render(request, "main.html", context)
     ```
   - Tambahkan informasi login pada main.html
     ```html
     ...
     <h5>Sesi terakhir login: {{ last_login }}</h5>
     ...
     ```
     
### Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.
Django AuthenticationForm adalah form bawaan Django yang digunakan untuk proses login pengguna. Form ini berfungsi untuk memvalidasi apakah username dan password yang di input user sesuai dengan data pada database.
### Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
### Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
### Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
