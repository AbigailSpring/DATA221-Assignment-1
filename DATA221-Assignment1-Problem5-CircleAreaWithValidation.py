import math
def circle_area_coverage(radius_circle_1, radius_circle_2):
    if not isinstance(radius_circle_1, int) or not isinstance(radius_circle_2, int):
        return "Both radii must be integers."
    if radius_circle_1 <= 0 or radius_circle_2 <=0:
        return "Both radii must be positive integers."
    area_circle_1 = math.pi*radius_circle_1**2
    area_circle_2 = math.pi*radius_circle_2**2
    smaller_area = min(area_circle_1, area_circle_2)
    larger_area = max(area_circle_1, area_circle_2)
    coverage_percentage = (smaller_area / larger_area)*100
    return coverage_percentage
print(circle_area_coverage(3, 5))