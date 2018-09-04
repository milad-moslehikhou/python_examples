import time
from mqhandler import RabbitMqHandler


mq = RabbitMqHandler()
mq.connect()

for i in range(100):
    mq.publish('msq-{}'.format(i))
    time.sleep(1)

