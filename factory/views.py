from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils.text import slugify
from django.views.decorators.http import require_http_methods

from .models import BlogPost, ContactMessage, SiteImage, SiteSnippet
from .site_content import build_recent_blog_posts, ensure_default_images, ensure_default_snippets


def index(request):
    ensure_default_blog_posts()
    recent_posts = build_recent_blog_posts()
    return render(request, "pages/index.html", {"recent_posts": recent_posts})


def about(request):
    return render(request, "pages/about.html")


def blog(request):
    ensure_default_blog_posts()
    posts = BlogPost.objects.filter(is_published=True)
    return render(request, "pages/blog.html", {"posts": posts})


def contact(request):
    form_data = {
        "name": "",
        "email": "",
        "phone": "",
        "subject": "",
        "message": "",
    }

    if request.method == "POST":
        form_data = {
            "name": request.POST.get("name", "").strip(),
            "email": request.POST.get("email", "").strip(),
            "phone": request.POST.get("phone", "").strip(),
            "subject": request.POST.get("subject", "").strip(),
            "message": request.POST.get("message", "").strip(),
        }

        missing_fields = [
            label
            for label, value in (
                ("name", form_data["name"]),
                ("email", form_data["email"]),
                ("subject", form_data["subject"]),
                ("message", form_data["message"]),
            )
            if not value
        ]

        if missing_fields:
            messages.error(request, "Please fill in your name, email, subject, and message before sending.")
            return render(request, "pages/contact.html", {"form_data": form_data})

        ContactMessage.objects.create(**form_data)
        messages.success(request, "Thanks for reaching out. Your message has been received and will be reviewed soon.")
        return redirect("contact_html")

    return render(request, "pages/contact.html", {"form_data": form_data})


def service(request):
    return render(request, "pages/service.html")


def _admin_menu(active_section):
    dashboard_url = reverse("admin_dashboard")
    return [
        {"key": "dashboard", "label": "Dashboard", "url": dashboard_url, "icon": "fa-gauge-high", "note": "Overview"},
        {"key": "frontend", "label": "Home", "url": f"{dashboard_url}#frontend", "icon": "fa-house", "note": "Manage frontend"},
        {"key": "about", "label": "About", "url": f"{dashboard_url}#about", "icon": "fa-circle-info", "note": "Page copy"},
        {"key": "services", "label": "Services", "url": f"{dashboard_url}#services", "icon": "fa-hand-holding-droplet", "note": "Page copy"},
        {"key": "blog", "label": "Blog", "url": f"{dashboard_url}#blog", "icon": "fa-pen-nib", "note": "Posts"},
        {"key": "products", "label": "Products", "url": f"{dashboard_url}#products", "icon": "fa-box", "note": "Product list"},
        {"key": "gallery", "label": "Gallery", "url": f"{dashboard_url}#gallery", "icon": "fa-images", "note": "Image library"},
        {"key": "messages", "label": "Messages", "url": f"{dashboard_url}#messages", "icon": "fa-envelope", "note": "Inbox"},
    ]


def _quick_actions():
    return [
        {"label": "Open Site", "url": reverse("index"), "icon": "fa-globe"},
        {"label": "Open Blog", "url": reverse("blog"), "icon": "fa-book-open"},
    ]


def _admin_context(active_section, page_title, page_intro):
    return {
        "active_section": active_section,
        "admin_menu": _admin_menu(active_section),
        "quick_actions": _quick_actions(),
        "page_title": page_title,
        "page_intro": page_intro,
    }


