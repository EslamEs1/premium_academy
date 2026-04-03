from django.apps import apps
from django.core.exceptions import AppRegistryNotReady
from django.db.utils import OperationalError, ProgrammingError


def get_model(model_or_label):
    if isinstance(model_or_label, str):
        return apps.get_model(model_or_label)
    return model_or_label


def get_singleton_instance(model_or_label, *, select_related=None, prefetch_related=None):
    """Return the first record for singleton-like models once the table exists."""

    try:
        model = get_model(model_or_label)
    except (LookupError, AppRegistryNotReady):
        return None

    try:
        queryset = model.objects.all()
        if select_related:
            queryset = queryset.select_related(*select_related)
        if prefetch_related:
            queryset = queryset.prefetch_related(*prefetch_related)
        return queryset.first()
    except (OperationalError, ProgrammingError):
        return None


def get_active_ordered_queryset(model_or_label, *, filters=None, select_related=None, prefetch_related=None):
    """Return active ordered querysets for list-like content models."""

    filters = filters or {}

    try:
        model = get_model(model_or_label)
    except (LookupError, AppRegistryNotReady):
        return None

    try:
        queryset = model.objects.filter(is_active=True, **filters)
        if select_related:
            queryset = queryset.select_related(*select_related)
        if prefetch_related:
            queryset = queryset.prefetch_related(*prefetch_related)

        if any(field.name == 'order' for field in model._meta.fields):
            queryset = queryset.order_by('order', 'pk')
        return queryset
    except (OperationalError, ProgrammingError):
        return None


def get_site_settings():
    return get_singleton_instance('main.SiteSettings', prefetch_related=('social_links',))


def site_settings(request):
    return {'site_settings': get_site_settings()}
