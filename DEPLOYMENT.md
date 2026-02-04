# 🚀 部署到 Render.com 教學

## 方法一：使用 GitHub（推薦）

### 步驟 1：建立 GitHub 儲存庫

1. 前往 [GitHub](https://github.com) 並登入（沒有帳號請先註冊）
2. 點擊右上角的 `+` 號，選擇 `New repository`
3. 輸入儲存庫名稱（例如：`toeic-vocab-test`）
4. 選擇 `Public`（公開）
5. 點擊 `Create repository`

### 步驟 2：上傳程式碼到 GitHub

在專案資料夾中執行以下命令：

```bash
# 初始化 Git（如果還沒初始化）
git init

# 添加所有檔案
git add .

# 提交變更
git commit -m "Initial commit - TOEIC Vocab Test App"

# 連接到 GitHub 儲存庫（替換成你的帳號和儲存庫名稱）
git remote add origin https://github.com/YOUR_USERNAME/toeic-vocab-test.git

# 推送到 GitHub
git branch -M main
git push -u origin main
```

### 步驟 3：部署到 Render

1. 前往 [Render.com](https://render.com) 並註冊/登入
2. 點擊 `New +` 按鈕，選擇 `Web Service`
3. 選擇 `Connect a repository` 並授權 GitHub
4. 找到你的 `toeic-vocab-test` 儲存庫並點擊 `Connect`
5. 配置服務：
   - **Name**: `toeic-vocab-test`（或你喜歡的名稱）
   - **Region**: 選擇最近的區域（如 Singapore）
   - **Branch**: `main`
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn main:app`
6. 選擇 **Free** 方案
7. 點擊 `Create Web Service`

### 步驟 4：等待部署完成

- 部署需要 3-5 分鐘
- 完成後會得到一個網址，例如：`https://toeic-vocab-test.onrender.com`
- 你可以在任何裝置上訪問這個網址！

---

## 方法二：使用 PythonAnywhere（替代方案）

### 步驟 1：註冊 PythonAnywhere

1. 前往 [PythonAnywhere](https://www.pythonanywhere.com)
2. 點擊 `Start running Python online in less than a minute!`
3. 選擇免費的 `Beginner` 帳號並註冊

### 步驟 2：上傳程式碼

1. 登入後，點擊 `Files`
2. 點擊 `Upload a file` 上傳所有專案檔案
3. 或使用 `Bash console` 從 GitHub clone：
   ```bash
   git clone https://github.com/YOUR_USERNAME/toeic-vocab-test.git
   ```

### 步驟 3：設置 Web App

1. 點擊 `Web` 標籤
2. 點擊 `Add a new web app`
3. 選擇 `Manual configuration`
4. 選擇 `Python 3.10`
5. 配置 WSGI 文件：
   - 點擊 WSGI configuration file 連結
   - 刪除所有內容，貼上：
   ```python
   import sys
   path = '/home/YOUR_USERNAME/toeic-vocab-test'
   if path not in sys.path:
       sys.path.append(path)
   
   from main import app as application
   ```
6. 設置虛擬環境：
   ```bash
   cd ~/toeic-vocab-test
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
7. 在 Web 標籤中，設置 Virtualenv 路徑：
   `/home/YOUR_USERNAME/toeic-vocab-test/venv`

### 步驟 4：啟動應用

1. 點擊 `Reload` 按鈕
2. 你的應用會在 `https://YOUR_USERNAME.pythonanywhere.com` 運行

---

## ⚠️ 重要注意事項

### 1. PDF 檔案處理

由於 PDF 檔案較大，建議：
- 確保 `docs` 資料夾包含在部署中
- 如果 GitHub 有大小限制，可使用 Git LFS

### 2. 免費方案限制

**Render 免費方案：**
- 15 分鐘無活動後會自動休眠
- 首次訪問可能需要等待 30-60 秒喚醒
- 每月 750 小時免費運行時間

**PythonAnywhere 免費方案：**
- 只能訪問白名單上的外部網站
- 每 3 個月需要手動延長
- 儲存空間 512MB

### 3. 推薦配置

建議使用 **Render.com**，原因：
- ✅ 設置更簡單
- ✅ 自動 HTTPS
- ✅ 支援 Git 自動部署
- ✅ 更好的效能

---

## 🔄 更新部署

當你修改程式碼後：

**Render（使用 GitHub）：**
```bash
git add .
git commit -m "更新說明"
git push
```
Render 會自動重新部署！

**PythonAnywhere：**
1. 上傳新檔案或使用 `git pull`
2. 在 Web 標籤點擊 `Reload`

---

## 🎉 完成！

部署完成後，你可以：
- 📱 在手機上訪問
- 💻 在任何電腦上使用
- 🔗 分享網址給其他人

需要幫助？請參考：
- [Render 文檔](https://render.com/docs)
- [PythonAnywhere 教學](https://help.pythonanywhere.com)
