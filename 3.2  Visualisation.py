import matplotlib.pyplot as plt
import numpy as np

# Dữ liệu giả lập về lượng mưa trong các tháng của năm
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
rainfall = [78, 60, 82, 98, 120, 140, 160, 150, 130, 110, 90, 70]
temperature = [15, 16, 18, 20, 23, 25, 27, 26, 24, 21, 18, 16]

# 1. Biểu đồ cột (Bar Chart)
plt.figure(figsize=(10, 5))
plt.bar(months, rainfall, color='blue')
plt.xlabel('Months')
plt.ylabel('Rainfall (mm)')
plt.title('Monthly Rainfall')
plt.show()

# Đánh giá ý nghĩa:
# Biểu đồ cột giúp chúng ta dễ dàng so sánh lượng mưa giữa các tháng.
# Ta có thể thấy rõ ràng rằng các tháng mùa hè có lượng mưa cao hơn.

# 2. Biểu đồ đường (Line Chart)
plt.figure(figsize=(10, 5))
plt.plot(months, rainfall, marker='o', linestyle='-', color='green')
plt.xlabel('Months')
plt.ylabel('Rainfall (mm)')
plt.title('Monthly Rainfall')
plt.grid(True)
plt.show()

# Đánh giá ý nghĩa:
# Biểu đồ đường cho thấy xu hướng thay đổi lượng mưa theo thời gian.
# Ta có thể thấy rõ xu hướng tăng lượng mưa từ tháng 1 đến tháng 7, sau đó giảm dần.

# 3. Biểu đồ tròn (Pie Chart)
plt.figure(figsize=(8, 8))
plt.pie(rainfall, labels=months, autopct='%1.1f%%', startangle=140)
plt.title('Rainfall Distribution Throughout the Year')
plt.show()

# Đánh giá ý nghĩa:
# Biểu đồ tròn cho biết tỷ lệ phần trăm lượng mưa của mỗi tháng so với tổng lượng mưa cả năm.
# Giúp ta thấy được tháng nào đóng góp lượng mưa nhiều nhất.

# 4. Biểu đồ phân tán (Scatter Plot)
plt.figure(figsize=(10, 5))
plt.scatter(rainfall, temperature, color='red')
plt.xlabel('Rainfall (mm)')
plt.ylabel('Average Temperature (°C)')
plt.title('Rainfall vs Temperature')
plt.show()

# Đánh giá ý nghĩa:
# Biểu đồ phân tán cho thấy mối quan hệ giữa lượng mưa và nhiệt độ trung bình.
# Từ biểu đồ này, ta có thể thấy rằng nhiệt độ có xu hướng tăng khi lượng mưa tăng đến một mức nhất định.

# 5. Biểu đồ hộp (Box Plot)
plt.figure(figsize=(10, 5))
data = [rainfall, temperature]
plt.boxplot(data, tick_labels=['Rainfall (mm)', 'Temperature (°C)'])
plt.title('Box Plot of Rainfall and Temperature')
plt.show()

# Đánh giá ý nghĩa:
# Biểu đồ hộp cho thấy phân phối của dữ liệu, bao gồm các giá trị trung vị, tứ phân vị và các giá trị ngoại lệ.
# Giúp ta hiểu rõ hơn về sự biến động của lượng mưa và nhiệt độ trong năm.
