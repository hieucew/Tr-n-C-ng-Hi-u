import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
from scipy.optimize import linprog
import matplotlib.pyplot as plt
import seaborn as sns

# Create more extensive sample sales data
dates = pd.date_range(start='2023-01-01', periods=100, freq='D')
products = [1, 2, 3]
sales_data = pd.DataFrame({
    'product_id': np.random.choice(products, size=len(dates)),
    'sale_date': np.tile(dates, len(products))[:len(dates)],
    'quantity_sold': np.random.randint(50, 300, size=len(dates))
})
sales_data.to_csv('sales_data.csv', index=False)

# Create sample inventory data
inventory_data = pd.DataFrame({
    'product_id': [1, 2, 3],
    'inventory_level': [500, 400, 300],
    'restock_date': ['2023-01-01', '2023-01-01', '2023-01-01']
})
inventory_data.to_csv('inventory_data.csv', index=False)

# Create sample supplier data
supplier_data = pd.DataFrame({
    'supplier_id': [1, 2, 3],
    'product_id': [1, 2, 3],
    'lead_time': [5, 10, 15]
})
supplier_data.to_csv('supplier_data.csv', index=False)

# Load data from CSV files
sales_data = pd.read_csv('sales_data.csv')
inventory_data = pd.read_csv('inventory_data.csv')
supplier_data = pd.read_csv('supplier_data.csv')

# Merge data into a single DataFrame
data = sales_data.merge(inventory_data, on='product_id').merge(supplier_data, on='product_id')

# Data Cleaning and Preprocessing
data.ffill(inplace=True)
data['sale_date'] = pd.to_datetime(data['sale_date'])
data['restock_date'] = pd.to_datetime(data['restock_date'])
data['quantity_sold'] = data['quantity_sold'].astype(int)
data['inventory_level'] = data['inventory_level'].astype(int)

# Demand Forecasting using ARIMA
sales_agg = data.groupby('sale_date')['quantity_sold'].sum().asfreq('D').fillna(0)
model = ARIMA(sales_agg, order=(5, 1, 0))
model_fit = model.fit()
forecast = model_fit.forecast(steps=30)
forecast_dates = pd.date_range(start=sales_agg.index[-1], periods=30)
forecast_series = pd.Series(forecast, index=forecast_dates)

# Plot the forecast
plt.figure(figsize=(12, 6))
plt.plot(sales_agg, label='Historical Sales')
plt.plot(forecast_series, label='Forecast', color='red')
plt.xlabel('Date')
plt.ylabel('Quantity Sold')
plt.title('Sales Forecast')
plt.legend()
plt.show()

# Inventory Optimization using Linear Programming
c = [5, 7]  # Cost of holding inventory and ordering cost
A = [[1, 0], [0, 1], [-1, -1]]  # Constraints matrix
b = [1000, 500, -200]  # Bounds for constraints
result = linprog(c, A_ub=A, b_ub=b, method='simplex')
print(f'Optimal inventory level: {result.x[0]}')
print(f'Optimal order quantity: {result.x[1]}')

# Visualization and Reporting
plt.figure(figsize=(12, 6))
sns.lineplot(x='restock_date', y='inventory_level', data=data)
plt.xlabel('Date')
plt.ylabel('Inventory Level')
plt.title('Inventory Levels Over Time')
plt.show()

# Generate a report
report = data.groupby('product_id').agg({
    'quantity_sold': 'sum',
    'inventory_level': 'mean',
    'supplier_id': 'nunique'
}).reset_index()

report.columns = ['Product ID', 'Total Quantity Sold', 'Average Inventory Level', 'Unique Suppliers']
report.to_csv('inventory_report.csv', index=False)
