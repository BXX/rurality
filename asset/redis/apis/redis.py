from base.api import BaseApi
from asset.redis.controllers import redis as redis_ctl


class RedisApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'obj_id': ('Redis ID', 'required int'),
    }
    def post(self, request, params):
        data = redis_ctl.get_redis(**params)
        return data


class ListRedisApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'keyword': ('关键字', 'optional str'),
        'page_num': ('页码', 'optional int'),
        'page_size': ('页容量', 'optional int'),
    }
    def post(self, request, params):
        data = redis_ctl.get_redises(**params)
        return data
