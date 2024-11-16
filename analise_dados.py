import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr
import statsmodels.api as sm
from tabulate import tabulate

# Lê o arquivo CSV
df = pd.read_csv("Employee.csv")
print()
print(df.head())


#Gender
perc_genero = df["Gender"].value_counts(normalize= True) *100
abs_genero = df["Gender"].value_counts()

tabGenero = pd.DataFrame({
    'Frequência': abs_genero,
    'perc (%)': perc_genero
})

tabGenero['perc (%)'] = tabGenero['perc (%)'].apply(lambda x: f"{x:.2f}")

df['Gender_numerical'] = df['Gender'].map({'Male': 0, 'Female': 1})


#Education
perc_qualificacao = df["Education"].value_counts(normalize= True) *100
abs_qualificacao = df["Education"].value_counts()

qualificacoes_filtradas = ["Masters", "Bachelors", "PHD"]
abs_qualificacao_filtrada = abs_qualificacao[qualificacoes_filtradas]
perc_qualificacao_filtrada = perc_qualificacao[qualificacoes_filtradas]

tabQualificacao = pd.DataFrame({
    'Frequência': abs_qualificacao_filtrada,
    'Porcentagem (%)': perc_qualificacao_filtrada
})

tabQualificacao['Porcentagem (%)'] = tabQualificacao['Porcentagem (%)'].apply(lambda x: f"{x:.2f}")

education_map = {'Bachelors': 3, 'Masters': 2, 'PHD': 1}

df['Education_numerical'] = df['Education'].map(education_map)


media_educacao = df['Education_numerical'].mean()

print(f"\nA média de Educação é: {media_educacao:.2f} \n")


#JoiningYear
abs_joining_year = df["JoiningYear"].value_counts()
perc_joining_year = df["JoiningYear"].value_counts(normalize=True) * 100

tabJoiningYear = pd.DataFrame({
    'Frequência': abs_joining_year,
    'Porcentagem (%)': perc_joining_year
})
tabJoiningYear['Porcentagem (%)'] = tabJoiningYear['Porcentagem (%)'].apply(lambda x: f"{x:.2f}")



#PaymentTier
abs_payment_tier = df["PaymentTier"].value_counts()
perc_payment_tier = df["PaymentTier"].value_counts(normalize=True) * 100

tabPaymentTier = pd.DataFrame({
    'Frequência': abs_payment_tier,
    'Porcentagem (%)': perc_payment_tier
})
tabPaymentTier['Porcentagem (%)'] = tabPaymentTier['Porcentagem (%)'].apply(lambda x: f"{x:.2f}")

media_PaymentTier = df['PaymentTier'].mean()

print(f"A média de PaymentTier é: {media_PaymentTier:.2f} \n")




#Age
abs_age = df["Age"].value_counts()
perc_age = df["Age"].value_counts(normalize=True) * 100
tabAge = pd.DataFrame({
    'Frequência': abs_age,
    'Porcentagem (%)': perc_age
})

tabAge['Porcentagem (%)'] = tabAge['Porcentagem (%)'].apply(lambda x: f"{x:.2f}")

media_idade = df["Age"].mean()
mediana_idade = df["Age"].median()  
moda_idade = df["Age"].mode()[0]  

print(f"A média de idade é {media_idade:.2f}")
print(f"A mediana de idade é {mediana_idade:.2f}")
print(f"A moda de idade é {moda_idade:.2f} \n")




#ExperienceDomain
abs_experience_domain = df["ExperienceInCurrentDomain"].value_counts()
perc_experience_domain = df["ExperienceInCurrentDomain"].value_counts(normalize=True) * 100
tabExperienceDomain = pd.DataFrame({
    'Frequência': abs_experience_domain,
    'Porcentagem (%)': perc_experience_domain
})

tabExperienceDomain['Porcentagem (%)'] = tabExperienceDomain['Porcentagem (%)'].apply(lambda x: f"{x:.2f}")

