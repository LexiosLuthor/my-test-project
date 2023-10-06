from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

# Определение собственного обработчика ошибки 404
def custom_404(request, exception):
    return render(request, '404.html', status=404)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('menu_app.urls')),
]

# Привязка собственного обработчика ошибки 404
handler404 = custom_404
