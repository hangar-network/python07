import numpy as np
import turtle

# show examples from documentation: https://docs.python.org/3/tutorial/errors.html
class WrongSizeError(Exception):
    def __init__(self, msg):
        self.message = msg

class Polygon:
    def __init__(self, vertices):
        ''' vertices must be circular sorted'''
        self.vertices = np.array(vertices)

    def perimeter(self):
        p = 0
        num_vertices = len(self.vertices)
        for i in range(num_vertices):
            p += np.linalg.norm(self.vertices[(i+1)%num_vertices] - self.vertices[i])

        return p

    def area(self):
        print("Don't know what to do :(")
        return 0

    def draw(self, pen=None):
        if pen is None:
            t = turtle.Turtle()
        else:
            t = pen
        t.penup()
        t.goto(self.vertices[0][0], self.vertices[0][1])
        t.pendown()
        for vertex in self.vertices:
            t.goto(vertex[0], vertex[1])
        t.goto(self.vertices[0][0], self.vertices[0][1])

        turtle.mainloop()

class Triangle(Polygon):
    def __init__(self, vertices):
        '''Triangles have exactly 3 vertices'''
        if len(vertices) != 3:
            #print("Triangles must have exaclty 3 vertices, but {} were given".format(len(vertices)))
            raise WrongSizeError("Triangles must have exaclty 3 vertices, but {} were given".format(len(vertices)))
        Polygon.__init__(self, vertices)

    def area(self):
        a = np.linalg.norm(self.vertices[0] - self.vertices[1])
        b = np.linalg.norm(self.vertices[1] - self.vertices[2])
        c = np.linalg.norm(self.vertices[2] - self.vertices[0])
        # calculate the semi-perimeter
        s = (a + b + c) / 2
        # calculate the area
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        return area

    def draw(self, pen=None):
        t = turtle.Turtle()
        t.color("red")
        t.width(2.0)
        Polygon.draw(self, t)

if __name__ == '__main__':

    # triangle = Polygon([[-100,0], [100,0], [0, 200]])
    # print(triangle.area())
    # triangle.draw()
    try:
        triangle = Triangle([[-100,0], [100,0], [0, 200]])
        poly = Polygon([[-100,0], [100,0], [0, 200]])
    except WrongSizeError:
        print(e)
    except ValueError:

    else:
        print(triangle.area())
        triangle.draw()
        print("Is triangle a Triangle?", isinstance(triangle, Triangle))
        print("Is triangle a Polygon?", isinstance(triangle, Polygon))
        print("Is poly a Triangle?", isinstance(poly, Triangle))
        print("Is poly a Polygon?", isinstance(poly, Polygon))
