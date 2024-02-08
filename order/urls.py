from django.urls import path
from order import views


urlpatterns = [
    path('', views.index,name='index'),
    path('sunil_login', views.sunil_login,name='sunil_login'),
    path('marketing_employee', views.marketing_employee,name='marketing_employee'),
    path('marketing_employee_login', views.marketing_employee_login,name='marketing_employee_login'),
    path('hotel', views.hotel,name='hotel'),
    path('hotel_dashboard', views.hotel_dashboard,name='hotel_dashboard'),
    path('employee', views.employee,name='employee'),
    path('table',views.table,name='table'),
    path('dish_category',views.dish_category , name='dish_category'),
    path('dish',views.dish,name='dish'),
    path('logout',views.logout,name='logout'),
    path('running_table',views.running_table,name='running_table'),
    path('change_color',views.change_color,name='change_color'),
    path('view_order/<int:id>',views.view_order,name='view_order'),
    path('filter_by_category',views.filter_by_category,name='filter_by_category'),
    path('dish_filter',views.dish_filter,name='dish_filter'),
    path('add_to_cart',views.add_to_cart,name='add_to_cart'),
    path('remove_cart',views.remove_cart,name='remove_cart'),
    path('merge_card/<int:table_id>/<int:hotel_id>',views.merge_card,name='merge_card'),
    path('place_order/<int:id>',views.place_order,name='place_order'),
    path('complate_view_order/<int:id>',views.complate_view_order,name='complate_view_order'),
    path('complate_order',views.complate_order,name='complate_order'),
    path('waiter_dashboard', views.waiter_dashboard,name='waiter_dashboard'),
    path('waiter_add_order/<int:id>/',views.waiter_add_order,name='waiter_add_order'),
    path('remove_cart_waiter',views.remove_cart_waiter,name='remove_cart_waiter'),
    path('chef_dashboard', views.chef_dashboard,name='chef_dashboard'),
    path('multiple_select',views.multiple_select,name='multiple_select'),
    path('multiple_order',views.multiple_order,name='multiple_order'),
    path('daily_report',views.daily_report,name='daily_report'),    
    path('profile',views.profile,name='profile'),    
    path('login',views.login,name='login'),
   
]
