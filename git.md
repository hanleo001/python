git add .  添加到暂存区

git commit -m . 提交

git status 查看状态

git reset --hard 版本号|HEAD^|HEAD^^|HEAD~100

git reflog

git checkout --file 放弃工作区的修改

rm file 删除

ssh-keygen -t rsa –C “youremail@example.com” 生成ssh密钥

git remote add origin https://github.com/tugenhua0707/testgit.git 添加远程库

git push -u origin branchname  push到远程库（-u 为关联）

git clone url 克隆远程库

git checkout -b branchname 生成分支

git branch 查看所有分支

git checkout branchname 切换分支

git merge name 合并某分支到当前分支

git stash 将工作区的修改隐藏

git stash list 列出stash 的工作区

git stash apply恢复，恢复后，stash内容并不删除，你需要使用命令git stash drop来删除。
git stash pop 恢复,同时把stash内容也删除了。

git checkout –b dev origin/dev 将远程库中的dev分支到本地的dev分支