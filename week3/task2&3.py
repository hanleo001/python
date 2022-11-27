import math
def istriangle(a,b,c):
    res= a+b>c and a+c>b and b+c>a
    return res

def area_tri(a,b,c):
    p=0.5*(a+b+c)
    return (p*(p-a)*(p-b)*(p-c))**0.5

def angle_tri(a,b,c):
    cosA=(b*b+c*c-a*a)/(2*b*c)
    cosB=(a*a+c*c-b*b)/(2*a*c)
    cosC=(a**2+b**2-c**2)/(2*a*b)
    p=[]
    for co in [cosA,cosB,cosC]:
        A=math.acos(co)
        p+=[A]
    return p

def outR_tri(a,b,c):
    p=angle_tri(a,b,c)
    r=0.5*(a/(math.sin(p[0])))
    s=math.pi*r*r
    return [r,s]

def insR(a,b,c):
    p=a+b+c
    r=2*area_tri(a,b,c)/p
    s=math.pi*r*r
    return [r,s]

print("请输入三个正数")
a,b,c=float(input('A')),float(input('B')),float(input('C'))
if istriangle(a,b,c):
    print("这三个数构成三角形，记为三角形ABC")
    ang=angle_tri(a,b,c)
    oR=outR_tri(a,b,c)
    iR=insR(a,b,c)
    print("三角形ABC的角A,B,C分别为 {:.3f} {:.3f} {:.3f}".format(ang[0],ang[1],ang[2]))
    print("三角形ABC的外接圆半径为{:.3f}，外接圆面积为{:.3f}".format(oR[0],oR[1]))
    print("三角形ABC的内接圆半径为{:.3f}，内接圆面积为{:.3f}".format(iR[0],iR[1]))
else:
    print("不构成三角形")
input("按任意键结束") # 免得看不清结果