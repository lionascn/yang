
height_n=100
bounce_n=height_n/2

for n  in range(1,10):#循环十次
      height_n+=bounce_n*2 #For循环的执行语句要缩两格
      bounce_n/=2

print("小球落下第十次落地总路径长度为%f米" % height_n)
print("小球落下的第十次反弹有%f米"% bounce_n)



print('The quick brown fox', 'jumps over', 'the lazy dog')
print(300)
print(100 + 200)
print('100 + 200 =', 100 + 200)