from .site_content import build_site_copy, build_site_images


def site_copy(request):
    return {
        "site_copy": build_site_copy(),
        "site_asset_urls": build_site_images(),
    }
