def wrapper(callback):
    def indoor(greeting):
        print("*****")
        callback(greeting)
        print("*****")
    return indoor


@wrapper
def c(a):
    print(a)

cin ="hi"

c(cin)





