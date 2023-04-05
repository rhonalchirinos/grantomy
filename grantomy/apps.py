from django.utils.translation import gettext_lazy
from . import __version__

try:
    from pretix.base.plugins import PluginConfig
except ImportError:
    raise RuntimeError("Please use pretix 2.7 or above to run this plugin!")


class PluginApp(PluginConfig):
    default = True
    name = "grantomy"
    verbose_name = "Gran Tomy Plugin"

    class PretixPluginMeta:
        name = gettext_lazy("Gran Tomy Plugin")
        author = "Your name Tomy"
        description = gettext_lazy("Short description")
        visible = True
        version = __version__
        category = "API"
        compatibility = "pretix>=2.7.0"

    def ready(self):
        from . import signals  # NOQA


