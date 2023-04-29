from django.shortcuts import render


def hello_rekruto(request):
    template = 'api/hello_rekruto.html'
    name = request.GET.get('name')
    message = request.GET.get('message')
    context = {
        'name': name,
        'message': message,
    }
    return render(request, template, context)
