from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext_lazy as _

from .models import AboutMeModel, ContainerModel


@plugin_pool.register_plugin
class ContainerModelPlugin(CMSPluginBase):
    model = ContainerModel
    name = _("POT-002 CMSPlugin Container")
    render_template = "container/container.html"
    cache = False
    allow_children = True
    child_classes = ["AboutMeModelPlugin"]

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context


@plugin_pool.register_plugin
class AboutMeModelPlugin(CMSPluginBase):
    model = AboutMeModel
    name = _("POT-003 CMSPlugin About me")
    render_template = "child_templates/about_me.html"
    cache = False
    require_parent = True
    parent_classes = ["ContainerModelPlugin"]

    def render(self, context, instance, placeholder):
        return super(AboutMeModel, self).render(context, instance, placeholder)
