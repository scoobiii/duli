### Projeto DULI 

Projeto DULI, integrando as classes corretas do modelo e melhorando a interface. O projeto continua usando **Streamlit** para a interface e **Plotly** para a visualização em **Treemap**.

---

## **Atualizações Implementadas**

1. **Correção de Labels**  
   Agora as classes exibidas no treemap refletem todas as categorias do modelo (extraídas do metadata fornecido).

2. **Interface Melhorada**  
   - Adição de texto explicativo para facilitar o uso.
   - Mensagens de erro claras para entradas inválidas.

3. **Ajustes no Treemap**  
   - As classes são exibidas com seus nomes completos.
   - O gráfico usa um esquema de cores mais intuitivo (**Viridis**) para destacar probabilidades.

---

### **Código Atualizado (`app.py`)**


---

### **Dependências Atualizadas**

Adicione as seguintes dependências ao arquivo `requirements.txt`:

```
    streamlit==1.40.2
    tensorflow==2.11.0
    Pillow==10.0.0
    requests==2.31.0
    plotly==5.17.0
    numpy==1.23.0
```

---

## **Como Usar**

1. **Instalar as Dependências**
   Certifique-se de estar em um ambiente virtual e instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

2. **Rodar o Aplicativo**
   Execute o aplicativo com Streamlit:

   ```bash
   streamlit run app.py
   ```

3. **Abrir no Navegador**
   - Acesse **http://localhost:8501** para usar a aplicação.

4. **Testar com Imagens**
   - Envie uma imagem de upload, forneça uma URL ou use a opção de webcam para testar.

---

## **Novidades**

1. **Integração Completa com Labels do Modelo**
   - O gráfico exibe todas as classes previstas no metadata do modelo.

2. **Cores Mais Intuitivas**
   - Usamos o esquema de cores **Viridis** para uma melhor visualização.

3. **Interface Simples e Educativa**
   - Mensagens explicativas guiam o usuário pelo processo.

---

### **Para Crianças**
Imagine que o **Treemap** é como uma árvore cheia de caixas. Cada caixa tem o nome de algo que o modelo viu, como "COVID-19" ou "Pneumonia". Quanto maior a caixa, mais provável que o modelo ache que a imagem é daquela coisa. 😊

Essa atualização melhora a interação com o modelo e torna mais fácil entender os resultados de forma visual e divertida! 🚀
