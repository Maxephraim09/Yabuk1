from django.db import models


class ContactMessage(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    subject = models.CharField(max_length=150)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.subject}"


class SiteSnippet(models.Model):
    key = models.SlugField(unique=True)
    group = models.CharField(max_length=80)
    label = models.CharField(max_length=160)
    value = models.TextField(blank=True)
    sort_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["group", "sort_order", "label"]

    def __str__(self):
        return f"{self.group} - {self.label}"


class SiteImage(models.Model):
    key = models.SlugField(unique=True)
    group = models.CharField(max_length=80)
    label = models.CharField(max_length=160)
    alt_text = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to="site/", blank=True, null=True)
    fallback_static = models.CharField(max_length=255, blank=True)
    sort_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["group", "sort_order", "label"]

    def __str__(self):
        return f"{self.group} - {self.label}"


class BlogPost(models.Model):
    title = models.CharField(max_length=180)
    slug = models.SlugField(unique=True)
    category = models.CharField(max_length=80, blank=True)
    excerpt = models.CharField(max_length=300, blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to="blog/", blank=True, null=True)
    image_path = models.CharField(max_length=255, blank=True, default="img/blog-1.jpg")
    is_published = models.BooleanField(default=True)
    sort_order = models.PositiveIntegerField(default=0)
    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["sort_order", "-published_at", "title"]

    def __str__(self):
        return self.title
