from django.http import JsonResponse
from api.library.redis.core import *
from api.core.constants import REDIS_HOSTNAME,REDIS_PORT
class APIBase:
    prefix          = ''
    redis           = ''
    request         = ''
    enable_redis    = 0
    redis_expiration= 60
    context         = {}
    DEBUG           = 0
    
    def __init__(self,request=0,enable_redis=0,suffix_redis_key=''):
        if enable_redis:
            self.prefix         = type(self).__name__ + ',' + str(request) + suffix_redis_key
            self.enable_redis   = enable_redis
            self.init_redis()

        if request:         
            self.request        = request
            self.process_request()


    def init_redis(self):
        self.redis              = Redis(REDIS_HOSTNAME, REDIS_PORT)

    def process_request(self):
        pass

    def check_cache(self):
        if self.enable_redis:
            try:
              context       = self.redis.get(self.prefix)
            except:
              context       = ''

            if not self.redis.is_expired(context):
              return JsonResponse(context, safe=False)
        
        return False

    def exec(self):
        self.check_permission()

        result = self.check_cache()
        if result:
            if self.DEBUG:      print("CACHED!")
            return result

        self.step1()
        self.step2()
        self.step3()
        self.save_redis()
        return self.output()

    def check_permission(self):
        pass

    def step1(self):
        pass

    def step2(self):
        pass

    def step3(self):
        pass

    def save_redis(self):
        if self.enable_redis:
            if self.DEBUG:       
                print("SAVE!")
                print("prefix: " + self.prefix)
            self.redis.save(self.context, prefix=self.prefix, ex=self.redis_expiration)

    def output(self):
        return JsonResponse(self.context, safe=False)