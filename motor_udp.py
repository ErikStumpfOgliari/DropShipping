import socket
import json
import threading
from datetime import datetime

class MotorP2P:
    def __init__(self, meu_ip, minha_porta, meu_nome):
        self.meu_ip = meu_ip
        self.minha_porta = minha_porta
        self.meu_nome = meu_nome
        
        # Cria o Socket UDP
        self.socket_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # Bind em "" permite que o Windows receba de qualquer IP na rede
        self.socket_udp.bind(("", self.minha_porta))

    def enviar_mensagem(self, ip_dest, conteudo, remanejado=False):
        # Monta o pacote de dados (JSON)
        pacote = {
            "timestamp": datetime.now().strftime("%H:%M:%S"),
            "remetente": self.meu_nome,
            "origem": f"{self.meu_ip}",
            "conteudo": conteudo,
            "remanejado": remanejado
        }
        bytes_pacote = json.dumps(pacote).encode('utf-8')
        # Envia para a porta 5000 do destino
        self.socket_udp.sendto(bytes_pacote, (ip_dest, 5000))

    def escutar(self):
        while True:
            try:
                dados, endereco = self.socket_udp.recvfrom(4096)
                msg = json.loads(dados.decode('utf-8'))
                
                print(f"\n[--- CARGA RECEBIDA ---]")
                if msg.get('remanejado'):
                    print(">>> STATUS: CARGA REPASSADA (REMANEJO) <<<")
                
                print(f"🕒 Hora: {msg['timestamp']}")
                print(f"👤 De: {msg['remetente']} ({msg['origem']})")
                print(f"📦 Produto: {msg['conteudo']}")
                print(f"[----------------------]\n")
            except:
                pass

    def iniciar_escuta(self):
        # Inicia a thread de recebimento
        t = threading.Thread(target=self.escutar, daemon=True)
        t.start()