import time, sys
from mqhandler import RabbitMqHandler


mq = RabbitMqHandler()
mq.connect()

for i in range(100):
    mq.publish('msq-{}'.format(i))
    time.sleep(0.1)
mq.disconnect()
input('enter key...')

