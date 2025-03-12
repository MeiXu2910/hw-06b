def classify_triangle(a, b, c):
    """Classifies a triangle based on side lengths a, b, and c."""
    
    if not all(isinstance(x, (int, float)) and x > 0 for x in [a, b, c]):
        return "Invalid input"

    a, b, c = sorted([a, b, c])

    if a + b <= c:
        return "Not a triangle"

    if a == b == c:
        return "Equilateral"
    elif a == b or b == c:
        if round(a**2 + b**2, 5) == round(c**2, 5):
            return "Isosceles and Right"
        return "Isosceles"
    elif round(a**2 + b**2, 5) == round(c**2, 5):
        return "Right"
    else:
        return "Scalene"
