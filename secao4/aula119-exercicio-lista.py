# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

import os
import json

path = '/home/juliana/OneDrive/Estudos/Cursos Udemy/Python/curso_python/secao4/'
file = 'Task_List.json'
taskList = []
taskListRedo = []

def insertTask(list):
    task = input("\nQual tarefa gostaria de inserir na lista?\n")
    list.append(task)
    return taskList

def printTaskList(list):
    print ('\nSUA LISTA DE TAREFAS',*list, sep='\n', end='\n\n')

def undo(list,listRedo):
    if len(list) > 0:
        listRedo.append(list[-1])
        list.pop()
    else:
        print('Não há tarefas para desfazer')
    return list, listRedo

def redo(list, listRedo):
    if len(listRedo) > 0:
        list.append(listRedo[-1])
        listRedo.pop()
    else:
        print('Não há tarefas para refazer')
    return list

def load(path_file):
    list = []
    try:
        with open(path_file, 'r') as file_object:
            list = json.load(file_object)
    except FileNotFoundError:
        save(list, path_file)
    return list

def save(list, path_file):
    with open(path_file, 'w') as file_object:
        json.dump(list,file_object,ensure_ascii=False,indent=2)
    return list

    
taskList = load(path+file)
while True:
    action = input('\nComandos: add, list, undo e redo, clear, quit\n')

    if action == 'list':
        printTaskList(taskList)
    elif action == 'add':
        insertTask(taskList)
        printTaskList(taskList)
    elif action == 'undo':
        undo(taskList,taskListRedo)
        printTaskList(taskList)
    elif action == 'redo':
        redo(taskList,taskListRedo)
        printTaskList(taskList)
    elif action == 'clear':
        os.system('clear')
    elif action == 'quit':
        save(taskList, path+file)
        print('Salvando e Saindo')
        break
    else:
        print('Comando inválido')
