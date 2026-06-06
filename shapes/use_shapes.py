import shapes
from shapes import circle
from shapes.rectangle import area as rect_area

circle_area = circle.area(5)
circle_perimeter = circle.perimeter(5)

rectangle_area = rect_area(4, 6)
rectangle_perimeter = shapes.rectangle.perimeter(4, 6)

triangle_area = shapes.triangle.area(4, 3)
triangle_perimeter = shapes.triangle.perimeter(3, 4, 5)

print(("circle", circle_area, circle_perimeter))
print(("rectangle", rectangle_area, rectangle_perimeter))
print(("triangle", triangle_area, triangle_perimeter))

areas = {
    "circle": circle_area,
    "rectangle": rectangle_area,
    "triangle": triangle_area
}

print("Areas:", areas)
