import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re


def create_treatment_column(single_data):
    """This function create a treatment's list:
    1 - Miss.
    2 - Mr.
    3 - Mrs.
    4 - Master
    5 - Others"""
    if re.findall(r".+(M|m)iss.+", single_data):
        return "Miss"
    elif re.findall(r".+(M|m)rs.+", single_data):
        return "Mrs"
    elif re.findall(r".+(M|m)r.+", single_data):
        return "Mr"
    elif re.findall(r".+(M|m)aster.+", single_data):
        return "Master"
    return "Others"  # Others


titanic_data = pd.read_csv("titanic_data.csv")
titanic_data = titanic_data.iloc[:, 1:]
titanic_data["Treatment"] = titanic_data["Name"]
titanic_data["Treatment"] = titanic_data["Treatment"].apply(
    create_treatment_column)
# titanic_data["Treatment"].astype("int64")
# print("Missed Data: ")
# print(titanic_data.isnull().sum(axis="index"))

# titanic_data.dropna(subset=["Age"], inplace=True)
# titanic_data.reset_index(inplace=True)

# print(titanic_data.head(50))

# missing data
fig, ax = plt.subplots(figsize=(9, 5))
sns.heatmap(titanic_data.isnull(), cbar=False)
plt.show()

# probabilidade de sobrevivência de acordo com os campos
cols = ["Survived", "Sex", "SibSp", "Parch",
        "Pclass", "Embarked", "Treatment"]

n_rows = 3
n_columns = 3

fig, axs = plt.subplots(n_rows, n_columns, figsize=(n_rows*3.5, n_columns*3))

for i in range(n_rows):
    for j in range(n_columns):
        z = i*n_columns+j
        ax = axs[i][j]
        if z < 7:
            sns.countplot(titanic_data[cols[z]],
                          hue=titanic_data["Survived"], ax=ax)
            ax.set_title(cols[z], fontsize=14, fontweight="bold")
            ax.legend(title="survived", loc='upper center')
plt.tight_layout()
plt.show()

# Distribuição da idade em função do sexo, classe e sobrevivência
bins = np.arange(0, 80, 5)
g = sns.FacetGrid(titanic_data, row="Sex", col="Pclass",
                  hue="Survived", margin_titles=True, aspect=1.2)
g.map(sns.distplot, "Age", kde=False, bins=bins, hist_kws=dict(alpha=0.7))
g.add_legend()
plt.show()


bins = np.arange(0, 300, 20)
g = sns.FacetGrid(titanic_data, row="Sex", col="Pclass",
                  hue="Survived", margin_titles=True, aspect=1.2)
g.map(sns.distplot, "Fare", kde=False, bins=bins, hist_kws=dict(alpha=0.7))
g.add_legend()
plt.show()
