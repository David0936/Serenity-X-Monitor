#!/usr/bin/env bash
# 构建 Mac 桌面版 .app（在 Mac 上运行；产物在 dist/Claworld Monitor.app）
# 用法：bash build-mac.sh
set -e
cd "$(dirname "$0")"

# 建议在虚拟环境里执行
python3 -m pip install -q -r requirements.txt -r requirements-desktop.txt

rm -rf build dist "Claworld Monitor.spec"

pyinstaller --noconfirm --windowed \
  --name "Claworld Monitor" \
  --osx-bundle-identifier com.claworld.monitor \
  --add-data "templates:templates" \
  --add-data "static:static" \
  --add-data "data/ashares.json:data" \
  --collect-all webview \
  --collect-all openai \
  desktop.py

echo
echo "✅ 完成：dist/Claworld Monitor.app"
echo "   首次打开若提示「身份不明开发者」：右键 App → 打开 → 再点打开。"
