# Correção da Prova - Introdução à Aprendizagem Automática

---

## **Parte 1**

### Questão 1 - 1,5 ponto

**A)** Representação das curvas de erro de predição em função do grau:

- **Erro na base de aprendizado**: Diminui rapidamente à medida que o grau aumenta e o modelo se ajusta melhor às amostras, podendo atingir erro próximo de zero para graus altos (sobreajuste).
- **Erro na base de teste**: Forma típica em U. Inicialmente diminui conforme o grau aumenta, atinge um ponto ótimo e volta a subir devido ao sobreajuste para graus muito elevados.

**B)** Escolha de classificador:

- **(a) SVM linear**: **Não recomendado**. Como a regressão logística já sofre de subajuste, este modelo similarmente não capturará relações não lineares.
- **(b) SVM com núcleo RBF**: **Recomendado**. Captura relações não lineares, melhorando o desempenho.
- **(c) Perceptron de Rosenblatt**: **Não recomendado**. Modelo linear, também sofre com subajuste.
- **(d) Perceptron multicamada com \( f(x) = \alpha x \)**: **Não recomendado**. Função de ativação linear não resolve relações não lineares.

**C)** Avaliação do XGBoost:

- Para um desequilíbrio de classes significativo (80%, 15%, 5%), a métrica de acurácia média de 70% é insatisfatória, já que pode refletir viés para a classe majoritária. Recomenda-se analisar métricas como F1-score ou curvas ROC.

---

### Questão 2 - 1,5 ponto

**Score leave-one-out:**

- **\( K = 1 \)**: O classificador se ajusta exatamente às amostras, mas pode apresentar instabilidade.
- **\( K = 3 \)**: Oferece maior robustez, generalizando melhor.
- **Escolha**: \( K = 3 \), pois equilibra variância e viés.

---

### Questão 3 - 2 pontos

**Classificador Naïf Bayes uniforme:**

- A classe predita depende da posição de \( x \) em relação aos retângulos \( R_1 \) e \( R_2 \).
- **Regras de decisão**:
  - Se \( x \) está apenas em \( R_1 \), predição: \( C_1 \).
  - Se \( x \) está apenas em \( R_2 \), predição: \( C_2 \).
  - Para interseções, comparar probabilidades a priori.
- **Simplificação com a priori iguais**: A predição depende exclusivamente da presença em \( R_1 \) ou \( R_2 \).

---

### Questão 4 - 1 ponto

**K-means com \( K = 2 \):**

- **Passos**:
  - Inicializar os centros em (2,3) e (4,2).
  - Atualizar iterativamente as atribuições e recalcular os centros até convergência.
- **Resultado final**:
  - Partição gráfica mostrando dois grupos separados pelos centros.

---

### Questão 5 - 2,5 pontos

**A)** Regressão logística padrão:

- Não separa as classes, pois elas não são linearmente separáveis.

**B)** Noyau definido:

- Transformação \( \phi(x) = \frac{x}{\|x\|} \).
- Representação gráfica com imagens \( \phi(x) \) que mostram separação linear no espaço transformado.

**C)** Separabilidade linear:

- Verificação visual confirma separação linear no espaço transformado.
- Vetores de suporte: Pontos mais próximos da margem.

**D)** Fronteira no espaço original:

- Fronteira curva correspondente à separação linear no espaço transformado.

---

### Questão 6 - 1,5 ponto

**A)** Probabilidade \( p(C_1|x) \):

- Calculada com base nos pesos \( w_i \), no parâmetro \( c \), e nas entradas \( (x_1, x_2) \).

**B)** Fronteira de classificação:

- Fronteira linear no espaço \( R^2 \).

**C)** Rede equivalente:

- Rede sem camada oculta, com saída diretamente conectada aos pesos e à função sigmoide.

---
