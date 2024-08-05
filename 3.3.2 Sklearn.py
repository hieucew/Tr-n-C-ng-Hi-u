import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Dữ liệu giả lập về lượng mưa và nhiệt độ
rainfall = np.array([78, 60, 82, 98, 120, 140, 160, 150, 130, 110, 90, 70]).reshape(-1, 1)
temperature = np.array([15, 16, 18, 20, 23, 25, 27, 26, 24, 21, 18, 16])

# Chia dữ liệu thành tập huấn luyện và tập kiểm tra
X_train, X_test, y_train, y_test = train_test_split(rainfall, temperature, test_size=0.2, random_state=42)

# Tạo và huấn luyện mô hình hồi quy tuyến tính
model = LinearRegression()
model.fit(X_train, y_train)

# Dự đoán nhiệt độ cho tập kiểm tra
y_pred = model.predict(X_test)

# Đánh giá mô hình
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f'Mean Squared Error (MSE): {mse}')
print(f'R² Score: {r2}')

# Trực quan hóa dữ liệu và đường hồi quy
plt.figure(figsize=(10, 5))
plt.scatter(rainfall, temperature, color='red', label='Actual Data')
plt.plot(rainfall, model.predict(rainfall), color='blue', label='Regression Line')
plt.xlabel('Rainfall (mm)')
plt.ylabel('Average Temperature (°C)')
plt.title('Linear Regression: Rainfall vs Temperature')
plt.legend()
plt.show()

# Sử dụng mô hình để đưa ra quyết định
# Ví dụ: Dự đoán nhiệt độ khi lượng mưa là 100 mm
predicted_temperature = model.predict(np.array([[100]]))
print(f'Dự đoán nhiệt độ khi lượng mưa là 100 mm: {predicted_temperature[0]} °C')
