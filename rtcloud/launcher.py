import sys
import pika

class Launcher:
    def __init__(self, work_queue, result_queue):
        self.rmq = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = self.rmq.channel()
        self.channel.queue_declare(queue=work_queue)

        def callback(channel, method, properties, body):
            print('Received message %s' % body)
            sys.stdout.flush()

        self.channel.basic_consume(callback, queue=work_queue, no_ack=True)
        self.channel.start_consuming()