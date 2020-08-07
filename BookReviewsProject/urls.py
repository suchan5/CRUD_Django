from django.contrib import admin
from django.urls import path, include
import reviews.views  # 각 app들에 요것도 해줘야함
import forum.views  # 각 app들에 요것도 해줘야함

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('books/', include('books.urls')),
    path('reviews/', reviews.views.index),
    path('forum/', forum.views.index)
]
