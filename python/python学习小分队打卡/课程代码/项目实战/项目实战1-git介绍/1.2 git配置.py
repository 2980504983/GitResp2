"""
    git分区:
        工作区，暂存区，本地仓库，远程仓库
        工作区的内容应该及时备份到本地仓库

    初始配置:
        git config --system 系统中所有用户的配置
        git config --global 一个用户所有项目的配置
            git config --global user.name "要填入的用户名"
            git config --global user.email "要填入的邮箱"
        git config  一个项目的配置

        git init 初始化git仓库

    git常用命令:
        git status 查看当前状态
        git add 文件名.格式  将工作区内容提交到暂存区(git add ./* 提交所有文件，*不能提交隐藏文件)
        git commit 文件名.格式

        # 可以创建一个.gitignore文件，在文件中写入你要忽略的文件，即如果项目中有一些，与你项目无关
        的文件，例如ide自动生成的.idea文件，就可以将文件名写入.gitignore文件中，表示忽略给文件

        git rm --cached 文件名.格式 将文件从暂存区撤回工作区
        git commit file -m '提交日志'  如果不写file表示将暂存区内容去全部提交到本地库

        git log 查看提交日志
        git diff 文件名.格式 将被修改的文件与本地库进行对比

        git checkout -- 文件名.格式  将本地库文件恢复到工作区

        git mv file path 移动文件，会同步到暂存区
        git rm files 删除文件，会同步到暂存区

    版本控制:
        git reset --hard HEAD^ 向前回滚一个版本
        git reset --hard 版本编码前七位(commit_id)  回滚到哪个版本
        git reflog  查询所有操作记录
        git tag tag_name commit_id -m message  打标签，类似于快照，在重要节点打标签，通过标签就可以快速回滚
        git show tag_name 查看标签详细信息
        git tag 查看所有标签
        git tag -d tag_name  删除标签
        git reset --hard [tag]  去往某个标签


"""