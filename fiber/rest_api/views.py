from django.core.urlresolvers import reverse

from djangorestframework.views import View
from djangorestframework.permissions import IsAuthenticated
from djangorestframework.views import ListOrCreateModelView, InstanceModelView

from forms import MovePageForm

from fiber.models import Page

class ApiRoot(View):
    """
    The root view for the rest api.
    """

    permissions = (IsAuthenticated, )
    
    def get(self, request):
        return [{'name': 'pages', 'url': reverse('page-resource-root')},
                {'name': 'page content items', 'url': reverse('page-content-item-resource-root')},
                {'name': 'content items', 'url': reverse('content-item-resource-root')},
                {'name': 'images', 'url': reverse('image-resource-root')},
                {'name': 'files', 'url': reverse('file-resource-root')},
                ]


class PageListView(ListOrCreateModelView):
    permissions = (IsAuthenticated, )


class PageInstanceView(InstanceModelView):
    permissions = (IsAuthenticated, )


class MovePageView(View):

    permissions = (IsAuthenticated, )

    form = MovePageForm

    def get(self, request, pk):
        return 'Exposes the `Page.move_page` method'

    def put(self, request, pk):
        position = self.CONTENT['position']
        target = self.CONTENT['target_node_id']
        page = Page.objects.get(id=pk)
        page.move_page(target, position)