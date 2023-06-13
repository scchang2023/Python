# 根據調查，大家喜歡用這種格式來命名：英國潛水艇 Boaty McBoateface、澳洲賽馬
# Horsey McHorseface、瑞典火車 Trainy McTrainface。使用 % 格式化來為國家博覽會
# 的獲勝者 duck、gourd 和 spitz 印出名字。
names=['duck', 'gourd', 'spitz']
for name in names:
    cap_name=name.capitalize()
    print("%sy Mc%sface" % (cap_name, cap_name))

print()
# 用 format() 格式化做同一件事。
for name in names:
    cap_name=name.capitalize()
    print("{}y Mc{}face".format(cap_name, cap_name))

print()
# 用 f-strings 憑感覺再做一次。
for name in names:
    cap_name=name.capitalize()
    print(f"{cap_name}y Mc{cap_name}face")