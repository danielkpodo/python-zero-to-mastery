# There is one last thing at the end of the try block, which is finally, and finally says that no
# matter what just do something for me


try:
    result = 1 / 2
except:
    print("operation not possible")
else:
    print(result)
finally:
    print("Ok, am done")
