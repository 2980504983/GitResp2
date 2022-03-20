"""
    保存工作区
        1 封存工作区:
            git stash save "注释信息"  封存工作区
            git stash list  查看被封存的工作区
            git stash apply stash@{0}  启用一个被封存的工作区
            git stash drop stash@{0}  删除一个被封存的工作区
            git stash clear  删除所有被封存的工作区

"""