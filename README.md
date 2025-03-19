# Minificador de Arquivos Web

**Minificador de Arquivos Web** é uma ferramenta desenvolvida em Python para ajudar a otimizar e reduzir o tamanho de arquivos web. O projeto suporta a minificação de **HTML**, **CSS**, **JavaScript (JS)**, **JSON** e **SVG**. Ele oferece uma interface de linha de comando simples e uma interface gráfica (GUI) baseada no **Tkinter**, permitindo ao usuário escolher facilmente os arquivos a serem minificados.

## Funcionalidades

- **Minificação de Arquivos Web**: Suporte para minificar arquivos dos tipos **HTML**, **CSS**, **JavaScript**, **JSON** e **SVG**.
- **Interface de Linha de Comando (CLI)**: Permite a minificação via terminal com argumentos de entrada e saída.
- **Interface Gráfica (GUI)**: Com **Tkinter**, o usuário pode facilmente selecionar os arquivos e minificar com apenas um clique.
- **Redução de Tamanho**: A minificação visa reduzir o tamanho dos arquivos, tornando-os mais rápidos para carregar e mais eficientes para produção.

O objetivo desse projeto é oferecer uma solução simples e rápida para otimizar arquivos usados em websites, tornando-os mais eficientes para a web.

## Pré-requisitos

Para rodar o projeto, você precisa ter o Python 3 instalado em sua máquina. Além disso, o módulo **Tkinter** (para a interface gráfica) precisa estar instalado.

### Instalando o Tkinter (se necessário)

Se o Tkinter não estiver instalado, siga as instruções abaixo:

#### **Windows**:
O Tkinter geralmente já vem pré-instalado com o Python. Caso contrário, reinstale o Python e selecione a opção para incluir o Tkinter.

#### **Linux (Ubuntu/Debian)**:
Execute o seguinte comando para instalar o Tkinter:

```bash
sudo apt-get install python3-tk
```

#### **macOS**:
No macOS, o Tkinter geralmente vem pré-instalado com o Python. Se você tiver problemas, tente reinstalar o Python via **Homebrew**:

```bash
brew install python
```

## Instalação

1. Clone o repositório ou baixe o arquivo `.py` do projeto.

   ```bash
   git clone https://github.com/Manoel-Fernandes/MinificadorGPT.git
   ```

2. Instale qualquer dependência, caso necessário. (O projeto usa bibliotecas padrão, como `json` e `re`, e o `Tkinter` para a interface gráfica).

## Como Usar

### Linha de Comando

Para utilizar o minificador pela linha de comando, use a seguinte sintaxe:

```bash
python MinificadorGPT.py <tipo> <arquivo_entrada> <arquivo_saida>
```

Onde:

- `<tipo>` pode ser `html`, `css`, `js`, `json`, ou `svg`.
- `<arquivo_entrada>` é o caminho para o arquivo que será minificado.
- `<arquivo_saida>` é o caminho onde o arquivo minificado será salvo.

#### Exemplos de uso:

- Minificar um arquivo HTML:
  ```bash
  python MinificadorGPT.py html pagina.html pagina.min.html
  ```

- Minificar um arquivo CSS:
  ```bash
  python MinificadorGPT.py css estilo.css estilo.min.css
  ```

- Minificar um arquivo JavaScript:
  ```bash
  python MinificadorGPT.py js script.js script.min.js
  ```

- Minificar um arquivo JSON:
  ```bash
  python MinificadorGPT.py json dados.json dados.min.json
  ```

- Minificar um arquivo SVG:
  ```bash
  python MinificadorGPT.py svg imagem.svg imagem.min.svg
  ```

### Interface Gráfica (GUI)

Se você preferir uma interface gráfica, basta rodar o script sem argumentos de linha de comando:

```bash
python MinificadorGPT.py
```

Isso abrirá uma janela onde você poderá:

1. Escolher o arquivo de entrada.
2. Escolher o arquivo de saída.
3. Selecionar o tipo de arquivo (HTML, CSS, JS, JSON ou SVG).
4. Minificar o arquivo com apenas um clique!

## Exemplos de Minificação

- **HTML**: Reduz a quantidade de espaços em branco e novas linhas.
- **CSS**: Remove espaços desnecessários, quebras de linha e comentários.
- **JavaScript (JS)**: Remover espaços e quebras de linha entre as instruções, deixando o código mais compacto.
- **JSON**: Remove espaços e formatação extra, deixando apenas os dados.
- **SVG**: Remove atributos como `id` e `style` de elementos não essenciais.

## Contribuindo

Se você encontrar algum erro ou quiser adicionar novas funcionalidades, sinta-se à vontade para abrir um **pull request**. A contribuição é sempre bem-vinda!

1. Faça um fork do repositório.
2. Crie uma branch para a nova funcionalidade (`git checkout -b minha-nova-funcionalidade`).
3. Faça as alterações e commit (`git commit -am 'Adicionando minha nova funcionalidade'`).
4. Envie para o repositório remoto (`git push origin minha-nova-funcionalidade`).
5. Abra um **pull request**.

## Licença

Este projeto está licenciado sob a **MIT License** - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## Agradecimentos

Este projeto foi **totalmente desenvolvido com o auxílio do ChatGPT** (auxílio nada, ele fez tudo, até o readme), da OpenAI, que ajudou a criar o código, implementar as funcionalidades e até solucionar problemas durante o desenvolvimento. Sem a ajuda do ChatGPT, esse projeto não teria saído do papel!

---
