
str1=r'''
        (()__(()
        /       \
       ( /    \  \
        \ o o    /
        (_()_)__/ \
       / _,==.____ \   
      (   |--|      )
      /\_.|__|'-.__/\_
     / (        /     \
     \  \      (      /
      )  '._____)    /
   (((____.--(((____/
'''
print(str1)
str2=r'''

    .....       ..............     ................     ..            ..        
  ..     ..            ..                 ..            ..            ..                  
 .                     ..                 ..            ..            ..                 
   .                   ..                 ..            ..            ..                
     .                 ..                 ..            ..            ..                  
       .               ..                 ..            ..            ..                     
         .             ..                 ..            ..            ..                  
  ..     ..    ..      ..                 ..             ..          ..                          
    .....         .....                   ..              ............                                    
        

'''
print(str2)
str3='''
*       
    *   
 *      
     *  
  *     
      * 
       *
     '''
print(str3)
print('''
                          忆江南
                   作者：白居易 年代：唐
江南好，风景旧曾谙。日出江花红胜火，春来江水绿如蓝。能不忆江南？ 　　
江南忆，最忆是杭州。山寺月中寻桂子，郡亭枕上看潮头。何日更重游？ 　　
江南忆，其次忆吴宫。吴酒一杯春竹叶，吴娃双舞醉芙蓉。早晚复相逢？
'''
)
a=3
b=4
c=3
p=0.5*(a+b+c)
import math
s=(math.sqrt(p*(p-a)*(p-b)*(p-c)))
print(s)
def root2(a,b,c):
    return [(-b+math.sqrt(b**2-4*a*c))/2*a,(-b-math.sqrt(b**2-4*a*c))/2*a]
rootssss=root2(1,2,-1)
print(rootssss[0],rootssss[1])