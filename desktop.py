#!/usr/bin/env python3
"""Mac 桌面版启动器：后台线程跑 Flask，前台开原生窗口。双击 .app 即用，关窗即退出。"""
import os
import socket
import threading
import time

os.environ["CLAWORLD_DESKTOP"] = "1"   # 必须在 import app 之前：开启桌面模式（免登录）

import webview  # noqa: E402

from app import app  # noqa: E402

PORT = 5001


def _wait_ready(port, timeout=15):
    end = time.time() + timeout
    while time.time() < end:
        try:
            with socket.create_connection(("127.0.0.1", port), 0.3):
                return True
        except OSError:
            time.sleep(0.2)
    return False


def _run_server():
    app.run(host="127.0.0.1", port=PORT, debug=False, use_reloader=False)


def main():
    threading.Thread(target=_run_server, daemon=True).start()
    _wait_ready(PORT)
    webview.create_window(
        "Claworld Monitor · 财经监控",
        f"http://127.0.0.1:{PORT}/",
        width=1240, height=840, min_size=(900, 600),
    )
    webview.start()   # 阻塞主线程；关窗后返回 → 进程退出，daemon 服务线程随之结束


if __name__ == "__main__":
    main()
