# 📦 P2P Logistics Terminal - Guia de Configuração (Unochapecó)

Este guia contém os passos exatos para configurar e rodar o sistema de logística descentralizada via UDP nos computadores do grupo.

## 1. Preparação do Ambiente
Abra o seu terminal (CMD ou PowerShell) e instale a biblioteca do servidor web executando o comando abaixo:
`pip install flask`

## 2. Ajuste de Identidade (Importante)
Abra o arquivo `app.py` no seu editor de código (VS Code ou Bloco de Notas). Vá até a **linha 11** e altere a variável `NOME_LOCAL` para o seu nome:
- Se for o Willian: `NOME_LOCAL = "Armazem_Willian"`
- Se for o Felipe: `NOME_LOCAL = "Armazem_Felipe"`

Salve o arquivo após a alteração.

## 3. Rodando o Sistema
No terminal, navegue até a pasta onde você salvou o projeto e execute o motor:
`python app.py`

**Atenção ao IP:** O terminal exibirá uma mensagem parecida com `* Running on http://192.168.0.XXX:8080`. 
Copie o número do seu IP e mande no grupo. Os outros nós precisam desse número exato para conseguir despachar as cargas para você.

## 4. Acessando a Interface
Mantenha a janela do terminal aberta. Vá para o seu navegador de internet e acesse o painel de controle pelo endereço:
`http://localhost:8080`

---

## 🎮 Fluxo de Apresentação

1. **Despacho Direto:** O Erik enviará uma carga original informando o IP de destino. A animação ASCII do avião aparecerá no terminal de quem enviou, e os dados da carga aparecerão no terminal de quem recebeu.
2. **Remanejo (Repasse):** Quem recebeu a carga vai copiar o texto do terminal, colar no formulário do site, preencher com o IP do terceiro integrante e clicar em **REMANEJAR CARGA (REPASSAR)**. A carga chegará ao destino final alertando que é um repasse.

## ⚠️ Regras Críticas para Funcionar
- **Mesma Rede:** Todos os notebooks devem estar conectados estritamente na mesma rede Wi-Fi da faculdade.
- **Terminal Aberto:** Não feche a janela preta do terminal durante a apresentação. Se fechar, o seu armazém fica offline e para de receber UDP.
- **Firewall:** Se o Windows exibir um alerta de segurança pedindo permissão de rede para o Python, clique em "Permitir".
