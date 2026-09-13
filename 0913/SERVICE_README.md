# Gemini News Bot 系統服務說明

## 📁 建立的檔案清單

### 系統服務檔案
1. **gemini-news-bot.service** - systemd 服務單元檔案
2. **gemini-news-bot.timer** - systemd 計時器檔案 (每 1 分鐘執行一次)

### 管理腳本
3. **install-service.sh** - 安裝服務腳本
4. **uninstall-service.sh** - 移除服務腳本
5. **check-service.sh** - 檢查服務狀態腳本
6. **SERVICE_README.md** - 本說明檔案

### 主程式
- **practice4.py** - Gemini 聯網搜尋 + Telegram 推播程式

---

## 🚀 安裝與啟動服務

### 步驟 1: 進入目錄
```bash
cd /home/pi/Documents/github/2026_07_26__chihlee_gemini_sunday/0913
```

### 步驟 2: 執行安裝腳本
```bash
./install-service.sh
```

安裝腳本會自動完成:
- ✅ 複製服務檔案到 `/etc/systemd/system/`
- ✅ 重新載入 systemd 配置
- ✅ 啟用並啟動 timer
- ✅ 顯示服務狀態

---

## 🔍 檢查服務狀態

### 使用檢查腳本 (推薦)
```bash
./check-service.sh
```

### 手動檢查指令
```bash
# 查看 timer 狀態
sudo systemctl status gemini-news-bot.timer

# 查看下次執行時間
sudo systemctl list-timers gemini-news-bot.timer

# 查看 service 狀態
sudo systemctl status gemini-news-bot.service

# 即時監控執行日誌
sudo journalctl -u gemini-news-bot.service -f

# 查看最近 50 筆日誌
sudo journalctl -u gemini-news-bot.service -n 50
```

---

## ⏯️ 服務控制指令

### 停止服務
```bash
sudo systemctl stop gemini-news-bot.timer
```

### 啟動服務
```bash
sudo systemctl start gemini-news-bot.timer
```

### 重新啟動服務
```bash
sudo systemctl restart gemini-news-bot.timer
```

### 手動執行一次 (不等待 timer)
```bash
sudo systemctl start gemini-news-bot.service
```

---

## 🗑️ 完全移除服務

### 使用移除腳本 (推薦)
```bash
./uninstall-service.sh
```

移除腳本會自動完成:
- ✅ 停止並停用 timer
- ✅ 停止 service
- ✅ 刪除系統檔案
- ✅ 重新載入 systemd 配置
- ✅ 清理所有相關設定

### 驗證移除成功
```bash
sudo systemctl list-unit-files | grep gemini-news-bot
```
如果沒有任何輸出,表示移除成功。

---

## ⚙️ 服務配置說明

### Timer 設定 (gemini-news-bot.timer)
- **OnBootSec=30sec** - 系統開機後 30 秒首次執行
- **OnUnitActiveSec=1min** - 每次執行完畢後 1 分鐘再次執行
- **Persistent=true** - 如果錯過執行時間(如關機),開機後會補執行

### Service 設定 (gemini-news-bot.service)
- **Type=oneshot** - 單次執行型服務
- **User=pi** - 以 pi 使用者身分執行
- **WorkingDirectory** - 設定工作目錄為專案根目錄
- **Environment** - 設定 Python 虛擬環境路徑

---

## 🔧 修改執行頻率

如果要修改執行頻率,編輯 `gemini-news-bot.timer` 檔案:

```bash
nano gemini-news-bot.timer
```

修改這一行:
```ini
OnUnitActiveSec=1min   # 改為其他時間,如: 5min, 10min, 1h
```

修改後重新安裝:
```bash
./install-service.sh
```

### 常用時間單位
- `30sec` = 30 秒
- `1min` = 1 分鐘
- `5min` = 5 分鐘
- `1h` = 1 小時
- `1d` = 1 天

---

## 📊 日誌查看技巧

### 查看今天的所有執行記錄
```bash
sudo journalctl -u gemini-news-bot.service --since today
```

### 查看最近 1 小時的記錄
```bash
sudo journalctl -u gemini-news-bot.service --since "1 hour ago"
```

### 即時追蹤日誌 (類似 tail -f)
```bash
sudo journalctl -u gemini-news-bot.service -f
```

### 只看錯誤訊息
```bash
sudo journalctl -u gemini-news-bot.service -p err
```

---

## ⚠️ 注意事項

1. **測試期間**: 目前設定為每 1 分鐘執行一次,僅供測試用
2. **API 限制**: 請注意 Gemini API 和 Telegram Bot 的呼叫頻率限制
3. **網路需求**: 服務需要網路連線才能正常運作
4. **環境變數**: 確保 `.env` 檔案包含正確的 API 金鑰
5. **權限問題**: 如果遇到權限錯誤,檢查 Python 虛擬環境路徑是否正確

---

## 🐛 故障排除

### 問題 1: 服務無法啟動
```bash
# 檢查服務日誌找出錯誤原因
sudo journalctl -u gemini-news-bot.service -n 50
```

### 問題 2: Python 找不到模組
確認虛擬環境已安裝所需套件:
```bash
cd /home/pi/Documents/github/2026_07_26__chihlee_gemini_sunday
source .venv/bin/activate
pip install python-telegram-bot google-genai python-dotenv
```

### 問題 3: 權限錯誤
確保檔案所有權正確:
```bash
sudo chown -R pi:pi /home/pi/Documents/github/2026_07_26__chihlee_gemini_sunday
```

---

## 📞 快速參考

| 操作 | 指令 |
|------|------|
| 安裝服務 | `./install-service.sh` |
| 移除服務 | `./uninstall-service.sh` |
| 檢查狀態 | `./check-service.sh` |
| 停止服務 | `sudo systemctl stop gemini-news-bot.timer` |
| 啟動服務 | `sudo systemctl start gemini-news-bot.timer` |
| 查看日誌 | `sudo journalctl -u gemini-news-bot.service -f` |
| 手動執行 | `sudo systemctl start gemini-news-bot.service` |
