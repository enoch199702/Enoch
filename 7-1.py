file_loc = input()
keyword = input()
import operator
with open(file_loc, mode="r", encoding="utf-8") as words:
    words_list = []
    for line in words:
        sp_line = line.split('\t')
        a_line = sp_line[0].strip()
        b_line = sp_line[1].strip()
        words_list.append(a_line)
        words_list.append(b_line)

rangea = 0
before_dict = dict()
after_dict = dict()
while True:
    for i in range(len(words_list)):
        key_find = words_list[i][rangea:].find(keyword)
        if key_find != -1:
            key_pos = rangea + key_find
        if key_find != -1:
            if key_pos - 1 >= 0:
                before_keyword = words_list[i][key_pos - 1]
            else:
                before_keyword = 0
            if key_pos + len(keyword) <= len(words_list[i]) - 1:
                after_keyword = words_list[i][key_pos + len(keyword)]
            else:
                after_keyword = 0 

            if before_keyword != 0:
                if before_keyword in before_dict.keys():
                    before_dict[before_keyword] += 1
                elif before_keyword not in before_dict.keys():
                    before_dict[before_keyword] = 1
            if after_keyword != 0:
                if after_keyword in after_dict.keys():
                    after_dict[after_keyword] += 1
                elif after_keyword not in after_dict.keys():
                    after_dict[after_keyword] = 1
            if key_pos < len(words_list[i]) - 1:
                rangea = key_pos + 1
            else:
                rangea = key_pos
            break
        elif key_find == -1:
            rangea = 0
            words_list.pop(i)
            break
    if len(words_list) == 0:
        break

sorted_before_dict = sorted(before_dict.items(), key=operator.itemgetter(1), reverse=True) 
sorted_after_dict = sorted(after_dict.items(), key=operator.itemgetter(1), reverse=True)
print("熱門前一個字:")
if len(sorted_before_dict) >= 10:
    for i in range(10):
        print(sorted_before_dict[i][0] + "---" + str(keyword))
else:
    for i in range(len(sorted_before_dict)):
       print(sorted_before_dict[i][0] + "---" + str(keyword))
print("熱門下一個字:")
if len(sorted_after_dict) >= 10:
    for j in range(10):
        print(str(keyword) + "---" + sorted_after_dict[j][0])
else:
    for j in range(len(sorted_after_dict)):
        print(str(keyword) + "---" + sorted_after_dict[j][0])