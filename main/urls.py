from django.urls import path
from main.views import show_main, show_json, show_json_by_id, show_xml, show_xml_by_id, create_product, show_product, login_user, logout_user, register, edit_product, delete_product, add_product_ajax, delete_product_ajax, edit_product_ajax, login_ajax, register_ajax, proxy_image, create_news_flutter

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('create-product/', create_product, name='create_product'),
    path('show-product/<str:id>', show_product, name='show_product'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register, name='register'),
    path('product/<uuid:id>/edit/', edit_product, name='edit_product'),
    path('product/<uuid:id>/delete/', delete_product, name='delete_product'),
    path('login-ajax/', login_ajax, name='login_ajax'),
    path('register-ajax/', register_ajax, name='register_ajax'),
    path('create-product-ajax/', add_product_ajax, name='add_product_ajax'),
    path('edit-product-ajax/<uuid:id>/', edit_product_ajax, name='edit_product_ajax'),
    path('delete-product-ajax/<uuid:id>/', delete_product_ajax, name='delete_product_ajax'),
    path('proxy-image/', proxy_image, name='proxy_image'),
    path('create-flutter/', create_news_flutter, name='create_news_flutter'),
]