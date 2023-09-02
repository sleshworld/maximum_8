import time
# num = 570000

# l = []
# for i in range(1, 10000001):
#     l.append(i)
# start = time.time()
# left = 0
# right = len(l)

# while left <= right:
#     mid = (left + right)//2
#     if l[mid] == num:
#         print(mid)
#         break
#     if l[mid] > num:
#         right = mid
#     if l[mid] < num:
#         left = mid
# end = time.time()
# print(end-start)

# start = time.time()
# for i in range(len(l)):
#     if l[i] == num:
#         print(i)
# end = time.time()
# print(end-start)


# Задание: создать функцию которая принимает на вход строку и выводит в терминал число повторений каждого символа
# Например: strcount("aabbccd") -> a 2 b 2 c 2 d 1
def strcount(s): # O(N^2)
    print(s)
    # цикл for по каждому символу в строке и записываем в переменную sym
    for sym in s:
        count = 0
        # проходимся по каждому символу в строке и записываем в переменную sub_sym
        for sub_sym in s:
            if sym == sub_sym:
                count += 1
        print(sym, count)

def strcount(s): # O(N*M) если число уникальных символов равно числу всех (т.е. каждой буквы по одной) -> O(N^2) 
    print(s)
    for sym in set(s): # число уникальных символов M
        count = 0
        for sub_sym in s: # всего симолов N
            if sym == sub_sym:
                count += 1
        print(sym, count)
# можно за O(N) - но как ?!!!
def strcount(s):
    print(s)
    syms_counter = {}
    for sym in s:
        # заходим в словарь по ключу и записываем туда подсчитанное число + 1, если не найдется элемент, то будет число 0
        syms_counter[sym] = syms_counter.get(sym, 0) + 1 
    print(syms_counter.items())

strcount("abcde")
strcount("aabbccd")