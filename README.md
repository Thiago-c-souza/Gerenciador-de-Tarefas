# 📝 Gerenciador de Tarefas

Um **Gerenciador de Tarefas** simples e eficiente feito em **Python**, utilizando **JSON** para armazenar as tarefas. O programa funciona no terminal e permite adicionar, listar, concluir e excluir tarefas.

## 🚀 Funcionalidades
✅ Adicionar tarefas com ID único
✅ Listar tarefas pendentes e concluídas
✅ Marcar tarefas como concluídas
✅ Excluir tarefas
✅ Salvar e carregar tarefas automaticamente (JSON)
✅ Interface de menu interativa no terminal

## 📌 Tecnologias Utilizadas
- **Python 3**
- **Manipulação de arquivos JSON** para armazenamento
- **Estruturas de repetição e condicionais** para controle de fluxo

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
4 - Excluir Tarefa
5 - Sair
```

🔹 **Opções disponíveis:**
- **1:** Digite a descrição da nova tarefa para adicioná-la.
- **2:** Lista todas as tarefas, mostrando seu status (pendente ou concluída).
- **3:** Digite o ID da tarefa que deseja marcar como concluída.
- **4:** Digite o ID da tarefa que deseja excluir.
- **5:** Salva as tarefas e encerra o programa.

---

## 🏗 **Trecho do Código (Exemplo de Adicionar Tarefa)**
```python
def adicionar_tarefa(tarefas):
    descricao = input("✏ Digite a descrição da tarefa: ")
    nova_tarefa = {"id": len(tarefas) + 1, "descricao": descricao, "concluido": False}
    tarefas.append(nova_tarefa)
    salvar_tarefas(tarefas)
    print("✅ Tarefa adicionada com sucesso!")
```

---

## 📌 **Possíveis Melhorias Futuras**
🔹 Ordenação automática (pendentes primeiro, concluídas depois)  
🔹 Opção para editar uma tarefa  
🔹 Interface gráfica com Tkinter ou PyQt  
🔹 Uso de Banco de Dados (SQLite) para armazenar tarefas  
🔹 Implementação de testes unitários  

---

## 🤝 **Contribuição**
Se quiser contribuir para o projeto:
1. **Faça um fork** do repositório
2. **Crie uma branch** com a nova funcionalidade: `git checkout -b minha-feature`
3. **Faça um commit das alterações**: `git commit -m 'Adicionando nova feature'`
4. **Envie para o GitHub**: `git push origin minha-feature`
5. **Abra um Pull Request**

---

📌 **Criado por Thiago Caixeta de Souza** 🚀

