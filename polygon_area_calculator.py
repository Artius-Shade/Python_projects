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

  def get_perimeter(self):
    return 2 * self.width + 2 * self.height

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5

  def get_picture(self):
    x = (['*' * self.width for _ in range(round(self.height))])
    return '\n'.join(x) + '\n' if self.height <= 50 and self.width <= 50 else "Too big for picture."

  def get_amount_inside(self, other):
    return round(self.get_area() / other.get_area())

  def __str__(self):
    return f'Rectangle(width={self.width}, height={self.height})'


class Square(Rectangle):

  def __init__(self, side):
    self.side = side
    self.width = self.side
    self.height = self.side

  def set_side(self, side):
    self.side = side
    self.width = self.side
    self.height = self.side

  def set_width(self, width):
    self.set_side(width)

  def set_height(self, height):
    self.set_side(height)

  def __str__(self):
    return f"Square(side={self.side})"


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
