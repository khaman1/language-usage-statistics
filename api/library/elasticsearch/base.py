from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
from elasticsearch_dsl.query import Q, Bool
from datetime import datetime, timedelta


class elasticsearch_base:
    request                 = ''
    s                       = ''
    result                  = ''
    my_Q                    = ''
    index                   = ''
    client                  = ''

    def __init__(self, host='127.0.0.1:45162', index='', request=''):
        self.check_permission()

        self.client = Elasticsearch(host)
        self.s      = Search(using=self.client, index=index)
        self.index  = index

        if request:
            self.process_request(request)

    def get_raw(self):
        return self.s

    def match_phrase(self, field='', input=[]):
        if not field:
            return

        if type(input) == str:
            input = [input]

        ######################
        ######################)
        exec('self.my_Q = Q("match_phrase", '+field+'="'+input[0]+'")')
        for item in input[1:]:
            exec('self.my_Q |= Q("match_phrase", '+field+'="'+item+'")')

        self.s = self.s.query(self.my_Q)

        return self

    def match(self, field='', input=[]):
        if not field:
            return

        if type(input) == str:
            input = [input]

        ######################
        ######################)
        exec('self.my_Q = Q("match", '+field+'="'+input[0]+'")')
        for item in input[1:]:
            exec('self.my_Q |= Q("match", '+field+'="'+item+'")')

        self.s = self.s.query(self.my_Q)

        return self

    def filter_in_range(self, field, m_range=[]):
        if not field or type(m_range) != list or len(m_range) < 2:
            print("ERROR!")
            return

        ######################
        ######################
        exec("self.s = self.s.filter('range', "+field+"={'gte': m_range[0], 'lte': m_range[1]})")

        return self

    def filter_in_time_range(self, field, last_num_of_days=3):
        start_date, end_date = self.get_last_day_range(days=last_num_of_days)
        
        self.filter_in_range(field, m_range=[start_date, end_date])
        
        return self

    def get_last_day_range(self, days=3):
        filtered_day_num    = timedelta(days=days)
        start_date          = (datetime.now() - filtered_day_num).strftime('%Y-%m-%d')
        end_date            = datetime.now().strftime('%Y-%m-%d')

        return start_date, end_date

    def sort(self, input):
        self.s = self.s.sort(input)

        return self

    def source(self, field_list=[]):
        self.s = self.s.source(field_list)

        return self

    def exec(self, count=0):
        if not count:
            count   = self.s.count()

        self.result = self.s[0:count].execute()

        return self

    def json(self):
        output = []

        for item in self.result['hits']['hits']:
            output.append(item['_source'])

        return output

    def process_request(self):
        pass

    def check_permission(self):
        pass

    def get(self, field, value):
        exec("self.result = self.match_phrase(field='"+field+"',input='"+str(value)+"').source(['"+field+"']).exec(count=1).out()")
        return self.result

    def save(self, json):
        self.client.index(index=self.index, body=json)
        self.client.indices.refresh(index=self.index)

    def out(self):
        return self.result
