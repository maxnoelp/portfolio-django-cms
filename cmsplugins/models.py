from cms.models.pluginmodel import CMSPlugin
from colorfield.fields import ColorField
from django.db import models
from django.utils.translation import gettext as _
from djangocms_text.fields import HTMLField

from .utils import COLOR_PALETTE


class ContainerModel(CMSPlugin):
    title = models.CharField(_("Titel eingeben"), max_length=50)
    background_color = ColorField(
        _("Farbe auswählen"), choices=COLOR_PALETTE, default="#000000"
    )

    def __str__(self):
        return self.title


# Create your models here.
