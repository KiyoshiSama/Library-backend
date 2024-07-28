import json
import pika

ROUTING_KEY = "user.created.key"
EXCHANGE = "user_exchange"
THREADS = 5


class ProducerUserCreated:
    def __init__(self) -> None:

        # credentials = pika.PlainCredentials("user", "password")
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                "rabbitmq",
                5672,
                "/",
                heartbeat=600,
                blocked_connection_timeout=300,
            )
        )
        self.channel = self.connection.channel()


    def publish(self, method, body):
        print("Inside UserService: Sending to RabbitMQ: ")
        print(body)
        properties = pika.BasicProperties(method)
        self.channel.basic_publish(
            exchange=EXCHANGE,
            routing_key=ROUTING_KEY,
            body=json.dumps(body),
            properties=properties,
        )
