import numpy as np
import matplotlib.pyplot as plt


def load_horizons_vectors(filename):
    """
    Lee un fichero VECTOR TABLE de Horizons usando las marcas $$SOE / $$EOE.
    Devuelve el array numérico completo.
    """
    data_lines = []
    inside = False

    with open(filename, 'r') as f:
        for line in f:
            if "$$SOE" in line:
                inside = True
                continue
            if "$$EOE" in line:
                break
            if inside:
                data_lines.append(line.strip())

    data = np.genfromtxt(data_lines, delimiter=",")
    return data


def detect_tli(r):
    """
    Detecta el instante aproximado de la TLI buscando
    el mayor incremento en la distancia al centro de la Tierra.
    """
    dr = np.diff(r)
    idx = np.argmax(dr)
    return idx


# ======== CARGA DE DATOS ========

filename = "artemis_vectors.csv"  # cambia el nombre si es necesario
data = load_horizons_vectors(filename)

jd = data[:, 0]
x = data[:, 2]
y = data[:, 3]
z = data[:, 4]
vx = data[:, 5]
vy = data[:, 6]
vz = data[:, 7]

# ======== CÁLCULOS ========

r = np.sqrt(x**2 + y**2 + z**2)
tli_index = detect_tli(r)

print(f"Instante aproximado de TLI (JD TDB): {jd[tli_index]:.6f}")

# ======== GRÁFICA 3D DE LA TRAYECTORIA ========

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(projection='3d')

ax.plot(x, y, z)
ax.scatter([0], [0], [0], s=200)  # Tierra en el origen
ax.scatter(x[tli_index], y[tli_index], z[tli_index], s=80)

ax.set_xlabel("X (km)")
ax.set_ylabel("Y (km)")
ax.set_zlabel("Z (km)")
ax.set_title("Trayectoria Artemis II en marco eclíptico J2000 (ICRF)")

plt.tight_layout()
plt.show()

# ======== DISTANCIA AL CENTRO DE LA TIERRA ========

plt.figure(figsize=(10, 4))
plt.plot(r)
plt.scatter(tli_index, r[tli_index], s=60)
plt.ylabel("Distancia al centro de la Tierra (km)")
plt.xlabel("Índice temporal (cada 30 min)")
plt.title("Evolución de la distancia geocéntrica")
plt.tight_layout()
plt.show()

# ======== ANIMACIÓN SOBRE LA TRAYECTORIA ========

from matplotlib.animation import FuncAnimation

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(projection='3d')

# Trayectoria completa (estática)
ax.plot(x, y, z, alpha=0.3)

# Tierra
ax.scatter([0], [0], [0], s=200)

# Punto móvil (la nave)
probe, = ax.plot([], [], [], marker='o')

ax.set_xlabel("X (km)")
ax.set_ylabel("Y (km)")
ax.set_zlabel("Z (km)")

# Fijar límites para que no cambien durante la animación
ax.set_xlim(min(x), max(x))
ax.set_ylim(min(y), max(y))
ax.set_zlim(min(z), max(z))


def update(frame):
    probe.set_data([x[frame]], [y[frame]])
    probe.set_3d_properties([z[frame]])
    return probe,


ani = FuncAnimation(fig, update, frames=len(x), interval=50)

plt.show()
