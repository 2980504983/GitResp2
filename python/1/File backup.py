# import time as mytime
# from time import ctime
# from time import *
# import os
# import shutil

# print(ctime())


# #File backup
# def copyFile():
#     # Receive file name user input
#     old_file=input('Please enter file name you want to backup:')
#     file_list=old_file.split('.')
#     # Structrue new file name and add backup suffix '.'
#     new_file=file_list[0]+"_backup"+file_list[1]
#     # old_f=open(old_file,'r') # Open file to be backed up
#     # new_f=open(new_file,'w') # Open a new file for writing, create it if it doesn’t exist
#     # content=old_f.read() # read file content
#     # new_f.write(content) # Write the read content to the backup file
#     # old_f.close()
#     # new_f.close()
#     try:
#         with open(old_file,'r') as old_file,open(new_file,'w')as new_f:
#             while True:
#                 context=old_file.read(1024) #
#                 new_f.write(context)
#                 if len(context)<1024:
#                     break
#             pass
#     except Exception as msg:
#         print(msg)
#         pass
#
#
#     pass
#
# copyFile()




# a=open('Test.txt','rb')

# b=a.read(3)
# print(b)
# c=a.tell()
# print(c)

# print(a.read(2))
# a.seek(-2,2)
# print(a.tell())
# print(a.read(2))


# # a=open('filea.txt','w')
# os.remove('filea.txt')
# # a.close()



# os.mkdir('E:/asas')
# os.rmdir('E:/asas')
# os.makedirs('E:/asas/asasas/asasasasas')
# shutil.rmtree('E:/asas/asasas/asasasasas')
# print(os.getcwd())
# listA=os.listdir('E:/')
# for item in listA:
#     print(item)
