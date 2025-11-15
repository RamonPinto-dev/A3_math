import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

#variável e função
x = sp.Symbol('x')
f = x**2 - 4*x + 4  # Exemplo: mínimo em x=2

# Derivada primeira
primeiro = sp.diff(f, x)
print(f"Derivada primeira: {primeiro}")  

# Pontos críticos: resolver f'(x) = 0
pontocritico = sp.solve(primeiro, x)
print(f"Pontos críticos (f'(x)=0): {pontocritico}")  # Saída: [2]

# Derivada segunda para classificar
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
# Para checagem básica, podemos avaliar limites
for ponto in pontocritico:
    limiteesquerdo = sp.limit(f, x, ponto, '-')
    limitedireito = sp.limit(f, x, ponto, '+')

if limiteesquerdo == limitedireito == f.subs(x, ponto):
    print(f"Função é contínua em {ponto}")
else:
    print(f"Função não é contínua em {ponto}") 
    

# GRÁFICO DA FUNÇÃO

# criar função numérica
ffunc = sp.lambdify(x, f, 'numpy')

# intervalo para o gráfico
xs = np.linspace(-2, 6, 400)
ys = ffunc(xs)

plt.figure(figsize=(8,5))
plt.plot(xs, ys, label="f(x) = x² - 4x + 4")

# marcar o ponto mínimo x=2
xmin = pontocritico[0]
ymin = ffunc(xmin)

plt.scatter([xmin], [ymin], color='red', s=80, label=f"Mínimo em x={xmin}")
plt.title("Gráfico da Função")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()
plt.show()
# MÉTODO DE OTIMIZAÇÃO (GRADIENTE)

# transformar derivada simbólica em função numérica
fprime = sp.lambdify(x, primeiro, 'numpy')
ffunc = sp.lambdify(x, f, 'numpy')

# Parâmetros do gradiente descendente
x0 = 8.0          # ponto inicial
taxa = 0.1        # learning rate
eps = 1e-6        # tolerância
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
