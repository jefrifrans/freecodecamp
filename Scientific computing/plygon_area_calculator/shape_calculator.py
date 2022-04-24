# class persegi panjang
class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        # memunculkan string
        return "Rectangle(width=" + str(self.width) + \
            ", height=" + str(self.height) + ")"

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height
        # cari Luas

    def get_perimeter(self):
        return 2 * (self.width + self.height)
        # cari nilai keliling

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5
        # cari nilai diagonal

    def get_picture(self):
        if self. width > 50 or self.height > 50:
            return "Too Big for picture"
        rectangle = ("*" * self.width + "\n") * self.height
        return rectangle

    def get_amount_inside(self, shape):
        # mencari berapa banyak maksimum yang dapat di isi kedalam persegi/persegi panjang
        max_width = self.width // shape.width
        max_height = self.height // shape.height

        return max_width * max_height

# class persegi


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
        # length = sisi, jadi yang dimasukkan di awal adalah panjang x lebar maka di class persegi menjadi sisix sisi

    def __str__(self):
        return "Square(side=" + str(self.width) + ")"

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, side):
        self.width = side
        self.height = side

    def set_height(self, side):
        self.width = side
        self.height = side
