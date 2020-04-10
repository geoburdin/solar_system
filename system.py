from vpython import sphere, vector, color, rotate
import math # Константы
G = 6.667e-11  # гравитационная постоянная, м^3 кг^-1 с^-2
MS = 1.9885e30  # масса Солнца, кг
ME = 5.97e24  # масса Земли, кг
MM = 7.348e22  # масса Луны, кг
RSE = 1.496e11  # среднее расстояние от Солнца до Земли, метры
REM = 384.4e6  # расстояние от Земли до Луны
# Гравитационная сила между Солнцем и Землей. Н
F_SE = G*MS*ME/(RSE*RSE)
# Гравитационная сила между Землей и Луной, Н
F_EM = G*ME*MM/(REM*REM)
# Угловая скорость Луны
wm = math.sqrt(F_EM/(MM*REM))
# Угловая скорость Земли
we = math.sqrt(F_SE/(ME*RSE))

v = vector(10, 0, 0)
Earth = sphere(pos=vector(RSE, 0, 0), color=color.green, radius=6371000, make_trail=True)
Moon = sphere(pos=vector(RSE + REM,0,0), color=color.white, radius=1737000, make_trail=True)
Sun = sphere(pos=vector(0, 0, 0), color=color.yellow, radius=696340000)
# Будем использовать полярные координаты
# Шаг
dt = 10
# углы поворота за один шаг:
theta_earth = we*dt
theta_moon = wm*dt
while dt <= 86400*365:
     # Земля и Луна поворачиваются вокруг оси z (0,0,1)
     Earth.pos = rotate(Earth.pos, angle=theta_earth, axis=vector(0, 0, 1))
     v = rotate(v, angle=theta_moon, axis=vector(0, 0, 1))
     Moon.pos = Earth.pos + v
     dt += 10
