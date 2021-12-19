x_min = 137
x_max = 171
y_min = -98
y_max = -73

valid_count = 0
for vx0 in range(17, x_max + 1): # Lower bound from solving for 1 + ... + vx ≥ 137
    for vy0 in range(y_min, abs(y_min) + 1):
        x = 0
        y = 0
        vx = vx0
        vy = vy0
        hit_target = False
        overshot = False
        while not hit_target and not overshot:
            x += vx
            y += vy
            if x >= x_min and x <= x_max and y >= y_min and y <= y_max:
                hit_target = True
            elif x > x_max or y < y_min:
                overshot = True
            vx = vx - 1 if vx > 0 else 0
            vy -= 1
        if hit_target:
            valid_count += 1

print(valid_count)
