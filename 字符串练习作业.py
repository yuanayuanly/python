'''定义一个列表，包含自己的家庭成员名字， 定义完成后在你名字前加入"鲸鱼"，
再 将"鲸鱼"这一名字删除，此时判断" 鲸鱼"是否在列表中。'''
familyname=['father','mother','son','sister']
familyname.insert(2,'yuan')
print(familyname)
#familyname.remove('son')
familyname.pop(3)
print(familyname)
print('son'in familyname)

