# ( ) Identificar o tema central do template. Qual é a tese principal?
# ( ) Identificar encapsulamento ou distanciamento de palavras-chave desta tese principal. Se houver grande desvio padrão, há baixo encapsulamento. Se houver pequeno desvio padrão, há um bom encapsulamento.
# ( ) Identificar quantidade de adjetivos utilizados vs uso de substativos. Com isso poderá ser verificado se a argumentação é voltada aos fatos ou se não tem esse foco.
# ( )

import tkinter as tk
from tkinter import filedialog
import csv

def select_file():
    root = tk.Tk()
    root.withdraw()
    file_name = filedialog.askopenfilename()
    return file_name

def get_list_incorrect_expressions():
    list_incorrect_expressions = []
    with open('incorrect_expressions.csv', 'r') as csv_file:
        list = csv.reader(csv_file, delimiter = ',')
        for i in list:
            list_incorrect_expressions.append(i)
    return list_incorrect_expressions

def check_incorrect_expressions(file_name, list_incorrect_expressions):
    targetFile = open(file_name, 'r', encoding = 'utf-8')
    line = targetFile.readline()
    list_incorrect_expressions_target_file = []
    while line:
        for e in list_incorrect_expressions:
            if line.find(e[0]) != -1:
                list_incorrect_expressions_target_file.append(e[0])
        line = targetFile.readline()
    for e in list_incorrect_expressions_target_file:
        print(e)
    targetFile.close()

file_name = select_file()
list_incorrect_expressions = get_list_incorrect_expressions()
check_incorrect_expressions(file_name, list_incorrect_expressions)