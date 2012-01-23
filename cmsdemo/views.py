from dockitcms.models import Collection

from dockit.views import ListView

class ViewPointListingView(ListView):
    document = Collection
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        data = super(ViewPointListingView, self).get_context_data(**kwargs)
        data['view_points'] = self.get_view_points(data['object_list'])
        return data
    
    def get_view_points(self, collections):
        #TODO perhaps in the future create a special indexer?
        view_points = list()
        for collection in collections:
            view_points.extend(collection.view_points)
        return view_points

home = ViewPointListingView.as_view()
