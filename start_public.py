from pyngrok import ngrok
import time

# 開啟 ngrok 隧道
public_url = ngrok.connect(5000, bind_tls=True)

print("\n" + "="*60)
print("🎉 TOEIC 測驗已成功部署到公網！")
print("="*60)
print(f"\n📱 你的公開網址：")
print(f"\n   {public_url}")
print(f"\n")
print("✅ 現在可以在任何裝置上訪問這個網址進行測驗！")
print("✅ 手機、平板、電腦都可以使用")
print("✅ 530 個 TOEIC 單字題庫已載入")
print("\n⚠️  注意：當你關閉這個視窗，網址會失效")
print("="*60 + "\n")

# 保持運行
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\n正在關閉...")
    ngrok.disconnect(public_url)
