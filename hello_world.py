import sys
import platform

print("hello")

print(1, sys.version)
print(2, platform.python_implementation())
print(3, sys.executable)


from direct.showbase.ShowBase import ShowBase

class MyApp(ShowBase):

        def __init__(self):
            ShowBase.__init__(self)

app = MyApp()
app.run()