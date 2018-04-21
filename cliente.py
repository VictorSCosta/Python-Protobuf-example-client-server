#!/usr/bin/env python

import socket
import os, sys, getopt
import traceback
import hmac
import hashlib
import logging
import mensagem_pb2
import names
from communication import (
    send_message, recv_message
)
from random import ( 
    choice, randint
)
from string import (
    ascii_uppercase, ascii_letters, digits
)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(threadName)s - %(levelname)s - %(message)s')

if __name__ == "__main__":
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("127.0.0.1", 5001))

    mensagem = mensagem_pb2.Mensagem()
    for i in range(10):
        try: 
            mensagem.id_cliente = int(''.join([choice(digits) for n in xrange(8)]))
            mensagem.id_mensagem = i
            mensagem.dados = ''.join([choice(ascii_letters + digits) for n in xrange(32)])

            name = names.get_first_name()
            email = name + ('@gmail.com')
            mensagem.sender_name = name
            mensagem.sender_nickname = name + str(randint(0,9))
            mensagem.sender_email = email

            name = names.get_first_name()
            email = name + '@gmail.com'
            mensagem.receiver_name = name
            mensagem.receiver_nickname = name + str(randint(0,9))
            mensagem.receiver_email = email
            
            mensagem.thread_id = 0
            mensagem.msg_type = 0
            mensagem.subject = ''.join([choice(ascii_letters + digits) for n in xrange(10)])

            hmac_maker = hmac.new('chave-secreta-2018', '', hashlib.sha512)
            hmac_maker.update(str(mensagem.id_cliente))
            hmac_maker.update(mensagem.dados)
            mensagem.hmac = hmac_maker.hexdigest()

            logging.info("[sending] sender name: %s, receiver name: %s, message type: %s and thread ID: %s", mensagem.sender_name, mensagem.receiver_name, mensagem_pb2.Mensagem.Msg_type.Name(mensagem.msg_type), str(mensagem.thread_id))
            send_message(sock, mensagem)
            recebe_mensagem = recv_message(sock)
            if recebe_mensagem:
                mensagem.ParseFromString(recebe_mensagem)
                logging.info("[received] sender name: %s, receiver name: %s, message type: %s and thread ID: %s", mensagem.sender_name, mensagem.receiver_name, mensagem_pb2.Mensagem.Msg_type.Name(mensagem.msg_type), str(mensagem.thread_id))
            else:
                logging.info("ERRO ao receber mensagens")
        except:
            traceback.print_exc()
        
    sock.close()

