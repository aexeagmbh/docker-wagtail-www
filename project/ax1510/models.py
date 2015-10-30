import django.db.models.options as options
options.DEFAULT_NAMES = options.DEFAULT_NAMES + ('description',)

from wagtail.wagtailcore.models import Page


class Ax1510HomePage(Page):
    pass

    class Meta:
        description = "The top level homepage for AX. Static version from October 15."
        verbose_name = "AX 1510 Static Homepage"
