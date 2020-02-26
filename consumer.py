#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kafka import KafkaConsumer

servers = ['192.168.5.110:9092']

consumer = KafkaConsumer('test', bootstrap_servers=servers)

print(consumer.partitions_for_topic('test'))
print(consumer.topics())
print(consumer.subscription())
print(consumer.assignment())
print(consumer.beginning_offsets(consumer.assignment()))

for msg in consumer:
    print(msg.value)

consumer.close()