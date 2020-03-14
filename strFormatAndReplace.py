"""
3.2 Стандартные методы и функции для строк

#1
Вашей программе на вход подаются три строки s, a, b, состоящие из строчных латинских букв.
За одну операцию вы можете заменить все вхождения строки a в строку s на строку b.
Например, s = "abab", a = "ab", b = "ba", тогда после выполнения одной операции строка s перейдет в строку "baba", после выполнения двух и операций – в строку "bbaa", и дальнейшие операции не будут изменять строку s.
Необходимо узнать, после какого минимального количества операций в строке s не останется вхождений строки a. Если операций потребуется более 1000, выведите Impossible.
Выведите одно число – минимальное число операций, после применения которых в строке s не останется вхождений строки a, или Impossible, если операций потребуется более 1000.
Условие задачи было изменено 12.09.2018

Sample Input 1:
ababa
a
b
Sample Output 1:
1

Sample Input 2:
ababa
b
a

Sample Output 2:
1

Sample Input 3:
ababa
c
c
Sample Output 3:
0

Sample Input 4:
ababac
c
c
Sample Output 4:
Impossible
"""

#1
s, a, b= [input() for i in range(3)]
i=0
Impossible=1000

while True:
    if(i>Impossible):
        print('Impossible')
        break
    if (s.count(a)):
        s=s.replace(a,b)
        i +=1
        #print(s)
    else:
        print(i)
        break


"""
Вашей программе на вход подаются две строки s и t, состоящие из строчных латинских букв.
Выведите одно число – количество вхождений строки t в строку s.

Пример:
s = "abababa"
t = "aba"

Вхождения строки t в строку s:
abababa
abababa
abababa

Sample Input 1:
abababa
aba

Sample Output 1:
3

Sample Input 2:
abababa
abc

Sample Output 2:
0

Sample Input 3:
abc
abc

Sample Output 3:
1

Sample Input 4:
aaaaa
a

Sample Output 4:
5
"""

#
s = input()
t = input()

i=0
st=0

while True:
    if (t in s[st::]):
        st=s.find(t, st)
        i+=1
        st+=1
    else:
        break

print(i)

'''
s = input()
t = input()
ans = 0
for i in range(len(s)):
    if s[i:].startswith(t):
        ans += 1
print(ans)


s = input()
t = input()
print(sum(1 for i in range(len(s)) if s.startswith(t, i)))
'''