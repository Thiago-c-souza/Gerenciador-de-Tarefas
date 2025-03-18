# 📝 Gerenciador de Tarefas

Um **Gerenciador de Tarefas** simples e eficiente feito em **Python**, utilizando **JSON** para armazenar as tarefas. O programa funciona no terminal e permite adicionar, listar, concluir e excluir tarefas.

## 🚀 Funcionalidades
✅ Adicionar tarefas com ID único  
✅ Listar tarefas pendentes e concluídas (ordenadas automaticamente)  
✅ Marcar tarefas como concluídas  
✅ Editar tarefas  
✅ Excluir tarefas  
✅ Salvar e carregar tarefas automaticamente (JSON)  
✅ Interface de menu interativa no terminal  
✅ Registro de data de criação e conclusão das tarefas  

## 📌 Tecnologias Utilizadas
- **Python 3**
- **Manipulação de arquivos JSON** para armazenamento
- **Estruturas de repetição e condicionais** para controle de fluxo
- **Uso da biblioteca `datetime`** para registrar datas das tarefas

---

## 📂 Estrutura do Projeto
```
📦 Gerenciador-de-Tarefas
 ├── 📜 main.py          # Arquivo principal do programa
 ├── 📜 tarefas.json     # Armazena as tarefas (criado automaticamente)
 ├── 📜 README.md        # Documentação do projeto
```

---

## 🔧 **Pré-requisitos**
Antes de começar, verifique se você tem os seguintes requisitos instalados:

- **Python 3.x** instalado na máquina

Para verificar a instalação do Python:
```sh
python --version  # Ou python3 --version
```

---

## 💻 **Como Executar o Projeto**

1️⃣ **Clone o repositório:**
```sh
git clone https://github.com/Thiago-c-souza/Gerenciador-de-Tarefas.git
```

2️⃣ **Acesse a pasta do projeto:**
```sh
cd gerenciador-de-tarefas
```

3️⃣ **Execute o programa:**
```sh
python main.py
```

📌 **Obs:** O arquivo `tarefas.json` será criado automaticamente ao executar o programa pela primeira vez.

---

## 🛠 **Como Usar**
Quando o programa for executado, o seguinte menu aparecerá:
```
📌 Gerenciador de Tarefas
1 - Adicionar Tarefa
2 - Listar Tarefas
3 - Marcar Tarefa como Concluída
4 - Editar Tarefa
5 - Excluir Tarefa
6 - Sair
```

🔹 **Opções disponíveis:**
- **1:** Digite a descrição da nova tarefa para adicioná-la.
- **2:** Lista todas as tarefas, mostrando seu status (pendente ou concluída), ordenadas automaticamente.
- **3:** Digite o ID da tarefa que deseja marcar como concluída.
- **4:** Digite o ID da tarefa que deseja editar e insira a nova descrição.
- **5:** Digite o ID da tarefa que deseja excluir.
- **6:** Salva as tarefas e encerra o programa.

---

## 🏗 **Trecho do Código (Exemplo de Ordenação de Tarefas)**
```python
def ordenar_tarefas(tarefas):
    pendentes = [t for t in tarefas if not t["concluido"]]
    concluidas = [t for t in tarefas if t["concluido"]]
    return pendentes + concluidas  # Junta as listas ordenadas
```

---

## 📌 **Possíveis Melhorias Futuras**
🔹 Implementação de uma interface gráfica com Tkinter ou PyQt  
🔹 Uso de Banco de Dados (SQLite) para armazenar tarefas  
🔹 Implementação de testes unitários para validar funcionalidades  
🔹 Envio de notificações sobre tarefas pendentes  
🔹 Exportação de tarefas para CSV  

---

## 🤝 **Contribuição**
Se quiser contribuir para o projeto:
1. **Faça um fork** do repositório
2. **Crie uma branch** com a nova funcionalidade: `git checkout -b minha-feature`
3. **Faça um commit das alterações**: `git commit -m 'Adicionando nova feature'`
4. **Envie para o GitHub**: `git push origin minha-feature`
5. **Abra um Pull Request`

---

📌 **Criado por Thiago Caixeta de Souza** 🚀

