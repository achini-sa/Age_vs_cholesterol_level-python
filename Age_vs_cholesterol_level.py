# Create a scatter plot of age against cholesterol level using Matplotlib
import pandas as pd
import matplotlib.pyplot as plt


excel_file = 'heart_disease_f.xlsx'
sheet_name = 'Sheet1'

# Read data from the excel file into a dataframe
data = pd.read_excel(excel_file, sheet_name=sheet_name)

# Extract data for the scatter plot 
x_values = data['age'] 
y_values = data['chol']

# Create a scatter plot using Matplotlib ,Female
plt.scatter(x_values, y_values, color = 'hotpink',label = 'Female', marker='*' )

# Add labels and title
plt.xlabel('Age')
plt.ylabel('Cholesterol Level')
plt.title('Scatter Plot: Age vs. Cholesterol Level')


excel_file = 'heart_disease_m.xlsx'
sheet_name = 'Sheet1'

# Read data from the excel file into a dataframe
data = pd.read_excel(excel_file, sheet_name=sheet_name)

# Extract data for the scatter plot
x_values = data['age']  
y_values = data['chol'] 

# Create a scatter plot using Matplotlib ,Male
plt.scatter(x_values, y_values, color = 'skyblue' ,label = 'Male')

# Add labels and title
plt.xlabel('Age')
plt.ylabel('Cholesterol Level')
plt.title('Scatter Plot: Age vs. Cholesterol Level')


# Add legend
plt.legend(loc='upper right')

# Show the plot
plt.show()

#Run the application