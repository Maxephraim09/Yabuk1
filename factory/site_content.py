from django.templatetags.static import static

from .models import BlogPost, SiteImage, SiteSnippet


DEFAULT_SNIPPETS = [
    # Home
    {"key": "home_hero1_kicker", "group": "Home", "label": "Hero Slide 1 Kicker", "value": "Pure Water, Trusted Daily", "sort_order": 1},
    {"key": "home_hero1_title", "group": "Home", "label": "Hero Slide 1 Title", "value": "Nigeria's Reliable Table Water Partner", "sort_order": 2},
    {"key": "home_hero1_body", "group": "Home", "label": "Hero Slide 1 Body", "value": "We supply clean, safe, and refreshing table water to homes, offices, events, and retailers across Nigeria. Every pack is produced with care, quality control, and prompt delivery in mind.", "sort_order": 3},
    {"key": "home_hero1_cta_primary", "group": "Home", "label": "Hero Slide 1 Primary CTA", "value": "Order Now", "sort_order": 4},
    {"key": "home_hero1_cta_primary_url", "group": "Home", "label": "Hero Slide 1 Primary URL", "value": "/contact.html", "sort_order": 5},
    {"key": "home_hero1_cta_secondary", "group": "Home", "label": "Hero Slide 1 Secondary CTA", "value": "Learn More", "sort_order": 6},
    {"key": "home_hero1_cta_secondary_url", "group": "Home", "label": "Hero Slide 1 Secondary URL", "value": "/about.html", "sort_order": 7},
    {"key": "home_hero2_kicker", "group": "Home", "label": "Hero Slide 2 Kicker", "value": "Built for everyday hydration", "sort_order": 8},
    {"key": "home_hero2_title", "group": "Home", "label": "Hero Slide 2 Title", "value": "Fresh Water For Every Home And Business", "sort_order": 9},
    {"key": "home_hero2_body", "group": "Home", "label": "Hero Slide 2 Body", "value": "From family use to bulk supply, we provide dependable table water with consistent taste, hygienic handling, and the kind of service customers can rely on.", "sort_order": 10},
    {"key": "home_hero2_cta_primary", "group": "Home", "label": "Hero Slide 2 Primary CTA", "value": "Order Now", "sort_order": 11},
    {"key": "home_hero2_cta_primary_url", "group": "Home", "label": "Hero Slide 2 Primary URL", "value": "/contact.html", "sort_order": 12},
    {"key": "home_hero2_cta_secondary", "group": "Home", "label": "Hero Slide 2 Secondary CTA", "value": "Explore Services", "sort_order": 13},
    {"key": "home_hero2_cta_secondary_url", "group": "Home", "label": "Hero Slide 2 Secondary URL", "value": "/service/", "sort_order": 14},
    {"key": "home_about_badge", "group": "Home", "label": "About Badge", "value": "Trusted Every Day", "sort_order": 15},
    {"key": "home_about_heading", "group": "Home", "label": "About Heading", "value": "Quality Table Water For Nigerian Homes", "sort_order": 16},
    {"key": "home_about_body", "group": "Home", "label": "About Body", "value": "Yubek Table Water is committed to supplying pure, safe, and refreshing drinking water for homes, offices, schools, events, and retailers. We focus on hygienic production, dependable delivery, and customer service that makes hydration simple and stress-free.", "sort_order": 17},
    {"key": "home_about_trust_title", "group": "Home", "label": "Trust Title", "value": "Customer Trust", "sort_order": 18},
    {"key": "home_about_trust_body", "group": "Home", "label": "Trust Body", "value": "Families, businesses, and event planners count on us for clean water and on-time delivery they can depend on.", "sort_order": 19},
    {"key": "home_about_quality_title", "group": "Home", "label": "Quality Title", "value": "Quality Assured", "sort_order": 20},
    {"key": "home_about_quality_body", "group": "Home", "label": "Quality Body", "value": "Every pack is handled with strict quality control and produced to support safe, refreshing daily use.", "sort_order": 21},
    {"key": "home_services_heading", "group": "Home", "label": "Services Heading", "value": "Reliable Water Supply For Every Need", "sort_order": 22},
    {"key": "home_services_subheading", "group": "Home", "label": "Services Subheading", "value": "Our Services", "sort_order": 23},
    {"key": "home_service1_title", "group": "Home", "label": "Service 1 Title", "value": "Home Delivery", "sort_order": 24},
    {"key": "home_service1_body", "group": "Home", "label": "Service 1 Body", "value": "Scheduled delivery of clean table water to apartments, estates, and family homes across Nigeria.", "sort_order": 25},
    {"key": "home_service2_title", "group": "Home", "label": "Service 2 Title", "value": "Bulk Supply", "sort_order": 26},
    {"key": "home_service2_body", "group": "Home", "label": "Service 2 Body", "value": "Consistent bulk supply for offices, hotels, schools, shops, and event venues that need dependable stock.", "sort_order": 27},
    {"key": "home_service3_title", "group": "Home", "label": "Service 3 Title", "value": "Purification Care", "sort_order": 28},
    {"key": "home_service3_body", "group": "Home", "label": "Service 3 Body", "value": "Careful filtration and hygiene checks help every bottle meet the standard your customers expect.", "sort_order": 29},
    {"key": "home_service4_title", "group": "Home", "label": "Service 4 Title", "value": "Clean Taste", "sort_order": 30},
    {"key": "home_service4_body", "group": "Home", "label": "Service 4 Body", "value": "Balanced treatment gives our water a crisp, refreshing taste that suits everyday drinking.", "sort_order": 31},
    {"key": "home_service5_title", "group": "Home", "label": "Service 5 Title", "value": "Customer Focus", "sort_order": 32},
    {"key": "home_service5_body", "group": "Home", "label": "Service 5 Body", "value": "We listen to customer needs and shape our delivery schedules, pack sizes, and service around them.", "sort_order": 33},
    {"key": "home_service6_title", "group": "Home", "label": "Service 6 Title", "value": "Event Supply", "sort_order": 34},
    {"key": "home_service6_body", "group": "Home", "label": "Service 6 Body", "value": "Need water for a wedding, conference, church program, or campaign? We can plan and deliver for it.", "sort_order": 35},
    {"key": "home_products_heading", "group": "Home", "label": "Products Heading", "value": "Table Water Packs For Home And Business Use", "sort_order": 36},
    {"key": "home_products_subheading", "group": "Home", "label": "Products Subheading", "value": "Our Products", "sort_order": 37},
    {"key": "home_product1_small", "group": "Home", "label": "Product 1 Small Label", "value": "2L Single Bottle", "sort_order": 38},
    {"key": "home_product1_title", "group": "Home", "label": "Product 1 Title", "value": "2L Family Pack", "sort_order": 39},
    {"key": "home_product1_price", "group": "Home", "label": "Product 1 Price", "value": "NGN 500", "sort_order": 40},
    {"key": "home_product2_small", "group": "Home", "label": "Product 2 Small Label", "value": "4L Twin Pack", "sort_order": 41},
    {"key": "home_product2_title", "group": "Home", "label": "Product 2 Title", "value": "Office Value Pack", "sort_order": 42},
    {"key": "home_product2_price", "group": "Home", "label": "Product 2 Price", "value": "NGN 900", "sort_order": 43},
    {"key": "home_product3_small", "group": "Home", "label": "Product 3 Small Label", "value": "6L Triple Pack", "sort_order": 44},
    {"key": "home_product3_title", "group": "Home", "label": "Product 3 Title", "value": "Family Stock Pack", "sort_order": 45},
    {"key": "home_product3_price", "group": "Home", "label": "Product 3 Price", "value": "NGN 1,200", "sort_order": 46},
    {"key": "blog_subheading", "group": "Blog", "label": "Blog Subheading", "value": "Insights", "sort_order": 1},
    {"key": "blog_heading", "group": "Blog", "label": "Blog Heading", "value": "Water Tips And Company Updates", "sort_order": 2},
    # About
    {"key": "about_badge", "group": "About", "label": "About Badge", "value": "Trusted Every Day", "sort_order": 1},
    {"key": "about_heading", "group": "About", "label": "About Heading", "value": "Quality Table Water For Nigerian Homes", "sort_order": 2},
    {"key": "about_body", "group": "About", "label": "About Body", "value": "Yubek Table Water is committed to supplying pure, safe, and refreshing drinking water for homes, offices, schools, events, and retailers. We focus on hygienic production, dependable delivery, and customer service that makes hydration simple and stress-free.", "sort_order": 3},
    {"key": "about_trust_title", "group": "About", "label": "Trust Title", "value": "Customer Trust", "sort_order": 4},
    {"key": "about_trust_body", "group": "About", "label": "Trust Body", "value": "Families, businesses, and event planners count on us for clean water and on-time delivery they can depend on.", "sort_order": 5},
    {"key": "about_quality_title", "group": "About", "label": "Quality Title", "value": "Quality Assured", "sort_order": 6},
    {"key": "about_quality_body", "group": "About", "label": "Quality Body", "value": "Every pack is handled with strict quality control and produced to support safe, refreshing daily use.", "sort_order": 7},
    {"key": "about_cta", "group": "About", "label": "About CTA", "value": "Learn More", "sort_order": 8},
    # Services
    {"key": "services_heading", "group": "Services", "label": "Services Heading", "value": "Reliable Water Supply For Every Need", "sort_order": 1},
    {"key": "services_subheading", "group": "Services", "label": "Services Subheading", "value": "Our Services", "sort_order": 2},
    {"key": "services_home_title", "group": "Services", "label": "Home Delivery Title", "value": "Home Delivery", "sort_order": 3},
    {"key": "services_home_body", "group": "Services", "label": "Home Delivery Body", "value": "Scheduled delivery of clean table water to apartments, estates, and family homes across Nigeria.", "sort_order": 4},
    {"key": "services_bulk_title", "group": "Services", "label": "Bulk Supply Title", "value": "Bulk Supply", "sort_order": 5},
    {"key": "services_bulk_body", "group": "Services", "label": "Bulk Supply Body", "value": "Consistent bulk supply for offices, hotels, schools, shops, and event venues that need dependable stock.", "sort_order": 6},
    {"key": "services_purification_title", "group": "Services", "label": "Purification Title", "value": "Purification Care", "sort_order": 7},
    {"key": "services_purification_body", "group": "Services", "label": "Purification Body", "value": "Careful filtration and hygiene checks help every bottle meet the standard your customers expect.", "sort_order": 8},
    {"key": "services_clean_title", "group": "Services", "label": "Clean Taste Title", "value": "Clean Taste", "sort_order": 9},
    {"key": "services_clean_body", "group": "Services", "label": "Clean Taste Body", "value": "Balanced treatment gives our water a crisp, refreshing taste that suits everyday drinking.", "sort_order": 10},
    {"key": "services_focus_title", "group": "Services", "label": "Customer Focus Title", "value": "Customer Focus", "sort_order": 11},
    {"key": "services_focus_body", "group": "Services", "label": "Customer Focus Body", "value": "We listen to customer needs and shape our delivery schedules, pack sizes, and service around them.", "sort_order": 12},
    {"key": "services_event_title", "group": "Services", "label": "Event Supply Title", "value": "Event Supply", "sort_order": 13},
    {"key": "services_event_body", "group": "Services", "label": "Event Supply Body", "value": "Need water for a wedding, conference, church program, or campaign? We can plan and deliver for it.", "sort_order": 14},
    # Footer
    {"key": "footer_description", "group": "Footer", "label": "Brand Description", "value": "Pure, safe, and refreshing table water for homes, offices, and events across Nigeria. We deliver quality you can taste and service you can trust.", "sort_order": 1},
    {"key": "footer_about_heading", "group": "Footer", "label": "About Links Heading", "value": "About Us", "sort_order": 2},
    {"key": "footer_about_link1", "group": "Footer", "label": "About Link 1", "value": "Why Choose Us", "sort_order": 3},
    {"key": "footer_about_link2", "group": "Footer", "label": "About Link 2", "value": "Service Details", "sort_order": 4},
    {"key": "footer_about_link3", "group": "Footer", "label": "About Link 3", "value": "Delivery Services", "sort_order": 5},
    {"key": "footer_about_link4", "group": "Footer", "label": "About Link 4", "value": "Contact Us", "sort_order": 6},
    {"key": "footer_about_link5", "group": "Footer", "label": "About Link 5", "value": "Terms & Conditions", "sort_order": 7},
    {"key": "footer_hours_heading", "group": "Footer", "label": "Hours Heading", "value": "Business Hours", "sort_order": 8},
    {"key": "footer_hours_mon_fri_label", "group": "Footer", "label": "Mon-Fri Label", "value": "Mon - Friday:", "sort_order": 9},
    {"key": "footer_hours_mon_fri_value", "group": "Footer", "label": "Mon-Fri Value", "value": "08.00 am to 07.00 pm", "sort_order": 10},
    {"key": "footer_hours_sat_label", "group": "Footer", "label": "Saturday Label", "value": "Saturday:", "sort_order": 11},
    {"key": "footer_hours_sat_value", "group": "Footer", "label": "Saturday Value", "value": "09.00 am to 05.00 pm", "sort_order": 12},
    {"key": "footer_hours_sun_label", "group": "Footer", "label": "Sunday Label", "value": "Sunday:", "sort_order": 13},
    {"key": "footer_hours_sun_value", "group": "Footer", "label": "Sunday Value", "value": "Closed", "sort_order": 14},
    {"key": "footer_contact_heading", "group": "Footer", "label": "Contact Heading", "value": "Contact Info", "sort_order": 15},
    {"key": "footer_contact_address", "group": "Footer", "label": "Contact Address", "value": "Lagos, Nigeria", "sort_order": 16},
    {"key": "footer_contact_email1", "group": "Footer", "label": "Contact Email 1", "value": "info@acuastablewater.com", "sort_order": 17},
    {"key": "footer_contact_email2", "group": "Footer", "label": "Contact Email 2", "value": "sales@acuastablewater.com", "sort_order": 18},
    {"key": "footer_contact_phone1", "group": "Footer", "label": "Contact Phone 1", "value": "+234 801 234 5678", "sort_order": 19},
    {"key": "footer_contact_phone2", "group": "Footer", "label": "Contact Phone 2", "value": "+234 809 876 5432", "sort_order": 20},
    # Contact
    {"key": "contact_heading", "group": "Contact", "label": "Contact Heading", "value": "Contact Yubek Table Water", "sort_order": 1},
    {"key": "contact_subheading", "group": "Contact", "label": "Contact Subheading", "value": "Have a question, need a refill, or want a delivery quote? Reach out to our team and we will respond quickly with the support you need.", "sort_order": 2},
    {"key": "contact_address", "group": "Contact", "label": "Contact Address", "value": "Lagos, Nigeria", "sort_order": 3},
    {"key": "contact_email", "group": "Contact", "label": "Contact Email", "value": "info@acuastablewater.com", "sort_order": 4},
    {"key": "contact_phone", "group": "Contact", "label": "Contact Phone", "value": "(+234) 801 234 5678", "sort_order": 5},
]

