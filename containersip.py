#!/usr/bin/env python
# -*- coding:utf-8 -*-

from docker import Client;
import json;

c = Client(base_url='unix://var/run/docker.sock');
containers = c.containers();
for x in containers:
    inspect = c.inspect_container(x);
    print inspect['NetworkSettings']['IPAddress'], x['Names'][0];
