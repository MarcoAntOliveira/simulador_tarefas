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
ax.set_xlabel("Tempo (s)")
ax.set_ylabel("Tarefa")
ax.grid(True)

tarefas = []  # (ativacao, duracao, nome)
inicio_tempo = time.time()

cores_tarefas = {}
ordem_tarefas = []
paleta = ['blue', 'green', 'orange', 'red', 'purple', 'brown', 'cyan', 'magenta']

def atualizar(frame):
    tempo_atual = time.time() - inicio_tempo

    try:
        linha = ser.readline().decode('utf-8').strip()
        if linha:
            print(f"Recebido: {linha}")
            if linha.startswith("Tarefa:"):
                campos = linha.split(",")
                dados = {}
                for campo in campos:
                    chave, valor = campo.split(":")
                    dados[chave.strip()] = valor.strip()

                nome = dados["Tarefa"]
                ativacao = float(dados["Ativacao"])
                duracao = float(dados["Duracao"])

                if nome not in cores_tarefas:
                    cores_tarefas[nome] = paleta[len(cores_tarefas) % len(paleta)]
                    if nome not in ordem_tarefas:
                        ordem_tarefas.append(nome)

                tarefas.append((ativacao, duracao, nome))

        # === ATUALIZA PLOT ===
        ax.clear()
        ax.set_xlim(max(0, tempo_atual - TEMPO_JANELA), tempo_atual)
        ax.set_yticks(range(len(ordem_tarefas)))
        ax.set_yticklabels(ordem_tarefas)
        ax.set_ylim(-1, len(ordem_tarefas))
        ax.set_xlabel("Tempo (s)")
        ax.set_ylabel("Tarefa")
        ax.grid(True)

        for ativ, dur, nome in tarefas:
            if ativ + dur >= tempo_atual - TEMPO_JANELA:
                y_idx = ordem_tarefas.index(nome)
                ax.broken_barh([(ativ, dur)], (y_idx - 0.4, 0.8), facecolors=cores_tarefas[nome])
                ax.text(ativ + dur / 2, y_idx, nome, ha='center', va='center', color='white', fontsize=8)

    except Exception as e:
        print(f"⚠️ Erro: {e}")

ani = FuncAnimation(fig, atualizar, interval=INTERVALO)
plt.tight_layout()
plt.show()
