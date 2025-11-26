import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
# o código otimiza o valor de x que faz a função ficar no menor valor possível.
#baixar as bibliotecas, pip install sympy numpy matplotlib terminal

#função+var
x = sp.Symbol('x')
f = x**2 - 4*x + 4  # Exemplo: mínimo em x=2
# f = x**3 - 6*x**2 + 4*x + 12 # ele não converge, só explode ou seja infinito
#sobe e desce infinito ent n é convexa. dois ponto critico

# Derivada primeira
primeiro = sp.diff(f, x)
print(f"Derivada primeira: {primeiro}")  

# Pontos críticos: f'(x) = 0
pontocritico = sp.solve(primeiro, x)
print(f"Pontos críticos (f'(x)=0): {pontocritico}")  # Saída: [2] unico ponto onde a derivada é 0
# é x

# Derivada segunda classi
segundo = sp.diff(primeiro, x)
print(f"Derivada segunda: {segundo}")  # Saída: 2

for ponto in pontocritico:
    valorsegundaderiva = segundo.subs(x, ponto)
    if valorsegundaderiva > 0:
        print(f"Ponto {ponto}: mínimo local")
    elif valorsegundaderiva < 0:
        print(f"Ponto {ponto}: máximo local")
    else:
        print(f"Ponto {ponto}: ponto de inflexão")

# Verificar continuidade (simples: assumir contínua se diferenciável)
# checagem basic, avalia lim
for ponto in pontocritico:
    limiteesquerdo = sp.limit(f, x, ponto, '-')
    limitedireito = sp.limit(f, x, ponto, '+')

if limiteesquerdo == limitedireito == f.subs(x, ponto):
    print(f"Função é contínua em {ponto}")
else:
    print(f"Função não é contínua em {ponto}") 
    

# HORA DO GRAFICOOO!!!!! foguinho foguinho

# cria função numérica
ffunc = sp.lambdify(x, f, 'numpy')

# intervalo do gráfico
xs = np.linspace(-2, 6, 400)
ys = ffunc(xs)

plt.figure(figsize=(8,5))
plt.plot(xs, ys, label=f"f(x) = ${sp.latex(f)}$") # f = x³ - 6*x²2 + 4*x + 12

for ponto in pontocritico:
    y = ffunc(ponto)
    plt.scatter([ponto], [y], s=80, label=f"Ponto crítico: x={float(ponto):.3f}")
plt.title("Gráfico da Função")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()
plt.show()

#otimizaçãi (GRADIENTE)
#derivada simbólica em função numérica
fprime = sp.lambdify(x, primeiro, 'numpy')
ffunc = sp.lambdify(x, f, 'numpy')

# Parâmetros do gradiente descendente
x0 = 8.0          # ponto inicial
taxa = 0.1        # tamanho do passo
eps = 1e-6        # quando para. épsilon igual a dez elevado a menos seis
max_iter = 100    # número máximo de iterações

x_atual = x0

print("\nOtimização por Gradiente Descendente:")
for i in range(max_iter):
    grad = fprime(x_atual)
    novo_x = x_atual - taxa * grad
    
    print(f"Iteração {i+1}: x = {novo_x:.6f}, f(x) = {ffunc(novo_x):.6f}")
    
    if abs(novo_x - x_atual) < eps:
        print("\nConvergiu!")
        break
    
    x_atual = novo_x

print(f"\nResultado final: x ≈ {x_atual}, f(x) ≈ {ffunc(x_atual)}")
