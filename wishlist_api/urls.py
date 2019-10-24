"""wishlist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from items import views as item_views
from api import views as api_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('items/list/', item_views.item_list, name='item-list'),
    path('items/detail/<int:item_id>/', item_views.item_detail, name='item-detail'),
    path('items/wishlist/', item_views.wishlist, name='wishlist' ),

    path('user/register/', item_views.user_register, name='user-register'),
    path('user/login/', item_views.user_login, name='user-login'),
    path('user/logout/', item_views.user_logout, name='user-logout'),

    path('items/<int:item_id>/favorite/', item_views.item_favorite, name='item-favorite'),
    path('api/list/', api_views.ItemListView.as_view(), name='item-api-list'),
    path('api/item/detail/<int:item_id>/', api_views.ItemDetailView.as_view(), name='item-api-detail'),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)