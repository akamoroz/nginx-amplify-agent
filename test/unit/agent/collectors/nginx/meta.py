# -*- coding: utf-8 -*-
from hamcrest import *

from amplify.agent.objects.nginx.binary import _parse_arguments
from test.base import NginxCollectorTestCase

__author__ = "Mike Belov"
__copyright__ = "Copyright (C) Nginx, Inc. All rights reserved."
__credits__ = ["Mike Belov", "Andrei Belov", "Ivan Poluyanov", "Oleg Mamontov", "Andrew Alexeev"]
__license__ = ""
__maintainer__ = "Mike Belov"
__email__ = "dedm@nginx.com"


class MetaParsersTestCase(NginxCollectorTestCase):

    def test_parse_arguments_1_4_6(self):
        raw_arguments = """ --with-cc-opt='-g -O2 -fstack-protector --param=ssp-buffer-size=4 -Wformat -Werror=format-security -D_FORTIFY_SOURCE=2' --with-ld-opt='-Wl,-Bsymbolic-functions -Wl,-z,relro' --prefix=/usr/share/nginx --conf-path=/etc/nginx/nginx.conf --http-log-path=/var/log/nginx/access.log --error-log-path=/var/log/nginx/error.log --lock-path=/var/lock/nginx.lock --pid-path=/run/nginx.pid --http-client-body-temp-path=/var/lib/nginx/body --http-fastcgi-temp-path=/var/lib/nginx/fastcgi --http-proxy-temp-path=/var/lib/nginx/proxy --http-scgi-temp-path=/var/lib/nginx/scgi --http-uwsgi-temp-path=/var/lib/nginx/uwsgi --with-debug --with-pcre-jit --with-ipv6 --with-http_ssl_module --with-http_stub_status_module --with-http_realip_module --with-http_addition_module --with-http_dav_module --with-http_geoip_module --with-http_gzip_static_module --with-http_image_filter_module --with-http_spdy_module --with-hroot"""
        arguments = _parse_arguments(raw_arguments)

        for expected_key in ['with-http_realip_module', 'with-http_spdy_module', 'with-ipv6', 'prefix', 'pid-path',
                             'with-http_ssl_module', 'http-log-path', 'with-http_gzip_static_module',
                             'with-http_image_filter_module', 'with-http_addition_module', 'with-http_geoip_module',
                             'with-http_dav_module', 'http-fastcgi-temp-path', 'http-proxy-temp-path', 'with-ld-opt',
                             'conf-path', 'with-http_stub_status_module', 'http-client-body-temp-path', 'with-debug',
                             'error-log-path', 'with-hroot', 'with-cc-opt', 'http-uwsgi-temp-path',
                             'http-scgi-temp-path', 'with-pcre-jit', 'lock-path']:
            assert_that(arguments.keys(), has_item(expected_key))

        for key in arguments.iterkeys():
            assert_that(key, is_not(contains_string('--')))

    def test_parse_arguments_nginx_1_6_2(self):
        raw_arguments = """configure arguments: --with-cc-opt='-g -O2 -fPIE -fstack-protector-strong -Wformat -Werror=format-security -D_FORTIFY_SOURCE=2' --with-ld-opt='-Wl,-Bsymbolic-functions -fPIE -pie -Wl,-z,relro -Wl,-z,now' --prefix=/usr/share/nginx --conf-path=/etc/nginx/nginx.conf --http-log-path=/var/log/nginx/access.log --error-log-path=/var/log/nginx/error.log --lock-path=/var/lock/nginx.lock --pid-path=/run/nginx.pid --http-client-body-temp-path=/var/lib/nginx/body --http-fastcgi-temp-path=/var/lib/nginx/fastcgi --http-proxy-temp-path=/var/lib/nginx/proxy --http-scgi-temp-path=/var/lib/nginx/scgi --http-uwsgi-temp-path=/var/lib/nginx/uwsgi --with-debug --with-pcre-jit --with-ipv6 --with-http_ssl_module --with-http_stub_status_module --with-http_realip_module --with-http_auth_request_module --with-http_addition_module --with-http_dav_module --with-http_geoip_module --with-http_gzip_static_module --with-http_image_filter_module --with-http_spdy_module --with-http_sub_module --with-http_xslt_module --with-mail --with-mail_ssl_module"""
        arguments = _parse_arguments(raw_arguments)

        for expected_key in ['with-http_realip_module', 'with-http_sub_module', 'with-http_auth_request_module',
                             'with-http_spdy_module', 'with-ipv6', 'prefix', 'pid-path', 'with-http_ssl_module',
                             'http-log-path', 'with-http_gzip_static_module', 'with-http_image_filter_module',
                             'with-http_addition_module', 'with-http_geoip_module', 'with-http_dav_module',
                             'configure arguments:', 'http-proxy-temp-path', 'with-ld-opt', 'conf-path',
                             'with-http_stub_status_module', 'http-client-body-temp-path', 'with-debug',
                             'error-log-path', 'http-fastcgi-temp-path', 'with-cc-opt', 'with-mail_ssl_module',
                             'http-uwsgi-temp-path', 'with-http_xslt_module', 'with-mail', 'http-scgi-temp-path',
                             'with-pcre-jit', 'lock-path']:
            assert_that(arguments.keys(), has_item(expected_key))

    def test_parse_arguments_add_modeles(self):
        raw_arguments = """configure arguments: --build=nginx-plus-extras-r7-p1 --prefix=/etc/nginx --sbin-path=/usr/sbin/nginx --conf-path=/etc/nginx/nginx.conf --error-log-path=/var/log/nginx/error.log --http-log-path=/var/log/nginx/access.log --pid-path=/var/run/nginx.pid --lock-path=/var/run/nginx.lock --http-client-body-temp-path=/var/cache/nginx/client_temp --http-proxy-temp-path=/var/cache/nginx/proxy_temp --http-fastcgi-temp-path=/var/cache/nginx/fastcgi_temp --http-uwsgi-temp-path=/var/cache/nginx/uwsgi_temp --http-scgi-temp-path=/var/cache/nginx/scgi_temp --user=nginx --group=nginx --with-http_ssl_module --with-http_realip_module --with-http_addition_module --with-http_sub_module --with-http_dav_module --with-http_flv_module --with-http_mp4_module --with-http_f4f_module --with-http_hls_module --with-http_gunzip_module --with-http_gzip_static_module --with-http_random_index_module --with-http_secure_link_module --with-http_session_log_module --with-http_stub_status_module --with-http_auth_request_module --with-mail --with-mail_ssl_module --with-threads --with-file-aio --with-http_spdy_module --with-ipv6 --with-stream --with-stream_ssl_module --with-http_perl_module --with-http_image_filter_module --with-http_geoip_module --with-http_xslt_module --add-module=extra/ngx_devel_kit-0.2.19 --add-module=extra/set-misc-nginx-module-0.29 --add-module=extra/lua-nginx-module-0.9.16 --add-module=extra/headers-more-nginx-module-0.26 --add-module=extra/passenger-5.0.15/ext/nginx --add-module=extra/nginx-rtmp-module-1.1.7 --with-cc-opt='-g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wp,-D_FORTIFY_SOURCE=2' --with-ld-opt='-Wl,-Bsymbolic-functions -Wl,-z,relro -Wl,--as-needed'"""
        arguments = _parse_arguments(raw_arguments)

        assert_that(arguments, has_key('add-module'))
        assert_that(arguments['add-module'], is_(list))
        assert_that(arguments['add-module'], has_length(greater_than(1)))