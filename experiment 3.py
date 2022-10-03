import pandas as pd
import seaborn as sns
d=pd.read_csv(r'/Users/samikshabudhiraja/Downloads/train.csv')
import matplotlib.pyplot as plt
#1
survived_count = d.groupby('Survived')['Survived'].count()
print(survived_count)
sns.countplot(x='Survived',data=d)
plt.show()
#2
survived_sex = d.groupby('Sex')['Survived'].sum()
print(survived_sex)
sns.countplot(x='Sex',data=d)
plt.show()
#3
Pclass = d.groupby('Pclass')['Survived'].sum()
print(Pclass)
sns.countplot(x='Pclass',data=d)
plt.show()
#4th part
#Histogram
plt.hist(d["Age"])
plt.xlabel('Age')
plt.ylabel('No. of people')
plt.title('distribution of age')
plt.show()
#5th part
column=len(d.SibSp)
print("count of Sibsp - Sibling, Spouse is : ",column)
sns.countplot(x='SibSp',data=d)
plt.show()




