# 通用版发布流程

在本仓库根目录维护 `skills/lowoo-job-search/` 和 README。每次改动完成后，按以下流程提交并推送到 `origin/main`。 [GitHub 仓库](https://github.com/Kylan3320/job-search-skill)

## 1. 核对仓库与分支

```sh
git rev-parse --show-toplevel
git status --short --branch
git remote get-url origin
git fetch origin
git log --oneline --left-right HEAD...origin/main
```

确认当前位于通用版仓库的 `main` 分支，远端是 `Kylan3320/job-search-skill`。如果远端有新提交，在保留本地改动的前提下先同步，再验证合并后的结果。

## 2. 验证并检查暂存内容

改动技能时，核对 `SKILL.md` 的 `name`、目录名、默认提示和 README 调用名。改动说明或图片时，检查相关链接和图片。用 `git add --` 逐项指定本次改动的文件，再查看暂存清单与差异。

```sh
git diff --cached --name-status
git diff --cached
git -c core.whitespace=cr-at-eol diff --cached --check
```

这个仓库是公开的。`profile/`、个人简历、求职记录、招聘平台截图和凭据都留在本地。以暂存清单为准，确认没有带入这些资料或其他任务的改动。

## 3. 提交、推送并核对结果

用 `git commit -m` 提交，提交说明写明本次改动，再推送到 `main`。

```sh
git push origin main
git rev-parse HEAD
git ls-remote origin refs/heads/main
git status --short --branch
```

确认本地提交和 GitHub 上 `main` 的提交一致。若推送因远端更新被拒绝，先拉取并整合远端提交，复核改动后再正常推送。
