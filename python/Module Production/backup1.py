def BackUp():
    old_file=input('please enter the file name you want to backup:')
    file_list=old_file.split('.')
    new_file=file_list[0]+'_backUp'
    old_f=open(old_file,'r')
    new_f=open(new_file,'w')
    context=old_f.read()
    new_f.write(context)
    old_f.close()
    new_f.close()
    try:
        with open('old_f','r')as old_f , open('new_f','w')as new_f:
            while True:
                context=old_f.read(1024)
                new_f.write(context)
                if len(context)<1024:
                    break
                    pass
                pass
            pass
        pass
    except Exception as msg:
        print(msg)
        pass
    pass
BackUp()
