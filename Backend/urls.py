"""
URL configuration for Backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from community import views
from community.views import CommunityForm, Community, CommunityDetail, Main, Fashion, Sell, FashionForm, SellForm, \
    FashionDetail, SellDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', Main.as_view(), name='main'),
    path('community/', Community.as_view(), name='community'),
    path('fashion/', Fashion.as_view(), name='fashion'),
    path('sell/', Sell.as_view(), name='sell'),
    path('communityForm/', CommunityForm.as_view(), name='communityForm'),
    path('fashionForm/', FashionForm.as_view(), name='fashionForm'),
    path('sellForm/', SellForm.as_view(), name='sellForm'),
    path('community/post/<int:boardID>/', CommunityDetail.as_view(), name='detail'),
    path('fashion/post/<int:boardID>/', FashionDetail.as_view(), name='detail'),
    path('sell/post/<int:boardID>/', SellDetail.as_view(), name='detail'),
    path('community/post/<int:boardID>/update', views.community_update, name='update'),
    path('fashion/post/<int:boardID>/update', views.community_update, name='update'),
    path('sell/post/<int:boardID>/update', views.community_update, name='update'),
    path('community/post/<int:boardID>/delete', views.delete, name='delete'),
    path('sell/post/<int:boardID>/delete', views.delete, name='delete'),
    path('fashion/post/<int:boardID>/delete', views.delete, name='delete')
]
