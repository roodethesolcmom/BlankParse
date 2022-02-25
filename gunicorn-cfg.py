# -*- encoding: utf-8 -*-

bind = '0.0.0.0:80','[::]:8443','[::]:3000','[::]:8080'
workers = 5
accesslog = '-'
loglevel = 'production'
capture_output = True
enable_stdio_inheritance = True
forwarded_allow_ips = '*'
proxy_protocol = True
proxy_allow_ips = '*'