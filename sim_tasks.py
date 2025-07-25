import serial
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

# === CONFIGURAÇÕES ===
PORTA = '/dev/ttyUSB0'
BAUD = 9600
INTERVALO = 100  # ms
TEMPO_JANELA = 20  # segundos mostrados no gráfico

# === INICIALIZA SERIAL ===
try:
    ser = serial.Serial(PORTA, BAUD, timeout=1)
    print(f"✅ Conectado em {PORTA}")
except Exception as e:
    print(f"❌ Erro ao abrir {PORTA}: {e}")
    exit(1)

# === FIGURA ===
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_ylim(0, 10)
ax.set_xlabel("Tempo")
ax.set_ylabel("Tarefas (nível)")
ax.grid(True)

tarefas = []  # (ativacao, duracao, altura, nome)
inicio_tempo = time.time()

cores_tarefas = {}
paleta = ['blue', 'green', 'orange', 'red', 'purple', 'brown', 'cyan', 'magenta']

def atualizar(frame):
    tempo_atual = time.time() - inicio_tempo

    try:
        linha = ser.readline().decode('utf-8').strip()
        if linha:
            print(f"Recebido: {linha}")
            if linha.startswith("Tarefa:"):
                dados = {k: v for k, v in [campo.split(":") for campo in linha.split(",")]}
                nome = dados["Tarefa"]
                ativacao = float(dados["Ativacao"])
                duracao = float(dados["Duracao"])
                altura = int(dados["Altura"])

                if nome not in cores_tarefas:
                    cores_tarefas[nome] = paleta[len(cores_tarefas) % len(paleta)]

                tarefas.append((ativacao, duracao, altura, nome))

        # === ATUALIZA PLOT ===
        ax.clear()
        ax.set_xlim(tempo_atual - TEMPO_JANELA, tempo_atual)
        ax.set_ylim(0, 10)
        ax.set_xlabel("Tempo")
        ax.set_ylabel("Tarefas (nível)")
        ax.grid(True)

        for ativ, dur, alt, nome in tarefas:
            if ativ + dur >= tempo_atual - TEMPO_JANELA:
                ax.broken_barh([(ativ, dur)], (alt - 0.4, 0.8), facecolors=cores_tarefas[nome])
                ax.text(ativ + dur / 2, alt, nome, ha='center', va='center', color='white', fontsize=8)

    except Exception as e:
        print(f"⚠️ Erro: {e}")

ani = FuncAnimation(fig, atualizar, interval=INTERVALO)
plt.tight_layout()
plt.show()
