import socket
import json
import threading

class MotorP2P:
    def __init__(self, meu_ip, minha_porta, meu_nome, callback_recebimento):
        self.meu_ip = meu_ip
        self.minha_porta = minha_porta
        self.meu_nome = meu_nome
        self.callback_recebimento = callback_recebimento
        
        self.socket_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # O bind em "" permite receber pacotes de qualquer origem (inclusive local)
        self.socket_udp.bind(("", self.minha_porta))

    def enviar_mensagem(self, ip_dest, porta_dest, nome_dest, conteudo, encaminhado=False, nota=""):
        pacote = {
            "remetente_nome": self.meu_nome,
            "remetente_ip_porta": f"{self.meu_ip}:{self.minha_porta}",
            "conteudo": conteudo,
            "status_encaminhamento": encaminhado,
            "nota_encaminhamento": nota
        }
        bytes_pacote = json.dumps(pacote).encode('utf-8')
        self.socket_udp.sendto(bytes_pacote, (ip_dest, porta_dest))

    def escutar(self):
        while True:
            try:
                dados, endereco = self.socket_udp.recvfrom(4096)
                pacote_recebido = json.loads(dados.decode('utf-8'))
                self.callback_recebimento(pacote_recebido)
            except Exception as e:
                print(f"Erro na escuta UDP: {e}")

    def iniciar_escuta_background(self):
        thread = threading.Thread(target=self.escutar, daemon=True)
        thread.start()