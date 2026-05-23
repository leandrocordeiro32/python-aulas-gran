import matplotlib.pyplot as plt

'''
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun']
qtdTI = [60, 52, 70, 89, 108, 95]
qtdRH = [56, 58, 67, 79, 92, 95]

# plt.plot(meses, valores)
# plt.bar(meses, valores)

# plt.bar(meses, qtdTI, label='TI', color='blue')
# plt.bar(meses, qtdRH, label='RH', color="#e72625")

plt.plot(meses, qtdTI, label='TI', color='blue', linestyle='-.', marker='o')
plt.plot(meses, qtdRH, label='RH', color="#e72625", marker='.')

plt.title('Chamados Abertos')
plt.xlabel('Meses')
plt.ylabel('Quantidade')
plt.legend()
plt.show()
'''
navegadores = ['Chrome', 'Firefox', 'Edge']
qtd = [1200, 600, 200]
cores = ['purple', 'black', 'yellow']

plt.pie(qtd, labels=navegadores, colors=cores)
plt.show()