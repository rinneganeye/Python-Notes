# <------------------------------------Break Statement------------------------------------>
# This statement breaks the loop if the condition is satisfied

for i in range(1, 10):
    if i == 5:  # as soon as i = 5, the loop will break
        break
    # print(i)

# <------------------------------------Continue Statement------------------------------------>
# This statement skips the assigned value

for j in range(1, 10):
    if j == 5:  # as soon as j = 5, it will skip 5 and move to 6
        continue
    print(j)
