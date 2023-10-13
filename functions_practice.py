def say_hello():
  print('hello')
say_hello()

def pack(hi, hello, bye):
  return[hi, hello, bye]
print(pack("hi","hello","bye"))


def eat_lunch(lunch_list):
  if len(lunch_list) == 0:
    print("My lunchbox is empty!")
  else:
    for i in range(len(lunch_list)):
      if i == 0:
        print(f"First I eat {lunch_list[0]}")
      else:
        print(f"Next I eat {lunch_list[i]}")
eat_lunch([])
eat_lunch(["soup"])
eat_lunch(["soup","salad","fish","cake"])