@login_required
def admin_dashboard(request):
    ensure_default_blog_posts()
    ensure_default_snippets()
    ensure_default_images()

    frontend_snippets = SiteSnippet.objects.filter(group="Home").order_by("sort_order", "label")
    frontend_images = SiteImage.objects.filter(group="Home").order_by("sort_order", "label")
    about_snippets = SiteSnippet.objects.filter(group="About").order_by("sort_order", "label")
    about_images = SiteImage.objects.filter(group="About").order_by("sort_order", "label")
    service_snippets = SiteSnippet.objects.filter(group="Services").order_by("sort_order", "label")
    service_images = SiteImage.objects.filter(group="Services").order_by("sort_order", "label")
    blog_posts = BlogPost.objects.all().order_by("-published_at")
    product_items = SiteImage.objects.filter(group="Product").order_by("sort_order", "label")
    gallery_items = SiteImage.objects.filter(group="Gallery").order_by("sort_order", "label")
    recent_messages = ContactMessage.objects.order_by("-created_at")

    blog_count = BlogPost.objects.count()
    published_post_count = BlogPost.objects.filter(is_published=True).count()
    draft_post_count = BlogPost.objects.filter(is_published=False).count()
    message_count = ContactMessage.objects.count()
    unread_message_count = ContactMessage.objects.filter(is_read=False).count()
    image_count = SiteImage.objects.count()
    active_image_count = SiteImage.objects.filter(is_active=True).count()
    frontend_count = frontend_snippets.count() + frontend_images.count()
    about_count = about_snippets.count() + about_images.count()
    service_count = service_snippets.count() + service_images.count()
    product_count = product_items.count()
    gallery_count = gallery_items.count()

    context = _admin_context(
        active_section="dashboard",
        page_title="Dashboard",
        page_intro="A DattaAble-inspired control center for the Yubek site.",
    )
    context.update(
        {
            "frontend_snippets": frontend_snippets,
            "frontend_images": frontend_images,
            "about_snippets": about_snippets,
            "about_images": about_images,
            "service_snippets": service_snippets,
            "service_images": service_images,
            "blog_posts": blog_posts,
            "product_items": product_items,
            "gallery_items": gallery_items,
            "recent_messages": recent_messages,
            "blog_count": blog_count,
            "published_post_count": published_post_count,
            "draft_post_count": draft_post_count,
            "message_count": message_count,
            "unread_message_count": unread_message_count,
            "image_count": image_count,
            "active_image_count": active_image_count,
            "frontend_count": frontend_count,
            "about_count": about_count,
            "service_count": service_count,
            "product_count": product_count,
            "gallery_count": gallery_count,
        }
    )
    return render(request, "pages/dashboard.html", context)


DEFAULT_BLOG_POSTS = [
    {
        "slug": "clean-water-supports-healthier-families",
        "title": "How clean water supports healthier families",
        "category": "Fresh Supply",
        "excerpt": "Simple hydration habits can improve daily comfort, focus, and overall well-being for every household.",
        "content": "Simple hydration habits can improve daily comfort, focus, and overall well-being for every household. Yubek Table Water keeps families supplied with safe, refreshing water that fits everyday routines.",
        "image_path": "img/blog-1.jpg",
        "sort_order": 1,
    },
    {
        "slug": "what-businesses-should-expect-from-a-water-supplier",
        "title": "What businesses should expect from a water supplier",
        "category": "Delivery Ready",
        "excerpt": "Dependable stock, clear communication, and consistent quality are the real markers of a strong supply partner.",
        "content": "Dependable stock, clear communication, and consistent quality are the real markers of a strong supply partner. Businesses need timely delivery, clean packaging, and a supplier that responds fast when demand changes.",
        "image_path": "img/blog-2.jpg",
        "sort_order": 2,
    },
    {
        "slug": "why-packaging-and-hygiene-matter-in-table-water",
        "title": "Why packaging and hygiene matter in table water",
        "category": "Quality First",
        "excerpt": "Safe handling and neat packaging help protect freshness from the factory to the customer.",
        "content": "Safe handling and neat packaging help protect freshness from the factory to the customer. Clear sealing, clean filling stations, and careful storage all build trust in every bottle we deliver.",
        "image_path": "img/blog-3.jpg",
        "sort_order": 3,
    },
]


def ensure_default_blog_posts():
    for post in DEFAULT_BLOG_POSTS:
        BlogPost.objects.get_or_create(slug=post["slug"], defaults=post)


