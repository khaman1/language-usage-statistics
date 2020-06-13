from api.library.Base.base import APIBase
from .library.research import research_website 
from api.core.constants import REDIS_EXPIRATION_LEVEL_2
import pandas as pd

def api_show_language_usage(request):
    class inside_class(APIBase):
        redis_expiration = REDIS_EXPIRATION_LEVEL_2
        
        def sort_histogram(self):
            ##
            histogram   = pd.DataFrame(self.context['histogram'].items(), columns=['word','count'])
            histogram.sort_values(by='count', ascending=False,inplace=True)

            ##
            self.context['histogram']=[]
            for i in range(0, min(100, len(histogram))): ## Because we only need top 100 occurences
                key         = histogram.iloc[i].values[0]
                value       = histogram.iloc[i].values[1]
                
                self.context['histogram'].append({
                    'word':     key,
                    'count':    int(value),
                })

        def step1(self):
            website_url                 = self.request.GET.get('url','https://vnexpress.net')
            self.context['histogram']   = research_website(website_url)
            self.sort_histogram()


    return inside_class(request=request,enable_redis=1).exec()