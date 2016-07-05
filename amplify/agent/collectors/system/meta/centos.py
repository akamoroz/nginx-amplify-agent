# -*- coding: utf-8 -*-
import re

from amplify.agent.collectors.system.meta.container import ContainerMetaCollector
from amplify.agent.collectors.system.meta.system import SystemMetaCollector
from amplify.agent.common.util import subp

__author__ = "Mike Belov"
__copyright__ = "Copyright (C) Nginx, Inc. All rights reserved."
__credits__ = ["Mike Belov", "Andrei Belov", "Ivan Poluyanov", "Oleg Mamontov", "Andrew Alexeev", "Grant Hulegaard"]
__license__ = ""
__maintainer__ = "Mike Belov"
__email__ = "dedm@nginx.com"


class SystemCentosMetaCollector(SystemMetaCollector):
    """
    CentOS meta collector
    """

    @staticmethod
    def etc_release(meta):
        SystemMetaCollector.etc_release(meta)

        # centos6 has different  *-release format
        # for example: CentOS release 6.7 (Final)
        if meta['release']['version_id'] is None and meta['release']['version'] is None:
            etc_release_out, _ = subp.call('cat /etc/centos-release')
            for line in etc_release_out:
                r = re.match('(\w+)\s+(\w+)\s+([\d\.]+)\s+([\w\(\)]+)', line)
                if r:
                    meta['release']['name'] = r.group(1)
                    meta['release']['version_id'] = r.group(3)
                    meta['release']['version'] = '%s %s' % (r.group(3), r.group(4))


class DockerCentosMetaCollector(ContainerMetaCollector):
    """
    Docker CentOS meta collector
    """

    @staticmethod
    def etc_release(meta):
        SystemMetaCollector.etc_release(meta)

        # centos6 has different  *-release format
        # for example: CentOS release 6.7 (Final)
        if meta['release']['version_id'] is None and meta['release']['version'] is None:
            etc_release_out, _ = subp.call('cat /etc/centos-release')
            for line in etc_release_out:
                r = re.match('(\w+)\s+(\w+)\s+([\d\.]+)\s+([\w\(\)]+)', line)
                if r:
                    meta['release']['name'] = r.group(1)
                    meta['release']['version_id'] = r.group(3)
                    meta['release']['version'] = '%s %s' % (r.group(3), r.group(4))