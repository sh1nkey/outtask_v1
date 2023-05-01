from django.urls import path

from users.views import LoginUpdate, VUZUpdate, Profile, DeleteOffers, DeleteOrders, PerCabView, \
    LinkUpdate, GiveOrder, RefuseOrder, OrderReady, NotHereOrder, LikeView, NeutralView

urlpatterns= [
    path("profile/", Profile.as_view(), name="profile"), # тут высвечиваются данные и формы для их изменения
    path("personal_cabinet/", PerCabView.as_view(), name="personal_cabinet"), # тут разные таблицы с заказами
    path("login-update/<int:pk>/",  LoginUpdate.as_view(), name="login-update"), # для апдейта данных
    path("vuz-update/<int:pk>/",  VUZUpdate.as_view(), name="vuz-update"),
    path("link-update/<int:pk>/",  LinkUpdate.as_view(), name="link-update"),
    path("offer-delete/<int:pk>/",  DeleteOffers.as_view(), name="deleteoffer"), # для удаление разных заказов
    path("order-delete/<int:pk>/",  DeleteOrders.as_view(), name="deleteorder"),
    path("give_order/<int:pk>/",  GiveOrder.as_view(), name="give-order"), # кнопки для заказчик-исполнитель взаимодействия
    path("refuse/<int:pk>/",  RefuseOrder.as_view(), name="refuse"),
    path("order_ready/<int:pk>/",  OrderReady.as_view(), name="ready"),
    path("order_not_ready/<int:pk>/",  NotHereOrder.as_view(), name="not-ready"),
    path("order_like/<int:pk>/",  LikeView.as_view(), name="like"),
    path("order_neutral/<int:pk>/",  NeutralView.as_view(), name="neutral"),

]