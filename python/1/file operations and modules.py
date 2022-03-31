# File operation
# Open file
# Default encoding is gbk , it's chinese encoding.
# It is better to specify the encoding type when opening the file.
# fobj=open('./Test.txt','w',encoding='utf-8')

# Start operation
#fobj.write('On the vast sea')
# fobj.write('Stormy winds enveloping the dark clouds')
# fobj.close()  # Store and close

# Write data in binary form
# fobj=open('Test.txt1','wb') #str-->bytes
# fobj.write('Between the dark and sea'.encode('utf-8'))
# fobj.close()

# open mode 'a'
# fobj=open('Test.txt','a') # append
# fobj.write('\nBetween the dark and sea\n')
# fobj.write('Petrel like black lightning\n')
# fobj.close()

# open mode 'ab'
# fobj=open('Test.txt','a') # append and it's binary.
# fobj.write('\nBetween the dark and sea\n')
# fobj.write('Petrel like black lightning\n')
# fobj.close()


# # Read operation
# f=open('Test.txt','r')
# # print(f.read(12))
# # print(f.read())
# print(f.readline())
# print(f.readlines())

# f=open('Test.txt','rb')
# # print(f.read(12))
# data=f.read()
# print(data.decode('gbk'))
# #print(f.readline())
# #print(f.readlines())
# f.close()

with open('Test.txt','r') as f :
    print(f.read())


