from __future__ import absolute_import, unicode_literals

from django.http import HttpResponse
from django.utils.html import escape
from django.utils.translation import ugettext as _

from debug_toolbar.toolbar import DebugToolbar


def render_panel(request):
    """Render the contents of a panel"""
    # Check if store_id key exist in GET request.
    if not request.GET.has_key('store_id'):
        content = _('"store_id" key is required')
        return HttpResponse(content)

    toolbar = DebugToolbar.fetch(request.GET['store_id'])
    if toolbar is None:
        content = _("Data for this panel isn't available anymore. "
                    "Please reload the page and retry.")
        content = "<p>%s</p>" % escape(content)
    else:
        panel = toolbar.get_panel_by_id(request.GET['panel_id'])
        content = panel.content
    return HttpResponse(content)
