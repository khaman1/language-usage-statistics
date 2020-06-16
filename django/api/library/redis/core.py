import redis
import json

class Redis:
    conn = None
    
    def __init__(self, ip, port):
        self.conn = redis.Redis(ip, port, charset="utf-8", decode_responses=True)

    def save(self, queryset_values, prefix='data',ex=5):
        self.conn.set(prefix, json.dumps(queryset_values), ex=ex)

    def save2(self, queryset_values, prefix='data',ex=5):
        self.conn.set(prefix, queryset_values, ex=ex)

    def get(self, prefix='data'):
        return json.loads(self.conn.get(prefix))

    def get2(self, prefix='data'):
        output = self.conn.get(prefix)
        if output:
            output = output

        return output

    def is_expired(self, data):
        if not data:
            return True

        try:
            if len(data) == 0:
                return True
        except:
            pass

        return False

    def flush(self, key):
        self.conn.delete(key)

    def flushall(self):
        self.conn.flushall()