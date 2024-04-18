import pandas as pd

data = {
    'name': ['Jhon', 'Jane', 'Mike', 'Emily', 'nombre mas largo'],
    'age': [32, 25, 18, 45, 30],
    'address': ['La habana', 'madrid', 'quito', 'matanzas', 'valencia']
}

df= pd.DataFrame(data)
print(df)