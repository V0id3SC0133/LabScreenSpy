
# LabScreenSpy - Versão 1.0.0

Projeto de monitoramento de tela via rede, utilizando comunicação TCP entre um cliente (Windows) e um servidor (Kali Linux). O cliente captura screenshots periodicamente e envia para o servidor, que as exibe em tempo real.

## 👨‍💻 Autor
- **Ernani S. C.**
- **Nickname:** v0id3SC0133

## 🎯 Objetivo
Criar uma PoC (Proof of Concept) de um screenshot spy entre máquinas conectadas em rede, simulando uma ferramenta de exfiltração de tela para fins educacionais ou testes de segurança.

## 🖥️ Arquitetura
- **Cliente:** Windows
- **Servidor:** Kali Linux

## 📦 Requisitos
### Cliente (Windows)
```bash
pip install pillow
```
### Servidor (Kali Linux)
```bash
sudo apt update
sudo apt install python3-opencv python3-pip -y
pip3 install pillow
```

## ⚙️ Execução
### Servidor (Kali)
```bash
python3 LabScreenSpy_Server.py
```
### Cliente (Windows)
1. Edite o IP do servidor no script.
```python
ip = '192.168.1.1'
```
2. Execute:
```bash
python LabScreenSpy_Client.py
```

## 📌 Funcionamento
- Captura de tela e compressão 4x.
- Envio somente se houver alteração visual.
- Exibição no servidor com OpenCV.

## ⚠️ Aviso Legal
Este projeto é apenas para fins educacionais. O uso indevido pode violar leis. O autor não se responsabiliza.

## Próximos Passos
- Suporte a múltiplos monitores
- Criptografia de dados
- Compressão mais rápida
