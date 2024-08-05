import pandas as pd

# Đường dẫn đến tệp Excel (cập nhật đường dẫn chính xác trên máy của bạn)
file_path = 'asm_busenessprocess.xlsx'

# Đọc dữ liệu từ tất cả các trang tính
sheets = ['Sales Data', 'Customer Data', 'Product Data', 'Market Trend Data', 'Website Access Data', 'Product Details']
data_frames = {sheet: pd.read_excel(file_path, sheet_name=sheet) for sheet in sheets}

# Kiểm tra và xử lý dữ liệu trống và trùng lặp
for sheet, df in data_frames.items():
    print(f"\n{sheet} trước khi xử lý:")
    print(df.head())

    # Kiểm tra số lượng giá trị trống trong mỗi cột
    missing_data = df.isnull().sum()
    print(f"\nSố lượng giá trị trống trong mỗi cột của {sheet}:")
    print(missing_data)

    # Loại bỏ các hàng có giá trị trống
    df.dropna(inplace=True)

    # Kiểm tra số lượng hàng trùng lặp
    duplicate_rows = df.duplicated().sum()
    print(f"\nSố lượng hàng trùng lặp trong {sheet}: {duplicate_rows}")

    # Loại bỏ các hàng trùng lặp
    df.drop_duplicates(inplace=True)

    # Cập nhật DataFrame sau khi xử lý
    data_frames[sheet] = df

    print(f"\n{sheet} sau khi xử lý:")
    print(df.head())

# Lưu dữ liệu đã xử lý vào các tệp CSV mới (nếu cần thiết)
for sheet, df in data_frames.items():
    cleaned_file_path = f'cleaned_{sheet.replace(" ", "_")}.csv'
    df.to_csv(cleaned_file_path, index=False)
    print(f"\nDữ liệu đã xử lý của {sheet} đã được lưu vào tệp: {cleaned_file_path}")