media_experience = df["ExperienceInCurrentDomain"].mean()
mediana_experience = df["ExperienceInCurrentDomain"].median()  
moda_experience = df["ExperienceInCurrentDomain"].mode()[0]  

print(f"A média de ExperienceDomain é {media_experience:.2f}")
print(f"A mediana de ExperienceDomain é {mediana_experience:.2f}")
print(f"A moda de ExperienceDomain é {moda_experience:.2f} \n")




#EverBenched
perc_ever_benched = df["EverBenched"].value_counts(normalize=True) * 100
abs_ever_benched = df["EverBenched"].value_counts()

tabEverBenched = pd.DataFrame({
    'Frequência (EverBenched)': abs_ever_benched,
    'perc (%) (EverBenched)': perc_ever_benched
})
tabEverBenched['perc (%) (EverBenched)'] = tabEverBenched['perc (%) (EverBenched)'].apply(lambda x: f"{x:.2f}")


#LeaveOrNot
perc_leave_or_not = df["LeaveOrNot"].value_counts(normalize=True) * 100
abs_leave_or_not = df["LeaveOrNot"].value_counts()

tabLeaveOrNot = pd.DataFrame({
    'Frequência (Leave or Not)': abs_leave_or_not,
    'perc (%) (Leave or Not)': perc_leave_or_not
})
tabLeaveOrNot['perc (%) (Leave or Not)'] = tabLeaveOrNot['perc (%) (Leave or Not)'].apply(lambda x: f"{x:.2f}")

# Cria o histograma da idade
# Figura 1
plt.figure(figsize=[10, 6])  # (largura, altura)
plt.hist(df["Age"], bins=10, color='skyblue', edgecolor='black')  # 10 bins para a idade
plt.title('Histograma da Idade')
plt.xlabel('Idade')
plt.ylabel('Frequência')
plt.grid(axis='y', alpha=0.75)



tabelas = [
    ('Education', tabQualificacao),
    ('JoiningYear', tabJoiningYear),
    ('PaymentTier', tabPaymentTier),
    ('Age', tabAge),
    ('Gênero', tabGenero),
    ('EverBenched', tabEverBenched),
    ('ExperienceInCurrentDomain', tabExperienceDomain),
    ('LeaveOrNot', tabLeaveOrNot)
]

# Exibir as tabelas de forma formatada
for nome, tabela in tabelas:
    print(f"\nTabela de {nome}:")
    print(tabulate(tabela, headers='keys', tablefmt='fancy_grid', showindex=True))
    print("\n")

media_idadeGenero = df.groupby('Gender')['Age'].mean()
print("\nMédia de idade por gênero:")
print(media_idadeGenero.round(2))

media_pagamentoGenero = df.groupby('Gender')['PaymentTier'].mean()
print("\nMédia de Pagamento por gênero:")
print(media_pagamentoGenero.round(2))


media_educationGenero = df.groupby('Gender')['Education_numerical'].mean()
print("\nMédia de Education por gênero:")
print(media_educationGenero.round(2))

media_experienceGenero = df.groupby('Gender')['ExperienceInCurrentDomain'].mean()

print("\nMédia de ExperienceInCurrentDomain por gênero:")
print(media_experienceGenero.round(2))

# Figura 2
plt.figure(figsize=(10, 6))
sns.barplot(x=media_idadeGenero.index, y=media_idadeGenero.values)
for i, value in enumerate(media_idadeGenero.values):
    plt.text(i, value + 0.05, round(value, 2), ha='center', va='bottom', fontweight='bold')

plt.title('Média de Idade por Gênero')
plt.xlabel('Gênero')
plt.ylabel('Média de Idade')

#Correlação Experiencia Pagamento
correlation, p_value = pearsonr(df['ExperienceInCurrentDomain'], df['PaymentTier'])

print(f"\nCorrelação entre ExperienceInCurrentDomain e PaymentTier: {correlation:.4f}")
print(f"p-valor: {p_value:.4f}")

