from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from .models import TrackingStation
from django.utils.translation import ugettext_lazy as _


class HelloPlugin(CMSPluginBase):
    model = CMSPlugin
    render_template = "cms/plugins/test.html"
    cache = False


class TrackingStations(CMSPluginBase):
    model = TrackingStation
    render_template = "cms/plugins/tracking_stations.html"
    name = "Tracking Stationen"

    def render(self, context, instance, placeholder):
        context = super(TrackingStations, self).render(context, instance, placeholder)
        return context


plugin_pool.register_plugin(TrackingStations)
