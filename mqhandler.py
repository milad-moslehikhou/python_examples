import pika


class RabbitMqHandler:
    __channel = None
    __exchange = None
    __queue = ()

    def connect(self, host='localhost', exchange='example', username='example', password='example'):
        self.__exchange = exchange
        credentials = pika.PlainCredentials(username=username, password=password)
        params = pika.ConnectionParameters(host=host, credentials=credentials)
        connection = pika.BlockingConnection(parameters=params)
        self.__channel = connection.channel()
        self.__channel.exchange_declare(exchange=self.__exchange, exchange_type='fanout')
        declare = self.__channel.queue_declare(exclusive=True)
        self.__queue = declare.method.queue
        self.__channel.queue_bind(exchange=self.__exchange, queue=self.__queue, routing_key='')
        print('connected to rabbitmq.')

    def publish(self, message):
        self.__channel.basic_publish(exchange=self.__exchange, routing_key='', body=message)
        print('The message was put.\nmsg={}'.format(message))

    def consume(self, callback):
        self.__channel.basic_consume(callback, queue=self.__queue, no_ack=True)
        print('Consuming start.')
        self.__channel.start_consuming()
