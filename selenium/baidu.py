from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

print("Selenium自动化测试示例")

# ======================
# Mac 专用稳定配置（必用）
# ======================
options = webdriver.ChromeOptions()
print("Selenium自动化测试示例1111")

options.add_argument("--no-sandbox")
print("Selenium自动化测试示例2222")
options.add_argument("--disable-dev-shm-usage")
print("Selenium自动化测试示例33333")
# options.add_argument("--headless=new")  # 👈 调试时必须注释！

# ======================
# 启动浏览器
# ======================
driver = webdriver.Chrome(options=options)
print("✅ 浏览器启动成功")

driver.maximize_window()
driver.implicitly_wait(10)

# ======================
# 打开百度
# ======================
driver.get("https://www.baidu.com")
time.sleep(1)

# ======================
# 搜索（只保留稳定逻辑）
# ======================
driver.find_element(By.ID, "kw").send_keys("Selenium 自动化测试")
driver.find_element(By.ID, "su").click()
time.sleep(2)

# ======================
# 等待结果
# ======================
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.ID, "content_left")))

# ======================
# 输出信息
# ======================
print("✅ 页面标题：", driver.title)
print("✅ 当前 URL：", driver.current_url)

# ======================
# 截图
# ======================
driver.get_screenshot_as_file("test.png")
print("✅ 截图已保存：test.png")

# ======================
# 退出
# ======================
time.sleep(3)
driver.quit()
print("✅ 运行完成！")