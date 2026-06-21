class Circle:
    radius = 5

    def get_area(self):
        return 3.1416 * self.radius**2


new_circle = Circle()
print(new_circle.get_area())