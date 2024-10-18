from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext_lazy as _

from .models import ContainerModel


@plugin_pool.register_plugin
class ContainerModelPlugin(CMSPluginBase):
    model = ContainerModel
    name = _("POT-002 CMSPlugin Container")
    render_template = "container/container.html"
    cache = False
    allow_children = True

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context