def unique_blog_slug(title, current_instance=None):
    base_slug = slugify(title) or "blog-post"
    slug = base_slug
    counter = 2
    while BlogPost.objects.filter(slug=slug).exclude(pk=getattr(current_instance, "pk", None)).exists():
        slug = f"{base_slug}-{counter}"
        counter += 1
    return slug


def _save_blog_post_from_request(request, post=None):
    title = request.POST.get("title", "").strip()
    content = request.POST.get("content", "").strip()
    if not title or not content:
        return None, "Please provide both a title and content for the blog post."

    sort_order = request.POST.get("sort_order", "").strip()
    try:
        sort_order_value = int(sort_order) if sort_order else 0
    except ValueError:
        sort_order_value = 0

    target = post or BlogPost()
    target.title = title
    target.slug = unique_blog_slug(title, current_instance=post)
    target.category = request.POST.get("category", "").strip()
    target.excerpt = request.POST.get("excerpt", "").strip()
    target.content = content
    uploaded_image = request.FILES.get("image")
    if uploaded_image:
        target.image = uploaded_image
    target.image_path = request.POST.get("image_path", "").strip() or "img/blog-1.jpg"
    target.is_published = request.POST.get("is_published") == "on"
    target.sort_order = sort_order_value
    target.save()
    return target, None


@login_required
@require_http_methods(["GET", "POST"])
def create_blog_post(request):
    if request.method != "POST":
        return redirect("admin_dashboard")

    post, error = _save_blog_post_from_request(request)
    if error:
        messages.error(request, error)
    else:
        messages.success(request, "Blog post created successfully.")
    return redirect(f"{reverse('admin_dashboard')}#blog")


@login_required
@require_http_methods(["GET", "POST"])
def update_blog_post(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)
    if request.method == "POST":
        updated_post, error = _save_blog_post_from_request(request, post=post)
        if error:
            messages.error(request, error)
            return redirect(f"{reverse('admin_dashboard')}#blog")
        messages.success(request, f"{updated_post.title} was updated successfully.")
        return redirect(f"{reverse('admin_dashboard')}#blog")

    return redirect(f"{reverse('admin_dashboard')}#blog")


@login_required
@require_http_methods(["POST"])
def delete_blog_post(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)
    title = post.title
    post.delete()
    messages.success(request, f"Deleted blog post '{title}'.")
    return redirect(f"{reverse('admin_dashboard')}#blog")


def _save_media_item(request, *, group, item=None):
    label = request.POST.get("label", "").strip()
    if not label:
        return None, "Please provide a label for the image."

    sort_order = request.POST.get("sort_order", "").strip()
    try:
        sort_order_value = int(sort_order) if sort_order else 0
    except ValueError:
        sort_order_value = 0

    target = item or SiteImage()
    target.key = slugify(label) or f"{group.lower()}-image"
    target.group = group
    target.label = label
    target.alt_text = request.POST.get("alt_text", "").strip()
    uploaded_image = request.FILES.get("image")
    if uploaded_image:
        target.image = uploaded_image
    target.sort_order = sort_order_value
    target.is_active = request.POST.get("is_active") == "on"
    target.save()
    return target, None


@login_required
@require_http_methods(["GET", "POST"])
def product_create(request):
    if request.method != "POST":
        return redirect("admin_dashboard")

    item, error = _save_media_item(request, group="Product")
    if error:
        messages.error(request, error)
    else:
        messages.success(request, "Product created successfully.")
    return redirect(f"{reverse('admin_dashboard')}#products")


@login_required
@require_http_methods(["GET", "POST"])
def product_update(request, product_id):
    product = get_object_or_404(SiteImage, pk=product_id, group="Product")
    if request.method == "POST":
        item, error = _save_media_item(request, group="Product", item=product)
        if error:
            messages.error(request, error)
            return redirect(f"{reverse('admin_dashboard')}#products")
        messages.success(request, f"{item.label} was updated successfully.")
        return redirect(f"{reverse('admin_dashboard')}#products")

    return redirect(f"{reverse('admin_dashboard')}#products")


