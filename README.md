📊 Visualizador de Tarefas em Tempo Real via Serial

Este projeto permite visualizar a execução de tarefas em tempo real através de uma linha do tempo dinâmica, utilizando dados enviados pela porta serial (por exemplo, via Arduino).
✨ Funcionalidades

    ✅ Visualiza tarefas na linha do tempo (gráfico tipo Gantt).

    🕒 Cada tarefa possui:

        Nome

        Tempo de ativação

        Duração

        Nível de execução (altura no gráfico)

    ⏱️ Tarefas são programadas para ocorrer no tempo exato indicado.

    📉 O sistema espera e atualiza a visualização conforme a duração de cada tarefa.

📡 Comunicação Serial

O Arduino simula a geração de tarefas e envia dados no seguinte formato:

Tarefa:T1,Ativacao:10.00,Duracao:5.00,Altura:1

Cada linha representa uma tarefa a ser visualizada no gráfico Python.
📦 Estrutura do Projeto

.
├── visualizador.py         # Script Python com Matplotlib para visualizar as tarefas
├── arduino_tarefas.ino     # Código Arduino que simula o envio das tarefas pela serial
└── README.md               # Este arquivo

🧪 Como Testar
1. 💻 Python

    Requisitos:

pip install matplotlib pyserial

Execute o script Python:

    python visualizador.py

2. 🔌 Arduino

    Carregue o código arduino_tarefas.ino em sua placa Arduino.

    O Arduino começa a enviar tarefas pela porta serial automaticamente.

    As tarefas aparecerão no gráfico em tempo real.

📷 Baseado na sua ideia

        Um código que eu possa visualizar minhas tarefas na linha do tempo.

        Programar para que ocorram no tempo certo.

        Ele vai esperar a duração da tarefa.

📈 Exemplo do Gráfico

Cada tarefa será exibida como uma barra horizontal na posição Altura durante o intervalo de tempo definido por Ativacao e Duracao.
🛠️ Melhorias Futuras (sugestões)

    Suporte a diferentes políticas de escalonamento (EDF, RM, etc)

    Detecção de colisões entre tarefas

    Exportação dos dados para CSV

    Interface gráfica com Tkinter ou Web (Dash/Flask)
