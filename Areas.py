import math

# Function to calculate the area of a rectangle
def calculate_rectangle_area(length, width):
    return length * width

# Function to calculate the area of a circle
def calculate_circle_area(radius):
    return math.pi * radius ** 2

# Function to calculate the area of a triangle
def calculate_triangle_area(base, height):
    return 0.5 * base * height

# Main program
while True:
    print("Choose a shape to calculate the area:")
    print("1. Rectangle")
    print("2. Circle")
    print("3. Triangle")
    print("4. Quit")
    
    choice = input("Enter your choice (1/2/3/4):")
    
    if choice == "4":
        break
    
    if choice in ["1", "2", "3"]:
        if choice == "1":
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            area = calculate_rectangle_area(length, width)
        elif choice == "2":
            radius = float(input("Enter the radius of the circle: "))
            area = calculate_circle_area(radius)
        else:
            base = float(input("Enter the base of the triangle: "))
            height = float(input("Enter the height of the triangle: "))
            area = calculate_triangle_area(base, height)
        
        print(f"The area is: {area}")
    else:
        print("Invalid choice. Please choose 1, 2, 3, or 4.")