@login_required
@require_http_methods(["POST"])
def product_delete(request, product_id):
    product = get_object_or_404(SiteImage, pk=product_id, group="Product")
    label = product.label
    product.delete()
    messages.success(request, f"Deleted product '{label}'.")
    return redirect(f"{reverse('admin_dashboard')}#products")


@login_required
@require_http_methods(["GET", "POST"])
def gallery_create(request):
    if request.method != "POST":
        return redirect("admin_dashboard")

    item, error = _save_media_item(request, group="Gallery")
    if error:
        messages.error(request, error)
    else:
        messages.success(request, "Gallery image created successfully.")
    return redirect(f"{reverse('admin_dashboard')}#gallery")


@login_required
@require_http_methods(["GET", "POST"])
def gallery_update(request, image_id):
    image = get_object_or_404(SiteImage, pk=image_id, group="Gallery")
    if request.method == "POST":
        item, error = _save_media_item(request, group="Gallery", item=image)
        if error:
            messages.error(request, error)
            return redirect(f"{reverse('admin_dashboard')}#gallery")
        messages.success(request, f"{item.label} was updated successfully.")
        return redirect(f"{reverse('admin_dashboard')}#gallery")

    return redirect(f"{reverse('admin_dashboard')}#gallery")


@login_required
@require_http_methods(["POST"])
def gallery_delete(request, image_id):
    image = get_object_or_404(SiteImage, pk=image_id, group="Gallery")
    label = image.label
    image.delete()
    messages.success(request, f"Deleted gallery image '{label}'.")
    return redirect(f"{reverse('admin_dashboard')}#gallery")


@login_required
@require_http_methods(["POST"])
def update_snippet(request, snippet_id):
    snippet = get_object_or_404(SiteSnippet, pk=snippet_id)
    snippet.label = request.POST.get("label", snippet.label).strip() or snippet.label
    snippet.value = request.POST.get("value", snippet.value).strip()
    snippet.group = request.POST.get("group", snippet.group).strip() or snippet.group
    sort_order = request.POST.get("sort_order", "").strip()
    if sort_order:
        try:
            snippet.sort_order = int(sort_order)
        except ValueError:
            pass
    snippet.is_active = request.POST.get("is_active") == "on"
    snippet.save()

    messages.success(request, f"{snippet.label} was updated successfully.")
    return redirect(request.META.get("HTTP_REFERER", reverse("admin_dashboard")))


@login_required
@require_http_methods(["POST"])
def update_site_image(request, image_id):
    site_image = get_object_or_404(SiteImage, pk=image_id)
    site_image.label = request.POST.get("label", site_image.label).strip() or site_image.label
    site_image.alt_text = request.POST.get("alt_text", site_image.alt_text).strip()
    site_image.group = request.POST.get("group", site_image.group).strip() or site_image.group
    sort_order = request.POST.get("sort_order", "").strip()
    if sort_order:
        try:
            site_image.sort_order = int(sort_order)
        except ValueError:
            pass
    site_image.is_active = request.POST.get("is_active") == "on"
    uploaded_image = request.FILES.get("image")
    if uploaded_image:
        site_image.image = uploaded_image
    site_image.save()

    messages.success(request, f"{site_image.label} was updated successfully.")
    return redirect(request.META.get("HTTP_REFERER", reverse("admin_dashboard")))


@login_required
@require_http_methods(["POST"])
def delete_message(request, message_id):
    message = get_object_or_404(ContactMessage, pk=message_id)
    sender = message.name
    message.delete()
    messages.success(request, f"Deleted message from {sender}.")
    return redirect(f"{reverse('admin_dashboard')}#messages")


@login_required
@require_http_methods(["POST"])
def toggle_message_read(request, message_id):
    message = get_object_or_404(ContactMessage, pk=message_id)
    message.is_read = not message.is_read
    message.save(update_fields=["is_read"])
    state = "read" if message.is_read else "unread"
    messages.success(request, f"Marked message from {message.name} as {state}.")
    return redirect(f"{reverse('admin_dashboard')}#messages")


@login_required
@require_http_methods(["POST"])
def logout_view(request):
    logout(request)
    messages.success(request, "You have been signed out.")
    return redirect("login")
