from django.urls import path

from admins import views

urlpatterns = [
    path('dashboard/', views.admin_dashboard),
    path('category_form/', views.categories_form),
    path('get_category/', views.get_category),

    path('show_course/', views.show_course),
    path('show_contact/', views.show_contact),
    path('form/', views.form),
    path('delete_category/<int:categories_id>', views.delete_category),

    path('transform_message/<int:contact_id>', views.mark_as_read),

    path('category_update_form/<int:categories_id>', views.category_update_form)

]