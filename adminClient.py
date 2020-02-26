#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kafka import KafkaAdminClient

servers = ['192.168.5.110:9092']

adminClient = KafkaAdminClient(bootstrap_servers=servers)

adminClient.delete_topics(['test'])

print(adminClient.list_consumer_groups())

adminClient.close()