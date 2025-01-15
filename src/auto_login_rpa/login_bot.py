from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from .config import LoginConfig

class LoginBot:
    def __init__(self, config: LoginConfig):
        self.config = config
        self.driver = None

    def setup_driver(self):
        options = Options()
        options = webdriver.ChromeOptions()
        options.binary_location = "/home/dev/chrome-linux64/chrome"
        # options.add_argument("--headless")  # Uncomment this line to run headless
        options.add_argument("--no-sandbox")  
        options.add_argument("--disable-dev-shm-usage")  
        options.add_argument("--remote-debugging-port=9222") 
        options.add_argument("--start-maximized")

        # Path to chromedriver
        service = Service("/usr/bin/chromedriver")

        # Start driver
        self.driver = webdriver.Chrome(service=service, options=options)

    def login(self):
        try:
            self.driver.get(self.config.url)
            
            # Wait for username field and enter credentials
            username_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "username"))
            )
            username_field.send_keys(self.config.username)
            
            # Enter password
            password_field = self.driver.find_element(By.ID, "password")
            password_field.send_keys(self.config.password)
            
            # Click login button
            login_button = self.driver.find_element(By.ID, "login")
            login_button.click()
            
            return True
            
        except Exception as e:
            print(f"Login failed: {e}")
            return False
        
    def close(self):
        if self.driver:
            self.driver.quit()