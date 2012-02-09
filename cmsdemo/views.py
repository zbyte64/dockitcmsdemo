from dockitcms.models import ViewPoint

from dockit.views import ListView

class ViewPointListingView(ListView):
    document = ViewPoint
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        data = super(ViewPointListingView, self).get_context_data(**kwargs)
        data['view_points'] = data['object_list']
        return data

home = ViewPointListingView.as_view()
