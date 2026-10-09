# CraftLens

**先查清兼容性，再升级。** CraftLens 是一个中文优先、支持中英文切换的 Minecraft Java 版兼容性参考站，面向玩家、模组整合包维护者和服务器管理员。

CraftLens 整理 Minecraft 版本、Java 运行环境、服务端软件和模组加载器的基础说明，并为每条参考资料提供上游来源链接。它不是完整的模组兼容性数据库，也不会把未经验证的推测包装成结论。

## 在线体验

**网站：** https://wuyixiao123.github.io/craftlens/  
**源代码与问题反馈：** https://github.com/wuyixiao123/craftlens

## 当前功能

- 简体中文为默认语言，可切换到 English。
- 按关键词搜索 Minecraft 版本、Java、服务端软件和模组加载器。
- 按类别和证据状态筛选记录。
- 使用升级风险检查器比较 Modrinth 插件版本、游戏版本支持、加载器、依赖和更新日志。
- 定时通过 Modrinth 官方 API 更新热门与近期更新插件目录。
- 查看来源链接、核对日期和参考可信度。
- 响应式布局，适配手机与桌面浏览器。
- GitHub Actions 定期验证数据格式和来源链接字段结构。

## 升级风险检查器

打开 [`upgrade-check.html`](https://wuyixiao123.github.io/craftlens/upgrade-check.html)，搜索 Modrinth 上的插件并选择旧版本、新版本和目标 Minecraft 版本。检查器仅依据公开元数据提供风险提示；不能证明升级一定安全，也不会下载或执行插件。

热门插件目录由 `scripts/sync_modrinth_catalog.py` 从 Modrinth 官方 API 定时更新，自动任务见 `.github/workflows/sync-catalog.yml`。如果仓库的 GitHub Actions 未获准写入内容，请在仓库 Settings → Actions → General 中允许工作流读写仓库内容。

## 本地运行

需要 Python 3（仅用于启动本地静态服务器和运行验证脚本）：

```bash
git clone https://github.com/wuyixiao123/craftlens.git
cd craftlens
python -m http.server 8000
```

打开 http://localhost:8000。由于浏览器的本地文件安全限制，请不要直接通过 `file://` 打开页面。

验证数据结构：

```bash
python scripts/validate_data.py
```

## 数据原则

- 没有记录代表**未知**，不代表兼容。
- Java 版本匹配不等于模组、插件或服务端一定兼容。
- 每条事实性记录都应有 HTTPS 来源链接和核对日期。
- 自动化只检查结构，不生成或猜测兼容性结论。
- 在生产服务器升级前，请查阅上游发布说明并备份世界存档与配置。

## 参与贡献

欢迎提交问题、修正和 Pull Request。请尽可能提供准确的 Minecraft 版本、Java 版本、服务端或加载器版本、相关项目版本、复现步骤和上游证据。中文问题和贡献说明同样欢迎。

更多信息见 [CONTRIBUTING.md](CONTRIBUTING.md)、[SECURITY.md](SECURITY.md) 和 [LICENSE](LICENSE)。

## 计划

- [x] 响应式兼容性查询页面
- [x] 简体中文优先和中英文切换
- [x] 来源链接与明确的证据状态
- [x] 自动化数据结构验证
- [x] 插件版本升级风险检查器（基于公开元数据）
- [x] 定时同步热门与近期更新的插件目录
- [ ] 基于上游证据逐步扩充版本与加载器资料
- [ ] 增加服务器升级检查清单
- [ ] 增加安全、尊重隐私的崩溃日志辅助工具

## 许可

MIT。详见 [LICENSE](LICENSE)。