if p_value < 0.05:
    print("Há uma correlação significativa entre ExperienceInCurrentDomain e PaymentTier.")
else:
    print("Não há uma correlação significativa entre ExperienceInCurrentDomain e PaymentTier.")

#Correlação Educação Pagamento
correlation, p_value = pearsonr(df['Education_numerical'], df['PaymentTier'])

print(f"\nCorrelação entre Education e PaymentTier: {correlation:.4f}")
print(f"p-valor: {p_value:.4f}")

if p_value < 0.05:
    print("Há uma correlação significativa entre Education e PaymentTier.")
else:
    print("Não há uma correlação significativa entre Education e PaymentTier.")

# Correlação Idade e Experiencia
correlation, p_value = pearsonr(df['Age'], df['ExperienceInCurrentDomain'])

print(f"\nCorrelação entre Age e ExperienceInCurrentDomain: {correlation:.4f}")
print(f"p-valor: {p_value:.4f}")

if p_value < 0.05:
    print("Há uma correlação significativa entre Age e ExperienceInCurrentDomain.")
else:
    print("Não há uma correlação significativa entre Age e ExperienceInCurrentDomain.")

correlation, p_value = pearsonr(df['LeaveOrNot'], df['PaymentTier'])

print(f"\nCorrelação entre LeaveOrNot e PaymentTier: {correlation:.4f}")
print(f"p-valor: {p_value:.4f}")

if p_value < 0.05:
    print("Há uma correlação significativa entre LeaveOrNot e PaymentTier.")
else:
    print("Não há uma correlação significativa entre LeaveOrNot e PaymentTier.")


# Função para plotar gráfico de dispersão com linha de regressão
def plot_correlation(x, y, xlabel, ylabel, correlation, p_value, title):
    plt.figure(figsize=(8, 6))
    sns.regplot(x=x, y=y, data=df, scatter_kws={'s': 50, 'color': 'blue'}, line_kws={'color': 'red'})
    
    # Adicionando título e rótulos
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    
    # Adicionando o texto com a correlação e o p-valor no gráfico
    plt.text(0.05, 0.95, f"Correlação: {correlation:.4f}\np-valor: {p_value:.4f}", 
             horizontalalignment='left', verticalalignment='top', transform=plt.gca().transAxes, 
             fontsize=12, bbox=dict(facecolor='white', alpha=0.7, edgecolor='none', boxstyle='round,pad=0.5'))


# Exemplo para 'ExperienceInCurrentDomain' vs 'PaymentTier'
correlation, p_value = pearsonr(df['ExperienceInCurrentDomain'], df['PaymentTier'])
plot_correlation(df['ExperienceInCurrentDomain'], df['PaymentTier'], 
                  'Experience in Current Domain', 'Payment Tier', 
                  correlation, p_value, 'Correlação entre ExperienceInCurrentDomain e PaymentTier')

# Exemplo para 'Education_numerical' vs 'PaymentTier'
correlation, p_value = pearsonr(df['Education_numerical'], df['PaymentTier'])
plot_correlation(df['Education_numerical'], df['PaymentTier'], 
                  'Education (Numerical)', 'Payment Tier', 
                  correlation, p_value, 'Correlação entre Education e PaymentTier')

# Exemplo para 'Age' vs 'ExperienceInCurrentDomain'
correlation, p_value = pearsonr(df['Age'], df['ExperienceInCurrentDomain'])
plot_correlation(df['Age'], df['ExperienceInCurrentDomain'], 
                  'Age', 'Experience in Current Domain', 
                  correlation, p_value, 'Correlação entre Age e ExperienceInCurrentDomain')

# Exemplo para 'LeaveOrNot' vs 'PaymentTier'
correlation, p_value = pearsonr(df['LeaveOrNot'], df['PaymentTier'])
plot_correlation(df['LeaveOrNot'], df['PaymentTier'], 
                  'Leave or Not', 'Payment Tier', 
                  correlation, p_value, 'Correlação entre LeaveOrNot e PaymentTier')

plt.show()