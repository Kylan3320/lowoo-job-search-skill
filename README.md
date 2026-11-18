<h1 align="center">老吴？求职助手</h1>

<p align="center">
  <a href="skills/lowoo-job-search/SKILL.md"><img src="assets/readme/codex-skill.svg" alt="Codex Skill"></a>
</p>

<p align="center">
  <a href="#安装与初始化">安装与初始化</a> · <a href="#使用流程">使用流程</a> · <a href="#同步资料">同步资料</a>
</p>

<p align="center">
  <img src="assets/readme/hero.webp" width="100%" alt="求职助手封面，简历和岗位卡片旁叠着一张招呼语卡片">
</p>

`lowoo-job-search` 是一个 Codex 技能。把简历和 BOSS 直聘岗位截图发给 Codex，它会选出最贴合岗位的经历，写一条发给招聘方的招呼语。简历改版后，也可以用它更新招聘平台的附件或在线资料。

## 招呼语示例

假设岗位要求能梳理业务流程并交付原型，简历里有仓配工作台项目。招呼语可以先亮出交付，再说清原型解决了什么问题。

> 您好，做过仓配运营工作台，交付过 PRD 和交互原型。跟着调度员走了一遍交班流程，发现异常件的进度和负责人得分开查，就把两项信息放到了同一张工单上。希望有机会进一步沟通。

## 安装与初始化

1. **复制技能目录。** 下载本项目，把 `skills/lowoo-job-search/` 整个文件夹复制到用户主目录的 `.agents/skills/` 下。装好后，入口文件应位于 `~/.agents/skills/lowoo-job-search/SKILL.md`。仅在某个项目里使用时，可以把它放进该项目的 `.agents/skills/`。 [Codex 技能文档](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills)
2. **带一份简历和一个岗位试用。** 在 Codex 新对话中选择 `$lowoo-job-search`，附上当前简历和一个想投的 BOSS 岗位截图或文字描述，再发出下面这条请求。

   ```text
   用 $lowoo-job-search 写招呼语。
   ```

3. **拿到首稿。** Codex 会直接给出首稿，有岗位截图就附上原图。它也会把可复用的经历、求职条件和简历位置存入安装目录里的 `profile/求职画像.md`。缺少关键材料时，按提示补上即可。如果只想试写一条，可以在请求里加上「仅本次使用」，这次的材料就只用来拟稿。

更新技能时，保留安装目录里的 `profile/`。从本项目的旧版升级时，把原来的 `profile/` 复制到 `lowoo-job-search/` 下。招呼语同时涉及毕业届别和出勤承诺时，随附的标点检查脚本需要 Python 3。

## 使用流程

1. **发岗位。** 初始化后，发一张或多张岗位截图，请 Codex 按岗写招呼语。它会沿用已有画像，按每个岗位的要求重新选经历。
2. **审稿。** 可以按编号通过、改写或跳过，也可以直接贴回修改过的句子。适合复用的改稿会存入 `profile/招呼语正反例.md`，供下次参考。
3. **确认发送。** 需要代发时，指定简历图片，并按编号确认要发的岗位和文案。确认后，Codex 逐岗先发简历图片，再发招呼语，并检查会话里的发送结果。 [投递说明](skills/lowoo-job-search/modules/boss/delivery.md)

## 同步资料

把正式简历和要更新的范围交给 Codex。同步在线履历时，也可以附上对应语言的完整文案。

```text
用 $lowoo-job-search 更新领英简历附件。
用这份英文 PDF，只换附件。
```

支持 BOSS 直聘、猎聘、前程无忧、牛客和领英。Codex 会核对指定附件或字段，保存后从平台页面检查结果。 [资料同步说明](skills/lowoo-job-search/modules/sync/guide.md)

代发和同步都需要已登录的账号与可用的界面操作工具。BOSS 直聘和猎聘使用桌面 Computer Use，其余平台默认使用浏览器。
