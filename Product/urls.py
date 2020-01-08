from django.urls import path
from .import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.conf.urls.static import static


urlpatterns = [
    path('buy', views.buy, name='buy'),
    path('sell', views.sell, name='sell'),
    path('logout', views.logout, name='logout'),
    path('admin_page', views.admin_page, name='admin_page'),
    path('delete_product', views.delete_product, name='delete_product'),
    path('update_product', views.update_product, name='update_product'),
    path('stuff', views.stuff, name='stuff'),
    path('thanks', views.thanks, name='thanks'),
    path('login_buy', views.login_buy, name='login_buy')

]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
