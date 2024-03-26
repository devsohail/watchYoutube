import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.common.exceptions import TimeoutException

# Function to generate a random duration to watch the video
def random_duration():
    return random.randint(50, 300)  # Adjust this range according to your preference time in seconds

# Function to change IP address using a proxy
def change_proxy(driver):
    # Random IP address will be used
    ip_addresses = [
        '158.178.241.45', '34.93.79.152', '35.185.196.38', '34.93.62.7', '47.74.12.139', '47.74.22.171', 
        '47.74.11.251', '47.74.5.150', '47.74.13.66', '47.74.5.233', '8.219.78.1', '47.91.14.62', '47.91.15.247', 
        '47.74.15.120', '69.25.155.173', '8.219.84.102', '8.219.174.142', '8.219.60.68', '8.222.221.109', 
        '8.219.157.97', '8.219.193.202', '8.219.106.15', '8.222.254.91', '8.222.198.105', '8.219.121.24', 
        '8.219.40.255', '8.222.167.147', '8.219.201.174', '8.219.247.203', '8.219.178.101', '8.222.221.90', 
        '8.219.101.138', '8.219.175.127', '8.219.159.232', '8.219.42.72', '8.219.50.180', '8.219.141.174', 
        '8.222.224.162', '8.219.102.252', '8.219.198.139', '8.219.201.245', '8.219.58.64', '8.219.60.54', 
        '8.222.253.235', '8.219.137.50', '8.219.100.155', '8.219.201.8', '8.219.61.52', '8.219.72.50', 
        '8.219.84.214', '8.219.114.201', '8.222.255.15', '8.222.224.17', '8.222.214.231', '8.222.221.86', 
        '8.222.209.223', '8.222.138.164', '8.219.122.55', '8.219.121.87', '8.219.228.157', '8.219.210.64', 
        '8.219.170.223', '8.219.195.47', '8.219.67.133'
    ]
    proxy_ip = random.choice(ip_addresses)
    proxy_port = '80'

    # Setup proxy
    proxy = Proxy()
    proxy.proxy_type = ProxyType.MANUAL
    proxy.http_proxy = f"{proxy_ip}:{proxy_port}"
    proxy.ssl_proxy = f"{proxy_ip}:{proxy_port}"

    # Restart the browser with new proxy
    capabilities = webdriver.DesiredCapabilities.CHROME.copy()
    capabilities['proxy'] = {
        "httpProxy": proxy_ip + ":" + proxy_port,
        "ftpProxy": proxy_ip + ":" + proxy_port,
        "sslProxy": proxy_ip + ":" + proxy_port,
        "proxyType": "MANUAL"
    }

    driver.quit()
    driver = webdriver.Chrome(desired_capabilities=capabilities)
    return driver

# Main function
def main():
    # Selenium setup
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()

    # YouTube link to watch
    video_link = "https://www.youtube.com/watch?v=Youtube_vidoe_Id"

    while True:
        # Load YouTube video
        driver.get(video_link)
        print("Watching video...")

        # Wait for the video to load
        try:
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.TAG_NAME, "video")))
        except TimeoutException:
            print("Timeout while waiting for video to load")
            continue

        # Watch video for a random duration
        duration = random_duration()
        print(f"Watching for {duration} seconds...")
        time.sleep(duration)

        # Change IP address by changing proxy
        driver = change_proxy(driver)

if __name__ == "__main__":
    main()
