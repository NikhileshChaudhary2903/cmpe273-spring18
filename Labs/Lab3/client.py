import sys
import threading
import zmq


class Client(object):

    def __init__(self, username, server_host, server_port, chat_pipe):
        self.username = username
        self.server_host = server_host
        self.server_port = server_port
        self.context = zmq.Context()
        self.chat_sock = None
        self.chat_pipe = chat_pipe
        self.poller = zmq.Poller()

    def connect_to_server(self):
        self.chat_sock = self.context.socket(zmq.REQ)
        connect_string = 'tcp://{}:{}'.format(
            self.server_host, self.server_port)
        self.chat_sock.connect(connect_string)

    def reconnect_to_server(self):
        self.poller.unregister(self.chat_sock)
        self.chat_sock.setsockopt(zmq.LINGER, 0)
        self.chat_sock.close()
        self.connect_to_server()
        self.register_with_poller()

    def register_with_poller(self):
        self.poller.register(self.chat_sock, zmq.POLLIN)

    def prompt_for_message(self):
        return self.chat_pipe.recv_string()

    def send_message(self, message):
        data = {
            'username': self.username,
            'message': message,
        }
        self.chat_sock.send_json(data)

    def get_reply(self):
        self.chat_sock.recv()

    def has_message(self):
        events = dict(self.poller.poll(3000))
        return events.get(self.chat_sock) == zmq.POLLIN

    def start_main_loop(self):
        self.connect_to_server()
        self.register_with_poller()

        while True:
            message = self.prompt_for_message()
            self.send_message(message)
            if self.has_message():
                self.get_reply()
            else:
                self.reconnect_to_server()

    def run(self):
        thread = threading.Thread(target=self.start_main_loop)
        # make sure this background thread is daemonized
        # so that when user sends interrupt, whole program stops
        thread.daemon = True
        thread.start()


def parse_args():
    parser = argparse.ArgumentParser(description='Run a chat client')

    # maybe make selection of username interactive
    parser.add_argument('username',
                        type=str,
                        help='your preferred username')
    parser.add_argument('--config-file',
                        type=str,
                        help='path to an alternate config file, defaults to zmq-chat.cfg')

    return parser.parse_args()


if '__main__' == __name__:
    try:
        args = parse_args()
        config_file = args.config_file if args.config_file is not None else 'zmq-chat.cfg'
        config = configparser.ConfigParser()
        config.read(config_file)
        config = config['default']

        client = Client(args.username,
                            config['server_host'], config['chat_port'])
        client.start_main_loop()

    except KeyboardInterrupt:
        pass
