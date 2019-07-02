# def test(score_list):
#     count_youxiu,count_liang,count_cha = 0,0,0
#     for i in score_list:
#         if i>=90:
#             count_youxiu+=1
#         if 80<=i<90:
#             count_liang+=1
#         else:
#             count_cha+=1
#     if count_youxiu>=2:
#         print('优秀')
#     elif count_liang+count_youxiu>=2:
#         print('合格')
#     else:
#         print('不合格')
# test([90,89,0])

import re
re = re.compile(r'^1[3-9][0-9]{9}$')
print(re.match('13121212112'))
