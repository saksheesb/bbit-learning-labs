#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pika
import os
# import sys
# module_path = os.path.abspath('..')
# if(module_path) not in sys.path:
#     sys.path.append(module_path)

from producer_interface import mqProducerInterface

class mqProducer(mqProducerInterface):
        def __init__(self, routing_key: str, exchange_name: str):
            self.routing_key = routing_key
            self.exchange_name = exchange_name
            # body of constructor
            self.setupRMQConnection()
            pass
            
        def setupRMQConnection(self):
            con_params = pika.URLParameters(os.environ["AMQP_URL"])
            self.connection = pika.BlockingConnection(parameters=con_params)

            self.channel = self.connection.channel()
            self.exchange = self.channel.exchange_declare(exchange="Exchange Name")

            # con_params = pika.URLParameters("amqp://rabbitmq?connection_attempts=5&retry_delay=5")
            pass
        
        def publishOrder(self, message: str):
     
            self.channel.basic_publish(
                exchange="Exchange Name",
                routing_key="Routing Key",
                body=message
                )
              
            self.channel.close()
            self.connection.close()
            pass