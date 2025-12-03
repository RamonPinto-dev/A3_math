1. Como baixar o código do GitHub

Opção 1 — Baixar ZIP

Acesse o repositório:
cole aqui o link

Clique em Code

Selecione Download ZIP

Extraia o arquivo no seu computador.

Opção 2 — Clonar via Git

Se tiver o Git instalado, execute:

git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git

2. Instalando as dependências

Este projeto utiliza três bibliotecas:

SymPy — Cálculo simbólico (derivadas, pontos críticos, limites)

NumPy — Cálculo numérico rápido

Matplotlib — Plotar gráficos

Instale tudo de uma vez no terminal com:

pip install sympy numpy matplotlib e caso dê erro de script 
tente python -m pip install sympy numpy matplotlib

3. Se ocorrer erro na instalação

Alguns erros comuns e soluções rápidas:

Erro: pip não reconhecido

Atualize o Python e certifique-se de marcar “Add Python to PATH”.

Solução rápida no Windows:

python -m pip install --upgrade pip

Erro de permissão (PermissionError)

Execute como administrador:

pip install --user sympy numpy matplotlib

Erro: Python desatualizado

NumPy pode exigir versão mais nova.

Verifique sua versão:

python --version


Se for menor que 3.8 → atualize o Python em
https://www.python.org/downloads/

Erro: NumPy não instala por incompatibilidade

Instale versão compatível:

pip install numpy==1.26.4

4. Como executar o código

Na pasta do projeto, rode:

python nome_do_arquivo.py


O programa irá:

calcular derivadas,

mostrar pontos críticos no terminal,

rodar o gradiente descendente,

exibir o gráfico.

e as funções utilizadas, estão comentadas. tire o comentario de uma, e se quiser usar a outra comente a antiga
e vice-versa, para não executar duas de vez

exemplo:
# f = x**2 - 4*x + 4            ou  f= x**2-4*x+4
f = x**3 - 6*x**2 + 4*x + 12    ou #f = x**3 - 6*x**2 + 4*x + 12

e se quiser adicionar uma função nova, só escrever por cima das anteriores
ou criar um f novo e comentar os outros ou apagar, fica aberto ao cliente oque decidir

ex:
f = 3x**2 + 5*x −7
