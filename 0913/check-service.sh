#!/bin/bash
# 檢查 Gemini News Bot Service 狀態

echo "📊 Gemini News Bot 服務狀態檢查"
echo "================================"
echo ""

echo "⏰ Timer 狀態："
sudo systemctl status gemini-news-bot.timer --no-pager
echo ""

echo "📋 下次執行時間："
sudo systemctl list-timers gemini-news-bot.timer --no-pager
echo ""

echo "🔍 Service 狀態："
sudo systemctl status gemini-news-bot.service --no-pager
echo ""

echo "📝 最近 20 筆執行記錄："
sudo journalctl -u gemini-news-bot.service -n 20 --no-pager
echo ""

echo "💡 常用指令："
echo "   - 即時監控日誌: sudo journalctl -u gemini-news-bot.service -f"
echo "   - 停止服務: sudo systemctl stop gemini-news-bot.timer"
echo "   - 啟動服務: sudo systemctl start gemini-news-bot.timer"
echo "   - 重新啟動: sudo systemctl restart gemini-news-bot.timer"
echo "   - 手動執行一次: sudo systemctl start gemini-news-bot.service"
