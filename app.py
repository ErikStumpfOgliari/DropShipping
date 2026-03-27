from flask import Flask, render_template, request
from motor_udp import MotorP2P
import time
import sys

app = Flask(__name__)

# --- CONFIGURAÇÃO ---
# No dia da apresentação, mude para o IP que aparecer no seu terminal
MEU_IP = "0.0.0.0" 
NOME_LOCAL = "Armazem_Erik" # O Willian e o Felipe mudam para o nome deles aqui

# Inicializa o motor
motor = MotorP2P(MEU_IP, 5000, NOME_LOCAL)
motor.iniciar_escuta()

def animar_aviao():
    print(f"\nDespachando carga de: {NOME_LOCAL}...")
    aviao_cima  = " <-----|----->   "
    aviao_baixo = "............... "
    
    for i in range(35):
        sys.stdout.write(f"\r{' ' * i}{aviao_cima}")
        sys.stdout.write(f"\n\r{' ' * i}{aviao_baixo}")
        sys.stdout.write("\033[F") # Comando para subir o cursor
        sys.stdout.flush()
        time.sleep(0.04)
    print("\n\n >>> CARGA SAIU DO PÁTIO! <<<\n")

@app.route('/')
def index():
    # Aqui o Flask procura o arquivo dentro da pasta 'templates'
    return render_template('index.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    ip_alvo = request.form.get('ip').strip()
    carga = request.form.get('mensagem')
    
    animar_aviao()
    motor.enviar_mensagem(ip_alvo, carga, remanejado=False)
    
    return "<h1>Sucesso!</h1><p>Carga original despachada. Veja o terminal.</p><a href='/'>Voltar</a>"

@app.route('/remanejar', methods=['POST'])
def remanejar():
    ip_alvo = request.form.get('ip').strip()
    carga_original = request.form.get('mensagem')
    
    # Texto indicando que é um remanejo
    texto_final = f"REMANEJO: {carga_original}"
    
    animar_aviao()
    motor.enviar_mensagem(ip_alvo, texto_final, remanejado=True)
    
    return "<h1>Sucesso!</h1><p>Carga REPASSADA com sucesso. Veja o terminal.</p><a href='/'>Voltar</a>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)