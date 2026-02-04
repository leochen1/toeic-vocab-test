# 快速部署指南 - Render.com

## 🚀 最簡單的部署方式

### 第一步：建立 GitHub 帳號並上傳程式碼

1. **建立 GitHub 儲存庫**
   - 前往 https://github.com
   - 登入後點擊右上角 `+` → `New repository`
   - Repository name: `toeic-vocab-test`
   - 選擇 `Public`
   - 點擊 `Create repository`

2. **上傳程式碼**（在專案資料夾執行）：

```powershell
# 添加所有檔案
git add .

# 提交
git commit -m "TOEIC Vocab Test Application"

# 設定遠端儲存庫（替換 YOUR_USERNAME 為你的 GitHub 帳號名稱）
git remote add origin https://github.com/YOUR_USERNAME/toeic-vocab-test.git

# 推送到 GitHub
git branch -M main
git push -u origin main
```

### 第二步：部署到 Render

1. **註冊 Render**
   - 前往 https://render.com
   - 點擊 `Get Started` 或 `Sign Up`
   - 使用 GitHub 帳號登入（推薦）

2. **建立 Web Service**
   - 登入後點擊 `New +` → `Web Service`
   - 點擊 `Connect a repository`
   - 授權 Render 訪問你的 GitHub
   - 選擇 `toeic-vocab-test` 儲存庫
   - 點擊 `Connect`

3. **配置設定**（應該會自動偵測，如果沒有請手動輸入）：
   - **Name**: `toeic-vocab-test`
   - **Region**: Singapore（或其他靠近的區域）
   - **Branch**: `main`
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn main:app`

4. **選擇方案**
   - 選擇 `Free` 方案
   - 點擊 `Create Web Service`

5. **等待部署**
   - 等待 3-5 分鐘
   - 部署完成後會顯示你的網址：`https://toeic-vocab-test.onrender.com`

### 完成！🎉

現在你可以在任何裝置上訪問測驗：
- 📱 手機
- 💻 電腦
- 🖥️ 平板

網址格式：`https://你的服務名稱.onrender.com`

---

## 📝 注意事項

1. **首次訪問可能較慢**
   - 免費方案 15 分鐘無活動會休眠
   - 休眠後首次訪問需要 30-60 秒喚醒

2. **更新程式碼**
   ```powershell
   git add .
   git commit -m "更新說明"
   git push
   ```
   推送後 Render 會自動重新部署

3. **查看日誌**
   - 在 Render Dashboard 點擊你的服務
   - 點擊 `Logs` 查看運行狀態

---

## ❓ 常見問題

**Q: 為什麼首次訪問很慢？**
A: 免費方案會在無活動時休眠，首次訪問需要喚醒伺服器。

**Q: 可以使用自己的網域嗎？**
A: 可以，但需要升級到付費方案。

**Q: PDF 檔案會一起部署嗎？**
A: 是的，只要在 Git 中提交，所有檔案都會部署。

**Q: 如何刪除部署？**
A: 在 Render Dashboard 中選擇服務，點擊 Settings → Delete Service。

---

## 🔧 故障排除

如果部署失敗：
1. 檢查 Render 的 Logs
2. 確認 requirements.txt 正確
3. 確認 docs 資料夾存在
4. 檢查 Python 版本相容性

需要協助？查看完整說明：DEPLOYMENT.md