DEFAULT_IMAGES = [
    {"key": "home_hero1_image", "group": "Home", "label": "Hero Slide 1 Image", "alt_text": "Yubek Table Water hero slide 1", "fallback_static": "img/carousel-1.jpg", "sort_order": 1},
    {"key": "home_hero2_image", "group": "Home", "label": "Hero Slide 2 Image", "alt_text": "Yubek Table Water hero slide 2", "fallback_static": "img/carousel-2.jpg", "sort_order": 2},
    {"key": "home_about_image", "group": "Home", "label": "About Section Image", "alt_text": "Yubek facility and team", "fallback_static": "img/about.jpg", "sort_order": 3},
    {"key": "home_service_image", "group": "Home", "label": "Service Illustration", "alt_text": "Yubek water bottle illustration", "fallback_static": "img/water.png", "sort_order": 4},
    {"key": "home_product1_image", "group": "Home", "label": "Product Card 1 Image", "alt_text": "2L family pack", "fallback_static": "img/product-3.png", "sort_order": 5},
    {"key": "home_product2_image", "group": "Home", "label": "Product Card 2 Image", "alt_text": "Office value pack", "fallback_static": "img/product-2.png", "sort_order": 6},
    {"key": "home_product3_image", "group": "Home", "label": "Product Card 3 Image", "alt_text": "Family stock pack", "fallback_static": "img/product-1.png", "sort_order": 7},
    {"key": "about_image", "group": "About", "label": "About Page Image", "alt_text": "Yubek team and facility", "fallback_static": "img/about.jpg", "sort_order": 1},
    {"key": "service_image", "group": "Services", "label": "Service Page Image", "alt_text": "Yubek water bottle illustration", "fallback_static": "img/water.png", "sort_order": 1},
]


def ensure_default_snippets():
    for snippet in DEFAULT_SNIPPETS:
        defaults = snippet.copy()
        key = defaults.pop("key")
        SiteSnippet.objects.get_or_create(key=key, defaults=defaults)


def ensure_default_images():
    for image in DEFAULT_IMAGES:
        defaults = image.copy()
        key = defaults.pop("key")
        SiteImage.objects.get_or_create(key=key, defaults=defaults)


def build_site_copy():
    ensure_default_snippets()
    return {snippet.key: snippet.value for snippet in SiteSnippet.objects.all()}


def build_site_images():
    ensure_default_images()
    assets = {}
    for asset in SiteImage.objects.all():
        if asset.image:
            assets[asset.key] = asset.image.url
        elif asset.fallback_static:
            assets[asset.key] = static(asset.fallback_static)
        else:
            assets[asset.key] = ""
    return assets


def build_recent_blog_posts(limit=3):
    return BlogPost.objects.filter(is_published=True)[:limit]
