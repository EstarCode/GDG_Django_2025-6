class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height


rectangle_length = Rectangle(width=10, height=20)
area = rectangle_length.width * rectangle_length.height
print(f"The area of the rectangle is: {area}")
