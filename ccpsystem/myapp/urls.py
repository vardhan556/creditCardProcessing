from .views import *


from django.urls import path

urlpatterns = [
    path('',home_page,name='home_page'),
    path('register/',register_user,name='register_user'),
    path('success/',success_page,name='success_page'),
    path('login/',login_user,name='login_user'),
    path('login_page/',login_page,name='login_page'),
    path('addaccounts/',add_account,name='add_account'),
    path('buyproduct/',buy_product,name='buy_product'),
    # path('selectaccount/',select_account,name='select_account'),
    path('transaction/',transaction,name='transaction'),
    # path('billpayment/',bill_payment,name='bill_payment'),
]