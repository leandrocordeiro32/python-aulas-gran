import numpy as np
import pandas as pd

class Paciente:
    def __init__(self, nome, idade, sexo, peso, altura):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.peso = peso
        self.altura = altura

pacientes = {
    'Paciente 1': Paciente('Madonna', 69, 'F', 60, 1.60),
    'Paciente 2': Paciente('Lady Gaga', 45, 'F', 50, 1.55),
    'Paciente 3': Paciente('Beyonce', 49, 'F', 70, 1.75),
    'Paciente 4': Paciente('Rihanna', 40, 'F', 75, 1.70),
}

l_pacientes = [p.__dict__ for p in pacientes.values()]

df_pacientes = pd.DataFrame.from_records(l_pacientes, index=pacientes.keys())

df_pacientes['IMC'] = df_pacientes.apply(lambda i: i.peso / i.altura ** 2, axis=1)
print(df_pacientes)

media = np.mean(df_pacientes['IMC'])

sobrepeso = df_pacientes[df_pacientes['IMC'] > 25]
print('Paciente(s) com  sobrepeso:')
print(sobrepeso)

percentual = len(sobrepeso) / len(df_pacientes) * 100
print(f'O percentual de pacientes com sobrepeso é {percentual} %.')