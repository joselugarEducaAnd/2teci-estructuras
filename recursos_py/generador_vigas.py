import matplotlib.pyplot as plt
import matplotlib.patches as patches

def dibujar_viga_isostatica():
    # Configuración del lienzo
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.set_aspect('equal')
    ax.axis('off')  # Ocultar ejes
    
    # Parámetros geométricos
    L = 6      # Longitud
    H = 0.6    # Altura viga
    y_suelo = -1.2
    
    # 1. DIBUJAR LA VIGA
    # Rectángulo gris con borde negro
    viga = patches.Rectangle((0, 0), L, H, facecolor='#e0e0e0', edgecolor='black', linewidth=1.5)
    ax.add_patch(viga)
    
    # 2. APOYO A (Articulado / Fijo) - Triángulo
    # Coordenadas: (0.5, 0)
    xA = 0.5
    path_A = [[xA, 0], [xA-0.3, -0.6], [xA+0.3, -0.6]]
    triangulo_A = patches.Polygon(path_A, closed=True, facecolor='white', edgecolor='black', linewidth=1.5)
    ax.add_patch(triangulo_A)
    # Suelo A (Línea con rayitas)
    ax.plot([xA-0.5, xA+0.5], [-0.6, -0.6], color='black', linewidth=1.5)
    for i in range(6):
        x_r = (xA-0.5) + i*0.2
        ax.plot([x_r, x_r-0.15], [-0.6, -0.75], color='black', linewidth=0.8)
    ax.text(xA, -0.4, "A", ha='center', fontsize=12, fontweight='bold')

    # 3. APOYO B (Rodillo / Móvil) - Triángulo con ruedas
    # Coordenadas: (5.5, 0)
    xB = 5.5
    path_B = [[xB, 0], [xB-0.3, -0.5], [xB+0.3, -0.5]]
    triangulo_B = patches.Polygon(path_B, closed=True, facecolor='white', edgecolor='black', linewidth=1.5)
    ax.add_patch(triangulo_B)
    # Ruedas
    circulo1 = patches.Circle((xB-0.15, -0.6), 0.1, facecolor='white', edgecolor='black')
    circulo2 = patches.Circle((xB+0.15, -0.6), 0.1, facecolor='white', edgecolor='black')
    ax.add_patch(circulo1)
    ax.add_patch(circulo2)
    # Suelo B
    ax.plot([xB-0.5, xB+0.5], [-0.7, -0.7], color='black', linewidth=1.5)
    for i in range(6):
        x_r = (xB-0.5) + i*0.2
        ax.plot([x_r, x_r-0.15], [-0.7, -0.85], color='black', linewidth=0.8)
    ax.text(xB, -0.35, "B", ha='center', fontsize=12, fontweight='bold')

    # 4. CARGAS (Vectores)
    # Carga F (Azul)
    ax.annotate("", xy=(3, H), xytext=(3, H+2),
                arrowprops=dict(facecolor='blue', edgecolor='blue', width=4, headwidth=12))
    ax.text(3.2, H+1, r"$\vec{F}$", color='blue', fontsize=14, fontweight='bold')

    # 5. REACCIONES (Vectores Rojos)
    # RAy
    ax.annotate("", xy=(xA, -0.6), xytext=(xA, -1.8),
                arrowprops=dict(facecolor='red', edgecolor='red', width=3, headwidth=10))
    ax.text(xA-0.6, -1.2, r"$R_{Ay}$", color='red', fontsize=12)
    
    # RAx
    ax.annotate("", xy=(xA, H/2), xytext=(xA-1.2, H/2),
                arrowprops=dict(facecolor='red', edgecolor='red', width=3, headwidth=10))
    ax.text(xA-1.2, H/2+0.2, r"$R_{Ax}$", color='red', fontsize=12)

    # RBy
    ax.annotate("", xy=(xB, -0.7), xytext=(xB, -1.9),
                arrowprops=dict(facecolor='red', edgecolor='red', width=3, headwidth=10))
    ax.text(xB+0.2, -1.3, r"$R_{By}$", color='red', fontsize=12)

    # 6. COTAS
    # Línea de cota
    ax.annotate("", xy=(0, -2.2), xytext=(L, -2.2),
                arrowprops=dict(arrowstyle='|-|', linewidth=1.2, color='black'))
    ax.text(L/2, -2.1, "L", ha='center', va='bottom', fontsize=12)

    # Ajustar límites para que no se corte nada
    ax.set_xlim(-1.5, L+1.5)
    ax.set_ylim(-2.5, 3.5)

    # Guardar
    plt.tight_layout()
    plt.savefig("viga_isostatica.png", dpi=300, bbox_inches='tight')
    print("Imagen 'viga_isostatica.png' generada con éxito.")

if __name__ == "__main__":
    dibujar_viga_isostatica()