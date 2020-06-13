from home.library.Base.base import PageRender
# Create your views here.

def page_search(request):
    class inside_class(PageRender):
        def exec(self):
            A=0
            return self

    return inside_class(request=request,template_url='frontend/search/index.html').exec().render()