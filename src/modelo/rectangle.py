class Rectangle():
    def __init__(self, name, lenght, width):
        self.name=name
        self.lenght=lenght
        self.width=width

    def area(self):
        area_calc=self.lenght*self.width
        return area_calc

    def perimeter(self):
        perimeter_calc=(2*self.lenght+2*self.width)
        return perimeter_calc



