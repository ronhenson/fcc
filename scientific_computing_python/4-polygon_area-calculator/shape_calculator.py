class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):\
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        return "".join([f'{"*" * self.width}\n'] * (self.height))

    def get_amount_inside(self, rect):
        return \
            int(self.height / rect.height) * \
            int(self.width / rect.width)

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'


class Square(Rectangle):
    def __init__(self, side):
        width = side
        height = side
        super().__init__(width, height)

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.height = height
        self.width = height

    def __str__(self):
        return f'Square(side={self.width})'


if __name__ == "__main__":

    # rect = Rectangle(60, 6)
    # rect.set_width(45)
    # print(f'width = {rect.width}    height = {rect.height}')
    # pic = rect.get_picture()
    # print(pic)

    sq = Square(5)
    rect = Rectangle(15, 10)
    print(rect.get_amount_inside(sq))
