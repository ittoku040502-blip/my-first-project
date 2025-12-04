import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options # ←追加：オプション設定用の道具
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# --- 設定 ---
def setup_driver():
    # Chromeの起動オプションを作る
    options = Options()
    # 以下の3つは、起動エラーを防ぐための「強力なおまじない」です
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu') 
    # options.add_argument('--headless') # ←これを有効にすると画面が出ずに裏で動きます

    # ドライバの準備
    service = Service(ChromeDriverManager().install())
    
    # オプション付きでChromeを起動
    return webdriver.Chrome(service=service, options=options)

def main():
    driver = None
    try:
        print("🤖 ブラウザを起動します...")
        driver = setup_driver() # 関数を呼び出して起動
        
        # 1. Yahoo! JAPANにアクセス
        driver.get("https://www.yahoo.co.jp")
        time.sleep(2)

        # 2. 検索窓を見つける
        search_box = driver.find_element(By.NAME, "p")
        
        # 3. キーワードを入力して検索実行
        keyword = "Python スクレイピング" # ←ここを変えると検索ワードが変わる（クイズの答え！）
        print(f"⌨️ 「{keyword}」と入力します...")
        
        search_box.send_keys(keyword)
        time.sleep(1)
        search_box.send_keys(Keys.RETURN)
        
        time.sleep(3)

        # 4. 検索結果のタイトルを取得
        print("👀 結果を読み取っています...")
        titles = driver.find_elements(By.TAG_NAME, "h3")

        print("-" * 30)
        for i, title in enumerate(titles[:5], 1):
            print(f"{i}. {title.text}")
        print("-" * 30)
        
    except Exception as e:
        print(f"エラーが発生しました: {e}")
        
    finally:
        if driver: # driverが無事に起動していたら閉じる
            print("👋 10秒後にブラウザを閉じます")
            time.sleep(10)
            driver.quit()

if __name__ == "__main__":
    main()