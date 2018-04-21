import time
import os, sys
import traceback
import socket
import hmac
import hashlib
import mensagem_pb2
import threading
from random import randint
import logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(threadName)s:%(message)s')

from random import (
    choice, randint
)
from string import (
   ascii_uppercase, ascii_letters, digits
)
from communication import (
    send_message, recv_message, SocketReadError
)

def recebe_mensagem_do_cliente(cliente, endereco):

    while True:
        try:
            mensagem = mensagem_pb2.Mensagem()
            recebe_mensagem = recv_message(cliente)
            mensagem.ParseFromString(recebe_mensagem)
            if not mensagem:
                raise error('Erro de comunicacao')
            logging.info("[received] sender name: %s, receiver name: %s, message type: %s and thread ID: %s", mensagem.sender_name, mensagem.receiver_name, mensagem_pb2.Mensagem.Msg_type.Name(mensagem.msg_type), str(mensagem.thread_id))

            mensagem.dados = os.urandom(32).encode("hex")            

            mensagem.msg_type = 1
            mensagem.thread_id = threading.current_thread().ident

            hmac_maker = hmac.new('chave-secreta-2018', '', hashlib.sha512)
            hmac_maker.update(str(mensagem.id_cliente))
            hmac_maker.update(mensagem.dados)
            mensagem.hmac = hmac_maker.hexdigest()

            logging.info("[sending] sender name: %s, receiver name: %s, message type: %s and thread ID: %s", mensagem.sender_name, mensagem.receiver_name, mensagem_pb2.Mensagem.Msg_type.Name(mensagem.msg_type), str(mensagem.thread_id))
            send_message(cliente, mensagem)
        except (SocketReadError):
            cliente.close()
            return False
        except:
            traceback.print_exc()

if __name__ == "__main__":
    
    PORTA = 5001
    
    try:
        s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s_socket.bind(("0.0.0.0", PORTA))
        s_socket.listen(10)
    
        logging.info ("Servidor iniciado na porta %s", str(PORTA))
    
        while True:
            (cliente, endereco) = s_socket.accept()
            logging.info ("Cliente (%s, %s) conectado" % endereco)
            threading.Thread(target = recebe_mensagem_do_cliente,args = (cliente,endereco)).start()

        s_socket.close()
    except (KeyboardInterrupt, SystemExit):
        logging.info("Finalizando a execucacao ...")
        pass
    except:
        traceback.print_exc()
