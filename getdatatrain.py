import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Đọc cookie từ file JSON
with open("cookies.json", "r") as file:
    cookies = json.load(file)

# Khởi tạo trình duyệt
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Truy cập Shopee để thiết lập domain
driver.get("https://shopee.vn")

# Thêm cookie từ file JSON
for cookie in cookies:
    # Đảm bảo trường "sameSite" hợp lệ
    if "sameSite" not in cookie or cookie["sameSite"] not in ["Strict", "Lax", "None"]:
        cookie["sameSite"] = "Lax"  # Giá trị mặc định nếu không hợp lệ
    # Xóa các trường không cần thiết
    cookie.pop("storeId", None)
    cookie.pop("index", None)
    cookie.pop("isSearch", None)
    # Thêm cookie vào trình duyệt
    driver.add_cookie(cookie)

# Refresh trình duyệt để áp dụng cookie
driver.refresh()

# Chờ để kiểm tra giao diện sau khi áp dụng cookie
input("Nhấn Enter để thoát...")

# Đóng trình duyệt
driver.quit()
