#!/bin/bash
# 安裝 Gemini News Bot Service 和 Timer

echo "📦 正在安裝 Gemini News Bot Service..."

# 複製 service 和 timer 檔案到 systemd 目錄
sudo cp gemini-news-bot.service /etc/systemd/system/
sudo cp gemini-news-bot.timer /etc/systemd/system/

# 重新載入 systemd 配置
echo "🔄 重新載入 systemd 配置..."
sudo systemctl daemon-reload

# 啟用並啟動 timer
echo "▶️  啟用並啟動 timer..."
sudo systemctl enable gemini-news-bot.timer
sudo systemctl start gemini-news-bot.timer

# 顯示狀態
echo ""
echo "✅ 安裝完成！"
echo ""
echo "📊 Timer 狀態："
sudo systemctl status gemini-news-bot.timer --no-pager

echo ""
echo "📋 查看執行時間表："
sudo systemctl list-timers gemini-news-bot.timer --no-pager

echo ""
echo "💡 提示："
echo "   - 查看即時日誌: sudo journalctl -u gemini-news-bot.service -f"
echo "   - 查看最近日誌: sudo journalctl -u gemini-news-bot.service -n 50"
echo "   - 停止服務: sudo systemctl stop gemini-news-bot.timer"
