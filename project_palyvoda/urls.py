from django.contrib import admin
from django.urls import path, include
from calc_app.views import calculator_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('game.urls')),
    path('calc_app/', include('calc_app.urls')),
    # path('', include('home.urls')),
    # path('', include('guessgame.urls')),
    # path('', include('simple_forms.urls'))
]
