from rest_framework.throttling import SimpleRateThrottle


class SMSSendThrottle(SimpleRateThrottle):
    rate = '1/10s'
