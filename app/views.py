from django.shortcuts import render
from .models import get_random_text
from django.http import HttpRequest, JsonResponse
from django.shortcuts import redirect
from django.contrib.auth import login, logout, authenticate
from .forms import TemplateForm


# def template_view(request):
#     if request.method == "GET":
#         return render(request, 'app/template_form.html')
#
#     if request.method == "POST":
#         received_data = request.POST  # Приняли данные в словарь
#         print(received_data)
#
#         # как пример получение данных по ключу `my_text`
#         # my_text = received_data.get('my_text')
#         return JsonResponse(data=
#                             {
#                                 'my_text': received_data.get('my_text'),
#                                 'my_password': received_data.get('my_password'),
#                                 'my_email': received_data.get('my_email'),
#                                 'my_date': received_data.get('my_date'),
#                                 'my_number': received_data.get('my_number'),
#                                 'my_select': received_data.get('my_select'),
#                                 'my_check': received_data.get('my_checkbox'),
#                                 'about_me': received_data.get('my_textarea'),
#
#                             }, json_dumps_params={'ensure_ascii': False, 'indent': 4})

        # TODO Проведите здесь получение и обработку данных если это необходимо

        # TODO Верните HttpRequest или JsonResponse с данными
def template_view(request):
    if request.method == "GET":
        return render(request, 'app/template_form.html')

    if request.method == "POST":
        received_data = request.POST  # Приняли данные в словарь
        print(received_data)
        form = TemplateForm(received_data)
        if form.is_valid():
            return JsonResponse(data=form.cleaned_data,
                                json_dumps_params={'indent': 4,
                                                   'ensure_ascii': False})
        return render(request, 'app/template_form.html', contex={'form': form})

        # как пример получение данных по ключу `my_text`
        # my_text = received_data.get('my_text')
        # return JsonResponse(data=
        #                     {
        #                         'my_text': received_data.get('my_text'),
        #                         'my_password': received_data.get('my_password'),
        #                         'my_email': received_data.get('my_email'),
        #                         'my_date': received_data.get('my_date'),
        #                         'my_number': received_data.get('my_number'),
        #                         'my_select': received_data.get('my_select'),
        #                         'my_check': received_data.get('my_checkbox'),
        #                         'about_me': received_data.get('my_textarea'),
        #
        #                     }, json_dumps_params={'ensure_ascii': False, 'indent': 4})


def login_view(request):
    if request.method == "GET":
        return render(request, 'app/login.html')

    if request.method == "POST":
        data = request.POST
        user = authenticate(username=data["username"], password=data["password"])
        if user:
            login(request, user)
            return redirect("app:user_profile")
        return render(request, "app/login.html", context={"error": "Неверные данные"})


def logout_view(request):
    if request.method == "GET":
        logout(request)
        return redirect("/")


def register_view(request):
    if request.method == "GET":
        return render(request, 'app/register.html')

    if request.method == "POST":
        return render(request, 'app/register.html')


def index_view(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect("app:user_profile")
        return render(request, 'app/index.html')


def user_detail_view(request):
    if request.method == "GET":
        return render(request, 'app/user_details.html')

def get_text_json(request):
    if request.method == "GET":
        return JsonResponse({"text": get_random_text()},
                            json_dumps_params={"ensure_ascii": False})

