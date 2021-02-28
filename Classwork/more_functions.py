'''
more functions, eveing class
'''
# swap swaps the value so the x,y becomes y,x
def swap( x, y, z):
    z = 15
    return y, x, z

def swap2( original_x, original_y, z):
    z = 0
    return original_y, original_x, z

def main():
    x = 10
    y = 20
    z = 0
    print('x = ', x, 'y = ', y, 'z = ', z)

    x, y, z = swap(x, y, 12)
    print('x = ', x, 'y = ',  y, 'z = ', z)

    x = 10
    y = 20
    z = 12
    print('origx = ', x, 'origy = ', y, 'z = ', z)

    x, y, z = swap2(original_y = y, original_x = x, z = z)
    print('origx = ', x, 'origy = ', y, 'z = ', z)
    

main()
