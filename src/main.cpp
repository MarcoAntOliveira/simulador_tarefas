#include <Arduino.h>

// === CONFIGURAÇÕES ===
unsigned long tempoAnterior = 0;
const unsigned long intervaloEnvio = 1000;  // Envia uma tarefa a cada 1s
int contadorTarefa = 0;

void setup() {
  Serial.begin(9600);
  while (!Serial);  // Espera conexão, útil para placas como Leonardo
}

void loop() {
  unsigned long agora = millis();

  if (agora - tempoAnterior >= intervaloEnvio) {
    tempoAnterior = agora;

    // Simula uma tarefa com ativação baseada no tempo atual
    float ativacao = agora / 1000.0;  // em segundos
    float duracao = random(1, 5);     // entre 1 e 4 segundos
    int altura = (contadorTarefa % 8) + 1;  // posição Y (1 a 8)
    String nome = "T" + String(contadorTarefa);

    // Envia no formato esperado:
    String linha = "Tarefa:" + nome + ",Ativacao:" + String(ativacao, 2) +
                   ",Duracao:" + String(duracao, 2) +
                   ",Altura:" + String(altura);

    Serial.println(linha);
    contadorTarefa++;
  }
}
