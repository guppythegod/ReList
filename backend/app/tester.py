try:
    print("something")
    x = 5
except Exception as e:
    print(e)
else:
    print("something else = " + str(x))