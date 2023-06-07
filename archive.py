import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By


quantity_codes = 10
suz_order_ceh_1 = "http://app.okto.ru/companies/a3e5ac4e-c6c3-4d80-9781-cdbc972297ba/oms_bussiness_orders"
suz_order_csm_archive = "http://app.okto.ru/companies/86ddc2a4-49a5-4330-98d4-b3928d0f50bd/oms_bussiness_orders"

options = webdriver.ChromeOptions()
options.add_extension("extension_1_2_13_0.crx")
options.add_argument(f"user-data-dir={os.environ['LOCALAPPDATA']}\\Google\\Chrome\\User Data\\1")
driver = webdriver.Chrome(options=options)

driver.get("http://app.okto.ru/users/sign_in")
time.sleep(2)
try:
    user_email = driver.find_element(by="id", value="user_email")
    user_password = driver.find_element(by="id", value="user_password")
    button_login = driver.find_element(by="id", value="sign_in_btn")
    user_email.send_keys("molvest.st@gmail.com")
    user_password.send_keys("Molvest22st07+")
    time.sleep(1)
    button_login.click()
    time.sleep(1)
    driver.get(suz_order_csm_archive + "/new")
    time.sleep(1)
    quantity = driver.find_element(by="id", value="quantity")
    quantity.clear()
    quantity.send_keys(quantity_codes)
    time.sleep(1)
    SKU = driver.find_element(By.ID, value="product_id")
    driver.execute_script("arguments[0].setAttribute('value', '92be7069-5ee8-4d85-a638-eee0fbb4d761')", SKU)
    button_send = driver.find_element(By.CSS_SELECTOR, value=".m-t-40px.btn.add_user")
    # button_send.click() // отправка заказа кодов
    time.sleep(1)
    driver.get(suz_order_csm_archive)
    report_status = driver.find_element(By.CLASS_NAME, value="report-status")
    time.sleep(1)
    if report_status.text == "Готов (в наличии активные буферы КМ)":
        order_id = driver.find_element(By.CLASS_NAME, value="order-id")
        order_id.click()
        time.sleep(5)
        check_gtin = driver.find_element(By.NAME, value="check_gtin")
        check_gtin.click()
        obtain_identification_codes = driver.find_element(By.ID, value="obtain_identification_codes")
        obtain_identification_codes.click()
        quantity = driver.find_element(By.ID, value="quantity")
        time.sleep(2)
        quantity.clear()
        quantity.send_keys(quantity_codes)
        time.sleep(1)
        submit_codes_form = driver.find_element(By.ID, value="submit_codes_form")
        submit_codes_form.click()
    else:
        print("NO")
    time.sleep(75)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()


