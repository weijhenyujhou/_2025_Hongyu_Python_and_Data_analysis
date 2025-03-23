#Set 集合存取內的資料無順序(無法index)但可去掉重複 符號括號：'{}'
from time import process_time_ns

s1 = {1,2,3}
s2 =set()
l1 = ['台北市','台北市','桃園市','桃園市','新竹市','台中市','台中市','台南市','高雄市']

s3 = set(l1)
print(s3)
#Set 使用的方法
print(len(s3))
s3.add('基隆市')

print(s3)
# remove 沒有在set內資料會報錯誤
s3.remove('基隆市')
# discard 與remove差別是會不會上報錯誤
s3.discard('新竹')
print(s3)
s3.pop()
print(s3)
s3.update(['宜蘭'])
print(s3)


se1 = {1,2,3,4,5}
se2 = {4,5,6,7,8}
print(f"se1{se1},se2:{se2}")
#聯集
#union_result = se1.union(se2)
union_result = se1 | se2
print(f'se1聯集se2:{union_result}')
#交集
#intersection_result = se1.intersection(se2)
intersection_result = se1 & se2
print(f'se1交集se2:{intersection_result}')
#差集
#difference_result = se1.difference(se2)
difference_result =se1 - se2
print(f'se1差集se2{difference_result}')
#對稱差集列出不同的
#symmertic_different = se1.symmetric_difference(se2)
symm_result = se1 ^ se2
print(f'se1對稱差集se2:{symm_result}')

