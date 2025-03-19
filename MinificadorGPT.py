import argparse
import json
import xml.etree.ElementTree as ET
import os
import re
import tkinter as tk
from tkinter import filedialog, messagebox


# Funções de minificação
def minificar_html(codigo):
    return re.sub(r'\s+', ' ', codigo).strip()

def minificar_css(codigo):
    return re.sub(r'\s+', ' ', codigo).strip()

def minificar_js(codigo):
    return re.sub(r'\s+', ' ', codigo).strip()

def minificar_json(codigo):
    return json.dumps(json.loads(codigo), separators=(',', ':'))

def minificar_svg(codigo):
    tree = ET.ElementTree(ET.fromstring(codigo))
    root = tree.getroot()
    
    for elem in root.iter():
        if 'id' in elem.attrib:
            del elem.attrib['id']
        if 'style' in elem.attrib:
            del elem.attrib['style']

    return ET.tostring(root, encoding='utf-8').decode('utf-8')


# Funções de minificação para arquivos
def minificar_arquivo(input_file, output_file, tipo):
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            codigo = f.read()
        
        if tipo == 'html':
            codigo_minificado = minificar_html(codigo)
        elif tipo == 'css':
            codigo_minificado = minificar_css(codigo)
        elif tipo == 'js':
            codigo_minificado = minificar_js(codigo)
        elif tipo == 'json':
            codigo_minificado = minificar_json(codigo)
        elif tipo == 'svg':
            codigo_minificado = minificar_svg(codigo)

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(codigo_minificado)

        print(f"Arquivo {tipo} minificado salvo em: {output_file}")
    except Exception as e:
        print(f"Erro ao processar o arquivo {tipo}: {e}")


# Linha de comando
def linha_de_comando():
    parser = argparse.ArgumentParser(description='Minificador de arquivos HTML, CSS, JS, JSON e SVG')
    
    parser.add_argument('tipo', choices=['html', 'css', 'js', 'json', 'svg'], help='Tipo de arquivo para minificar')
    parser.add_argument('input', help='Arquivo de entrada')
    parser.add_argument('output', help='Arquivo de saída')
    
    args = parser.parse_args()
    
    minificar_arquivo(args.input, args.output, args.tipo)


# Interface gráfica com Tkinter
def minificar_gui():
    def escolher_arquivo():
        arquivo = filedialog.askopenfilename()
        input_entry.delete(0, tk.END)
        input_entry.insert(0, arquivo)

    def salvar_arquivo():
        arquivo = filedialog.asksaveasfilename(defaultextension=".min.html")
        output_entry.delete(0, tk.END)
        output_entry.insert(0, arquivo)

    def minificar():
        tipo = tipo_var.get()
        input_file = input_entry.get()
        output_file = output_entry.get()
        
        minificar_arquivo(input_file, output_file, tipo)
        
        messagebox.showinfo("Sucesso", "Arquivo minificado com sucesso!")

    root = tk.Tk()
    root.title("Minificador de Arquivos")

    # Entradas e botões
    input_label = tk.Label(root, text="Arquivo de entrada:")
    input_label.grid(row=0, column=0)
    input_entry = tk.Entry(root, width=40)
    input_entry.grid(row=0, column=1)
    browse_button = tk.Button(root, text="Escolher", command=escolher_arquivo)
    browse_button.grid(row=0, column=2)

    output_label = tk.Label(root, text="Arquivo de saída:")
    output_label.grid(row=1, column=0)
    output_entry = tk.Entry(root, width=40)
    output_entry.grid(row=1, column=1)
    save_button = tk.Button(root, text="Salvar", command=salvar_arquivo)
    save_button.grid(row=1, column=2)

    tipo_label = tk.Label(root, text="Tipo de arquivo:")
    tipo_label.grid(row=2, column=0)
    tipo_var = tk.StringVar()
    tipo_var.set('html')  # valor padrão
    tipo_menu = tk.OptionMenu(root, tipo_var, 'html', 'css', 'js', 'json', 'svg')
    tipo_menu.grid(row=2, column=1)

    minificar_button = tk.Button(root, text="Minificar", command=minificar)
    minificar_button.grid(row=3, column=1)

    root.mainloop()


# Função principal
def main():
    # Verificar se estamos executando pela linha de comando ou interface gráfica
    if len(os.sys.argv) > 1:
        linha_de_comando()
    else:
        minificar_gui()


if __name__ == '__main__':
    main()

