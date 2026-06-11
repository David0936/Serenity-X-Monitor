# 参与贡献 Contributing

感谢参与 Serenity X Monitor！本文档说明如何提交代码与版本约定。

## 提交流程（贡献者）

1. **Fork** 本仓库到你自己的账号。
2. `git clone` 你的 fork，新建分支：
   ```bash
   git checkout -b fix/简短描述      # 或 feat/简短描述
   ```
3. 改代码、本地跑通：
   ```bash
   pip install -r requirements.txt
   python3 start.py          # 默认 http://localhost:5001
   ```
4. 提交并 push 到你的 fork，然后在 GitHub 上发起 **Pull Request** 指向本仓库的 `main`。
5. PR 描述里写清楚：**改了什么 / 为什么 / 怎么测的 / 建议算 patch 还是 minor**。

## ⚠️ 版本号请勿自行修改

- **不要**在 PR 里改 `app.py` 的 `VERSION`，**也不要**自己发 GitHub Release。
- 版本号与发版由维护者统一处理（避免多个 PR 同时改 `VERSION` 造成冲突）。
- 你只需在 PR 描述里**建议**版本位即可。

## 版本约定（语义化 `主.次.修订`）

| 改动类型 | 升哪位 | 例 |
|---|---|---|
| 修 bug、小调整 | 修订 patch | 1.1.0 → 1.1.1 |
| 新功能、向后兼容 | 次 minor | 1.1.0 → 1.2.0 |
| 不兼容改动（老 `config.json` 用不了） | 主 major | 1.x → 2.0.0 |

## 维护者发版流程

1. Review 并 Merge PR 到 `main`。
2. 改 `app.py` 顶部 `VERSION` + 在 `CHANGELOG.md` 顶部加一段 `## vX.Y.Z — 日期`（可标注 `感谢 @贡献者`）。
3. 推送并发布 Release：
   ```bash
   git push origin main
   git tag -a vX.Y.Z -m vX.Y.Z && git push origin vX.Y.Z
   gh release create vX.Y.Z --title vX.Y.Z --notes-file CHANGELOG.md
   ```
4. 老用户在应用「设置」页会自动检测到新版，点「一键更新」即可同步（`config.json` / `data/` 不受影响）。

## 代码风格

- 保持与现有代码一致：中文注释、简洁直接。
- 不要把密钥、`config.json`、`data/` 提交进仓库（已在 `.gitignore`）。
- 用户配置一律走 `config.json`，不要硬编码到源码（一键更新用 `git reset --hard`，手改源码会被覆盖）。
