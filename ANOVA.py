import pandas as pd

# Load dataset
data = pd.read_csv("StroopAccuracy.csv")

# Preview it
print(data.head())

import pingouin as pg

# Example repeated measures ANOVA
aov = pg.rm_anova(
    dv='accuracy',
    within=['congruency', 'trial'],
    subject='participant_id',
    data=data
)

print(aov)

print(data.columns)

data_long = pd.melt(
    data,
    id_vars=['participant_id'],
    var_name='condition',
    value_name='accuracy'
)




