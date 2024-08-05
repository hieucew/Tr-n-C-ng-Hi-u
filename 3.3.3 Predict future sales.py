import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Dữ liệu giả lập về doanh số bán hàng hàng tháng
data = {
    'Month': np.arange(1, 37),  # 3 năm dữ liệu (36 tháng)
    'Sales': [1000, 1200, 1300, 1400, 1500, 1600, 1700, 1600, 1500, 1400, 1300, 1200,
              1100, 1300, 1400, 1500, 1600, 1700, 1800, 1700, 1600, 1500, 1400, 1300,
              1200, 1400, 1500, 1600, 1700, 1800, 1900, 1800, 1700, 1600, 1500, 1400]
}

df = pd.DataFrame(data)

# Chia dữ liệu thành tập huấn luyện và tập kiểm tra
X = df['Month'].values.reshape(-1, 1)
y = df['Sales'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Tạo và huấn luyện mô hình hồi quy tuyến tính
model = LinearRegression()
model.fit(X_train, y_train)

# Dự đoán doanh số bán hàng cho tập kiểm tra
y_pred = model.predict(X_test)

# Đánh giá mô hình
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f'Mean Squared Error (MSE): {mse}')
print(f'R² Score: {r2}')

# Trực quan hóa dữ liệu và đường hồi quy
plt.figure(figsize=(10, 5))
plt.scatter(X, y, color='red', label='Actual Sales')
plt.plot(X, model.predict(X), color='blue', label='Regression Line')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Linear Regression: Month vs Sales')
plt.legend()
plt.show()

# Sử dụng mô hình để dự đoán doanh số bán hàng trong tương lai
future_months = np.arange(37, 49).reshape(-1, 1)  # Tháng 37 đến tháng 48
future_sales_pred = model.predict(future_months)

print(f'Dự đoán doanh số bán hàng cho 12 tháng tiếp theo: {future_sales_pred}')
