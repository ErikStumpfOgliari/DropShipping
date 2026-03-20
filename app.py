import socket
from flask import Flask, render_template
from flask_socketio import SocketIO
from motor_udp import MotorP2P 

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

def buscar_meu_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    except:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

MEU_IP = buscar_meu_ip()
PORTA_UDP = 5000

def notificar(msg):
    socketio.emit('chegou_mensagem', msg)

# Inicializa o motor
motor = MotorP2P(MEU_IP, PORTA_UDP, f"Usuario_{MEU_IP.split('.')[-1]}", notificar)
motor.iniciar_escuta_background()

@app.route('/')
def index():
    return render_template('index.html', ip=MEU_IP)

@socketio.on('comando_enviar')
def enviar(dados):
    motor.enviar_mensagem(
        dados['ip_destino'], 
        int(dados['porta_destino']), 
        dados.get('nome_destino', 'Unidade Remota'), 
        dados['texto_mensagem'],
        dados.get('encaminhado', False),
        dados.get('nota', '')
    )

if __name__ == '__main__':
    print(f"\n🚀 LOGISTICS TERMINAL ONLINE\n🔗 Dashboard: http://{MEU_IP}:8080\n")
    socketio.run(app, host="0.0.0.0", port=8080, debug=False)