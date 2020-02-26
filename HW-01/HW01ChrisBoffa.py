# equilateral triangles have all three sides with the same length
# isosceles triangles have two sides with the same length
# scalene triangles have three sides with different lengths
# right triangles have three sides with lengths, a, b, and c where a2 + b2 = c2


def classify_triangle(side_a, side_b, side_c):
    """
    Classifies the triangle based on the sides given
    """
    intersection = {side_a, side_b, side_c} & {side_a, side_b, side_c}
    is_right_triangle = side_a ** 2 + side_b ** 2 == side_c ** 2
    triangle_classification = 'Invalid Triangle'

    if side_a <= 0 or side_b <= 0 or side_c <= 0:
        return triangle_classification

    if is_right_triangle:
        triangle_classification = 'right'
    elif len(intersection) == 1:
        triangle_classification = 'equilateral'
    elif len(intersection) == 2:
        triangle_classification = 'isosceles'
    elif len(intersection) == 3:
        triangle_classification = 'scalene'

    return triangle_classification


if __name__ == '__main__':
    classify_triangle(3, 3, 1)
