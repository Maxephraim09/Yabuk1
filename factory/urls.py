from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    # Authentication
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", views.logout_view, name="logout"),

    # Admin
    path("dashboard/", views.admin_dashboard, name="admin_dashboard"),
    path("blog/create/", views.create_blog_post, name="create_blog_post"),
    path("blog/<int:post_id>/update/", views.update_blog_post, name="update_blog_post"),
    path("blog/<int:post_id>/delete/", views.delete_blog_post, name="delete_blog_post"),

    path("products/create/", views.product_create, name="product_create"),
    path("products/<int:product_id>/edit/", views.product_update, name="product_update"),
    path("products/<int:product_id>/delete/", views.product_delete, name="product_delete"),

    path("gallery/create/", views.gallery_create, name="gallery_create"),
    path("gallery/<int:image_id>/edit/", views.gallery_update, name="gallery_update"),
    path("gallery/<int:image_id>/delete/", views.gallery_delete, name="gallery_delete"),

    # Shared updates
    path("snippets/<int:snippet_id>/update/", views.update_snippet, name="update_snippet"),
    path("site-images/<int:image_id>/update/", views.update_site_image, name="update_site_image"),
    path("messages/<int:message_id>/delete/", views.delete_message, name="delete_message"),
    path("messages/<int:message_id>/toggle-read/", views.toggle_message_read, name="toggle_message_read"),

    # Public pages
    path("", views.index, name="index"),
    path("index.html", views.index, name="index_html"),
    path("about/", views.about, name="about"),
    path("about.html", views.about, name="about_html"),
    path("blog/", views.blog, name="blog"),
    path("blog.html", views.blog, name="blog_html"),
    path("contact/", views.contact, name="contact"),
    path("contact.html", views.contact, name="contact_html"),
    path("service/", views.service, name="service"),
    path("service.html", views.service, name="service_html"),
]
