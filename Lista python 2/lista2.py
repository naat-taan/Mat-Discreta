import matplotlib.pyplot as plt
import numpy as np

# Função do primeiro grau
def funcao1oGrau(a, b, x):
    return a * x + b

# Função do segundo grau
def funcao2oGrau(a, b, c, x):
    return a * x**2 + b * x + c

# Função exponencial
def funcaoExponencial(a, b, x):
    return a * (b**x)

# Função modular
def funcaoModular(x):
    return abs(x)

# Função seno
def funcaoSeno(x):
    return np.sin(x)

# Criação do vetorX
vetorX = np.arange(-5, 5, 1)
print("vetorX:", vetorX)

# Parâmetros da função do primeiro grau
a = 2
b = 5

# Criação do vetorY
vetorY = [funcao1oGrau(a, b, x) for x in vetorX]

# Geração do gráfico discreto
plt.scatter(vetorX, vetorY, label="Função 1o Grau")
plt.title('f(x) = ax + b')
plt.xlabel('eixo x')
plt.ylabel('eixo y')
plt.legend()
plt.grid(True, which='both')
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.show()

# Alteração do terceiro parâmetro de arange para 0.5
vetorX = np.arange(-5, 5, 0.5)
vetorY = [funcao1oGrau(a, b, x) for x in vetorX]

# Geração do gráfico discreto com novo vetorX
plt.scatter(vetorX, vetorY, label="Função 1o Grau (passo 0.5)")
plt.title('f(x) = ax + b')
plt.xlabel('eixo x')
plt.ylabel('eixo y')
plt.legend()
plt.grid(True, which='both')
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.show()

# Alteração para função plot
plt.plot(vetorX, vetorY, label="Função 1o Grau (contínua)")
plt.title('f(x) = ax + b')
plt.xlabel('eixo x')
plt.ylabel('eixo y')
plt.legend()
plt.grid(True, which='both')
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.show()

# Parâmetros e gráficos para funções adicionais
vetorX = np.arange(-5, 5, 0.1)

# Função do 2° grau
vetorY = [funcao2oGrau(1, 0, 0, x) for x in vetorX]
plt.plot(vetorX, vetorY, label="Função 2o Grau")
plt.title('f(x) = ax^2 + bx + c')
plt.xlabel('eixo x')
plt.ylabel('eixo y')
plt.legend()
plt.grid(True, which='both')
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.show()

# Função exponencial
vetorY = [funcaoExponencial(1, 2, x) for x in vetorX]
plt.plot(vetorX, vetorY, label="Função Exponencial")
plt.title('f(x) = a * b^x')
plt.xlabel('eixo x')
plt.ylabel('eixo y')
plt.legend()
plt.grid(True, which='both')
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.show()

# Função modular
vetorY = [funcaoModular(x) for x in vetorX]
plt.plot(vetorX, vetorY, label="Função Modular")
plt.title('f(x) = |x|')
plt.xlabel('eixo x')
plt.ylabel('eixo y')
plt.legend()
plt.grid(True, which='both')
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.show()

# Função seno
vetorY = [funcaoSeno(x) for x in vetorX]
plt.plot(vetorX, vetorY, label="Função Seno")
plt.title('f(x) = sin(x)')
plt.xlabel('eixo x')
plt.ylabel('eixo y')
plt.legend()
plt.grid(True, which='both')
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.show()