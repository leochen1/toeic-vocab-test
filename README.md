# TOEIC 單字測驗系統

這是一個基於 Flask 的 TOEIC 單字測驗網頁應用程式。

## 功能特色

1. **自動讀取 PDF 單字庫**：從 `docs` 資料夾中的 10 個 TOEIC 主題 PDF 檔案讀取單字
2. **隨機出題**：每次測驗隨機抽取 10 個單字
3. **語音發音**：點擊發音按鈕可聽取單字發音（使用瀏覽器內建 TTS）
4. **選擇題測驗**：每題提供 4 個選項
5. **即時評分**：提交後立即顯示分數和詳細解析
6. **錯題解釋**：答錯的題目會顯示正確答案和例句
7. **重新測驗**：可隨時刷新並生成新的測驗題目

## 安裝步驟

1. 確保已安裝 Python 3.8 或以上版本

2. 安裝所需套件：
```bash
pip install -r requirements.txt
```

## 使用方法

1. 確保 `docs` 資料夾中有 TOEIC 單字的 PDF 檔案

2. 執行應用程式：
```bash
python main.py
```

3. 開啟瀏覽器並訪問：
```
http://localhost:5000
```

4. 開始測驗！

## 專案結構

```
PyToeicTest/
├── main.py                 # Flask 後端主程式
├── templates/
│   └── index.html         # 前端網頁
├── docs/                  # PDF 單字檔案資料夾
│   ├── 1 一般商務General Business_v1.pdf
│   ├── 2 辦公庶務 Office Issues_v1.pdf
│   ├── ...
│   └── 10 健康 Health_v1.pdf
├── requirements.txt       # Python 套件清單
└── README.md             # 說明文件
```

## 注意事項

- PDF 檔案中的單字格式應為：`單字 - 中文翻譯` 或 `單字：中文翻譯`
- 發音功能需要瀏覽器支援 Web Speech API（Chrome、Edge 等現代瀏覽器皆支援）
- 首次載入時會自動解析所有 PDF 檔案，可能需要幾秒鐘時間

## 技術棧

- **後端**：Flask (Python)
- **前端**：HTML5、CSS3、JavaScript
- **PDF 處理**：PyPDF2
- **語音**：Web Speech API

## 未來改進方向

- 加入使用者帳號系統
- 儲存測驗歷史記錄
- 提供更多樣化的例句
- 加入單字卡學習模式
- 支援更多題型（填空、聽力等）
