# re正则表达式:使用表达式对字符串进行匹配的语法规则

'''
^：以那个元字符开头
$：以那个元字符结尾

元字符（^ $的表达式，可以匹配固定的某些东西）
. 任意字符（除了下划线）
\w 数字、字母、下划线
\d：0-9的数字
\s 空白符
\n \t 换行、制表符

\W 非字母或下划线
\D 非数字
\S 非空白符
a|b 匹配字符a或b
() 括号内的表达式，也表示一个组
[...] 匹配字符组的字符  [a-zA-Z0-9]表示匹配数字字母
[^...] 除了字符组里面的所有字符
'''

print("校验你的电话号码")
phone = input("请输入你的电话号码：")