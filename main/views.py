from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'app': 'Pacil Ballers',
        'name': 'Ananda Gautama Sekar Khosmana',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)
