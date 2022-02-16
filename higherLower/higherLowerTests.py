# test run
import random

data = [
    {
        "name": "john",
        "item": "10",
    },
    {
        "name": "josh",
        "item": "5",
    }
]

new_list = []

name_list = []

num_list = []

# for name in data:
#     if name["name"] == "john":
#         new_list.append(random.choice(name["name"]))
#         print(new_list)


for item in data:
    new_list.append(random.choice(data))
    print(new_list)

for item in new_list:
    name_list.append(item["name"])

print(f"\nWho has more items?\nCompare A: {name_list[0]}\nAgainst B: {name_list[1]}")
user_choice = input("Answer: ")

for item in new_list:
    num_list.append(int(item["item"]))

if num_list[0] > num_list[1]:
    print("true")
if num_list[0] == num_list[1]:
    print("equal")
elif num_list[0] < num_list[1]:
    print("false")

# x = 0
# while num_list[0] == num_list[1]:
#     for item in range(2):
#         new_list.remove(new_list[x])
#         random.choice(data)
#         x += 1

print(num_list)

remove_items = True
while remove_items:
    if len(new_list) != 0:
        del new_list[0]
    else:
        remove_items = False


print(new_list)
