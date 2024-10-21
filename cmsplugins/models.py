from cms.models.pluginmodel import CMSPlugin
from colorfield.fields import ColorField
from django.db import models
from django.utils.translation import gettext as _
from djangocms_text.fields import HTMLField
from filer.fields.image import FilerImageField

from .utils import COLOR_PALETTE


class ContainerModel(CMSPlugin):
    title = models.CharField(_("Titel eingeben"), max_length=50)
    background_color = ColorField(
        _("Farbe auswählen"), choices=COLOR_PALETTE, default="#000000"
    )

    def __str__(self):
        return self.title


class AboutMeModel(CMSPlugin):
    text = HTMLField(blank=True)
    image = FilerImageField(related_name="images", blank=True, on_delete=models.CASCADE)
    background_color = ColorField(
        _("Hintergrundfarbe auswählen"), choices=COLOR_PALETTE, default="#FFFFFF"
    )

    def __str__(self):
        return self.text


class CodingSkillsmodel(CMSPlugin):
    text = HTMLField(blank=True, null=True)
    icon_url = models.URLField(_("Icon Urleinfügen"), max_length=200)

    def __str__(self):
        return self.text


# Create your models here.
