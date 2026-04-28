class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"2D Vector: {self.x}i + {self.y}j")

class Vector3D(Vector2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)   # 2D class ka constructor call
        self.z = z

    def show(self):
        print(f"3D Vector: {self.x}i + {self.y}j + {self.z}k")


v2 = Vector2D(2, 3)
v2.show()

v3 = Vector3D(4, 5, 6)
v3.show()