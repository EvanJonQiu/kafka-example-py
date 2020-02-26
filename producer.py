#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kafka import KafkaProducer

servers = ['192.168.5.110:9092']

producer = KafkaProducer(bootstrap_servers=servers)

for _ in range(100):
  producer.send('test', b'some-message-bytes')

producer.close()