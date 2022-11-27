# Python 

## 数据类型

### 数字

#### 函数
##### 随机函数
random.choice(seq) :choose a element from a seq

randrange :

random():chose a number from 0 to 1 (not 1)

seed:

shuffle(list):将列表重新随机排序

uniform（x,y）：从【x，y】中随机生成一个实数

##### 三角函数

hypot(x,y):

degrees(x): 返回x 的角度值

radians(x):返回x的弧度值

### 字符串
#### f-string
f-string 以f 开头，后跟字符串，用{}包裹需要运行的表达式
{}内末尾加=可以拼接表达式与结果
如 *f”\*\*\*{\*\*}\*“* 

#### .format
在字符串中用{}占位 字符串外紧跟 *.format(\*\*\*)*
{}中可以加**：表达式** 进行格式的修改 如：*.8f* 表示保留小数点后八位
#### 内置函数

capitalize():

center(width,fillchar):返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。

count(str,beg=0,end=len(string))返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数

bytes.decode(encoding='Uft-8',errors='strict')

encode(encoding='Uft-8',errors='strict')

endwith(suffix,beg=0,end=len(string)):检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.

expandtabs(absize=8):把字符串 string 中的 tab 符号转为空格，tab 符号默认的空格数是 8 。

find(str,beg=0,end=len(string)):检测 str 是否包含在字符串中，如果指定范围 beg 和 end ，则检查是否包含在指定范围内，如果包含返回开始的索引值，否则返回-1

[index(str, beg=0, end=len(string))](https://www.runoob.com/python3/python3-string-index.html):跟find()方法一样，只不过如果str不在字符串中会报一个异常。

[join(seq)](https://www.runoob.com/python3/python3-string-join.html):以指定字符串作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串

[ljust(width[, fillchar])](https://www.runoob.com/python3/python3-string-ljust.html):返回一个原字符串左对齐,并使用 fillchar 填充至长度 width 的新字符串，fillchar 默认为空格。

[rjust(width,[, fillchar])](https://www.runoob.com/python3/python3-string-rjust.html)返回一个原字符串右对齐,并使用fillchar(默认空格）填充至长度 width 的新字符串

[replace(old, new \[, max])](https://www.runoob.com/python3/python3-string-replace.html)把 将字符串中的 old 替换成 new,如果 max 指定，则替换不超过 max 次。

[rfind(str, beg=0,end=len(string))](https://www.runoob.com/python3/python3-string-rfind.html)类似于 find()函数，不过是从右边开始查找.

[rindex( str, beg=0, end=len(string))](https://www.runoob.com/python3/python3-string-rindex.html)类似于 index()，不过是从右边开始.

[swapcase()](https://www.runoob.com/python3/python3-string-swapcase.html)将字符串中大写转换为小写，小写转换为大写

### 列表

list.append(obj)](https://www.runoob.com/python3/python3-att-list-append.html)

[list.count(obj)](https://www.runoob.com/python3/python3-att-list-count.html)

[list.extend(seq)](https://www.runoob.com/python3/python3-att-list-extend.html)

[list.index(obj)](https://www.runoob.com/python3/python3-att-list-index.html)

[list.insert(index, obj)](https://www.runoob.com/python3/python3-att-list-insert.html)

[list.pop([index=-1])](https://www.runoob.com/python3/python3-att-list-pop.html)

[list.remove(obj)](https://www.runoob.com/python3/python3-att-list-remove.html)

[list.reverse()](https://www.runoob.com/python3/python3-att-list-reverse.html)

[list.sort( key=None, reverse=False)](https://www.runoob.com/python3/python3-att-list-sort.html)

[list.clear()](https://www.runoob.com/python3/python3-att-list-clear.html)

[list.copy()](https://www.runoob.com/python3/python3-att-list-copy.html)

### 元组

tuple(iterable)

### 字典

len(dict）

str(dict)

[dict.clear()](https://www.runoob.com/python3/python3-att-dictionary-clear.html)

[dict.fromkeys()](https://www.runoob.com/python3/python3-att-dictionary-fromkeys.html)

[dict.get(key, default=None)](https://www.runoob.com/python3/python3-att-dictionary-get.html)

[key in dict](https://www.runoob.com/python3/python3-att-dictionary-in.html)

[dict.setdefault(key, default=None)](https://www.runoob.com/python3/python3-att-dictionary-setdefault.html)

[dict.update(dict2)](https://www.runoob.com/python3/python3-att-dictionary-update.html)

[pop(key[,default])](https://www.runoob.com/python3/python3-att-dictionary-pop.html)

[popitem()](https://www.runoob.com/python3/python3-att-dictionary-popitem.html)

### 集合

[difference()](https://www.runoob.com/python3/ref-set-difference.html) 将字符串中大写转换为小写，小写转换为大写

[difference_update()](https://www.runoob.com/python3/ref-set-difference_update.html) 将字符串中大写转换为小写，小写转换为大写

[discard()](https://www.runoob.com/python3/ref-set-discard.html) 删除集合中指定的元素

[intersection()](https://www.runoob.com/python3/ref-set-intersection.html) 

[intersection_update()](https://www.runoob.com/python3/ref-set-intersection_update.html)

[isdisjoint()](https://www.runoob.com/python3/ref-set-isdisjoint.html) 判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False。

[issubset()](https://www.runoob.com/python3/ref-set-issubset.html)

[issuperset()](https://www.runoob.com/python3/ref-set-issuperset.html)

[pop()](https://www.runoob.com/python3/ref-set-pop.html) 随机移除元素

[remove()](https://www.runoob.com/python3/ref-set-remove.html)

[symmetric_difference()](https://www.runoob.com/python3/ref-set-symmetric_difference.html)

[symmetric_difference_update()](https://www.runoob.com/python3/ref-set-symmetric_difference_update.html)

[union()](https://www.runoob.com/python3/ref-set-union.html)

[update()](https://www.runoob.com/python3/ref-set-update.html) 





















































