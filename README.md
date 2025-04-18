# 🤖 Automação de Consultas e Limpeza de Dados — Estágio

Este projeto foi desenvolvido durante meu período de estágio com o objetivo de automatizar consultas repetitivas de números em um sistema web, resolver captchas manualmente e organizar os resultados diretamente em planilhas Excel.

Além disso, foram criados scripts auxiliares para tratar e limpar dados automaticamente em arquivos `.csv`, otimizando o fluxo de trabalho e reduzindo erros humanos.

---

## 💡 Objetivo do Projeto

Automatizar o processo de consulta e coleta de dados em sistemas com captcha manual, incluindo:

- Abertura e navegação pelo sistema.
- Seleção automática de arquivos.
- Detecção de campos captcha.
- Copia e cola de resultados para Excel.
- Limpeza de dados em planilhas CSV.
- Salvamento final dos resultados processados.

---

## 🗂️ Estrutura de Pastas

```
Leads/
├── Codigo/                # Scripts Python
│   ├── abrMeuCodigo deepsek.py        # Script principal de automação.
│   ├── abrMeuCodigo.py                # Versão base do script de automação.
│   ├── abrTelecomConsultaNumero.py    # Consultas específicas de número.
│   ├── apaga as pri repetidas.py      # Script para remoção de duplicatas.
│   ├── apaga99linhas.py               # Script que apaga as 99 primeiras linhas.
│   ├── apagarLinha.py                 # Função auxiliar de limpeza.
│   ├── teste.py                       # Arquivo de testes.
│   └── testeClicks.py                 # Testes de cliques automatizados.
│
└── parar apagar/         # Arquivos de entrada e saída
    ├── Para apagar.csv                # Arquivo principal de leads.
    ├── Para apagar - Copia.csv        # Backup do arquivo principal.
    ├── Para apagar - Copia 2.csv      # Backup secundário.
    ├── Para colar.xlsx                # Planilha de destino dos dados.
    └── todas 2 tratado.csv           # Arquivo final tratado.
```

---

## ⚙️ Tecnologias Utilizadas

- Python 3.x
- PyAutoGUI — Controle de mouse e teclado.
- Clipboard e Pyperclip — Manipulação de área de transferência.
- Pandas — Leitura e manipulação de arquivos CSV.
- Tempo de espera dinâmico para estabilidade.

---

## 🔥 Como funciona

1️⃣ **Execução de Scripts Python**  
Os arquivos `.py` localizados em `Codigo` realizam tarefas específicas, desde consultas em páginas web, extração de dados, até limpeza e padronização de planilhas.

2️⃣ **Arquivos de Dados**  
Os arquivos `.csv` localizados em `parar apagar` são as bases que o script manipula, tratando e atualizando conforme a necessidade.

3️⃣ **Automação com Captcha Assistido**  
O script permite a pausa manual caso detecte necessidade de digitação de captcha, garantindo segurança e precisão no processo.

---

## 💻 Pré-requisitos

- Python 3.x instalado.
- Bibliotecas: `pyautogui`, `pyperclip`, `clipboard`, `pandas`.
  
Instalar dependências:
```bash
pip install pyautogui pyperclip clipboard pandas
```

---

## 🚀 Como usar

1. Ajuste os caminhos dos arquivos no script se necessário.
2. Execute o script `abrMeuCodigo deepsek.py`.
3. Quando solicitado, insira o captcha manualmente.
4. O script cuidará do resto: seleção, cópia, colagem e salvamento no Excel.

---

## ⚠️ Observações

- Este projeto foi desenvolvido para uso interno durante o estágio e customizado para o ambiente da empresa.
- Pode necessitar ajustes de coordenadas (mouse) dependendo da resolução da máquina.
- Scripts de manipulação de planilhas foram otimizados para arquivos específicos e podem não funcionar corretamente com outros layouts.

---

💼 **Desenvolvido por:** Mateus Araujo Monteiro e Wilgne  
🔗 *Estagiário de Desenvolvimento / Automação de Processos*
