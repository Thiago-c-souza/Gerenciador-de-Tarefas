import json
import csv
from datetime import datetime

def menu():
    print("\n📌 Gerenciador de Tarefas")
    print("1 - Adicionar Tarefa")
    print("2 - Listar Tarefas")
    print("3 - Marcar Tarefa como Concluída")
    print("4 - Editar Tarefa")
    print("5 - Excluir Tarefa")
    print("6 - Exportar Tarefas para CSV")
    print("7 - Sair")

def salvar_tarefas(tarefas, arquivo="tarefas.json"):
    with open(arquivo, "w") as f:
        json.dump(tarefas, f, indent=4)

def carregar_tarefas(arquivo="tarefas.json"):
    try:
        with open(arquivo, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def adicionar_tarefa(tarefas):
    descricao = input("✏ Digite a descrição da tarefa: ")
    nova_tarefa = {
        "id": len(tarefas) + 1,
        "descricao": descricao,
        "concluido": False,
        "data_criacao": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "data_conclusao": None
    }
    tarefas.append(nova_tarefa)
    salvar_tarefas(tarefas)
    print("✅ Tarefa adicionada com sucesso!")

def ordenar_tarefas(tarefas):
    pendentes = [x for x in tarefas if not x["concluido"]]
    concluidas = [x for x in tarefas if x["concluido"]]
    return pendentes + concluidas

def listar_tarefas(tarefas):
    tarefas_ordenadas = ordenar_tarefas(tarefas)
    if not tarefas_ordenadas:
        print("📭 Nenhuma tarefa encontrada!")
        return
    print("\n📌 Lista de Tarefas:")
    print("-" * 150)
    for tarefa in tarefas_ordenadas:
        status = "✔ Concluída" if tarefa["concluido"] else "❌ Pendente"
        data_criacao = tarefa["data_criacao"]
        data_conclusao = tarefa["data_conclusao"] if tarefa["data_conclusao"] else "Ainda não concluída"
        print(f'ID: {tarefa["id"]:<3} | {tarefa["descricao"]:<30} | {status} | Criada: {data_criacao} | Concluída: {data_conclusao}')
    print("-" * 150)


def marcar_como_concluida(tarefas):
    listar_tarefas(tarefas)
    try:
        id_tarefa = int(input("✅ Digite o ID da tarefa concluída: "))
        for tarefa in tarefas:
            if tarefa["id"] == id_tarefa:
                tarefa["concluido"] = True
                tarefa["data_conclusao"] = datetime.now().strftime("%d/%m/%Y %H:%M")  # Data de conclusão
                salvar_tarefas(tarefas)
                print("✔ Tarefa marcada como concluída!")
                return
        print("⚠ Tarefa não encontrada.")
    except ValueError:
        print("⚠ Digite um número válido.")


def editar_tarefa(tarefas):
    listar_tarefas(tarefas)
    try:
        id_tarefa = int(input("✅ Digite o ID da tarefa: "))
        for tarefa in tarefas:
            if tarefa["id"] == id_tarefa:
                nova_desc = input("✏ Digite a descrição da tarefa: ").strip()
                if not nova_desc:
                    print("⚠ A descrição não pode estar vazia.")
                    return
                tarefa["descricao"] = nova_desc
                salvar_tarefas(tarefas)
                print("✔ Tarefa atualizada!")
                return
        print('⚠ Tarefa não encontrada.')
    except ValueError:
        print("⚠ Digite um número válido.")

def excluir_tarefa(tarefas):
    listar_tarefas(tarefas)
    try:
        id_tarefa = int(input("🗑️ Digite o ID da tarefa para excluir: "))
        nova_lista = [tarefa for tarefa in tarefas if tarefa["id"] != id_tarefa]
        if len(nova_lista) == len(tarefas):
            print("⚠ Tarefa não encontrada.")
        else:
            tarefas.clear()
            tarefas.extend(nova_lista)
            salvar_tarefas(tarefas)
            print("🗑️ Tarefa excluída com sucesso!")
    except ValueError:
        print("⚠ Digite um número válido.")

def exportar_para_csv(tarefas):
    with open("tarefas.csv", "w", newline="", encoding="utf-8") as arquivo:
        escritor_csv = csv.writer(arquivo)
        escritor_csv.writerow(["ID", "Descrição", "Status", "Data de Criação", "Data de Conclusão"])
        
        for tarefa in tarefas:
            status = "Concluída" if tarefa["concluido"] else "Pendente"
            escritor_csv.writerow([tarefa["id"], tarefa["descricao"], status, tarefa["data_criacao"], tarefa["data_conclusao"]])

    print("✅ Tarefas exportadas com sucesso para `tarefas.csv`!")


tarefas_lista = carregar_tarefas()

while True:
    menu()
    opcao = input("💡 Escolha uma opção: ")

    if opcao == "1":
        adicionar_tarefa(tarefas_lista)
    elif opcao == "2":
        listar_tarefas(tarefas_lista)
    elif opcao == "3":
        marcar_como_concluida(tarefas_lista)
    elif opcao == "4":
        editar_tarefa(tarefas_lista)
    elif opcao == "5":
        excluir_tarefa(tarefas_lista)
    elif opcao == "6":
        exportar_para_csv(tarefas_lista)
    elif opcao == "7":
        salvar_tarefas(tarefas_lista)
        print("👋 Saindo... Suas tarefas foram salvas!")
        break
    else:
        print("⚠ Opção inválida, tente novamente.")
