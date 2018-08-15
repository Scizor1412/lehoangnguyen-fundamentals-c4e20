def is_inside(point, retangle):
    if retangle[0] <= point[0] <= retangle[0]+ retangle[2] and retangle[1] <= point[1] <= retangle[1] + retangle[3]:
        is_inside = True
    else:
        is_inside = False
    return is_inside

result = is_inside([100, 120], [140, 60, 100, 200])
print (result)