import copy
import matplotlib.pyplot as plt
import numpy as np

def es_seguro(tablero, fila, col, n):
    # Verificar la misma columna
    for i in range(fila):
        if tablero[i][col] == 1:
            return False
            
    # Verificar diagonal principal (\)
    i, j = fila, col
    while i >= 0 and j >= 0:
        if tablero[i][j] == 1:
            return False
        i -= 1
        j -= 1
        
    # Verificar diagonal secundaria (/)
    i, j = fila, col
    while i >= 0 and j < n:
        if tablero[i][j] == 1:
            return False
        i -= 1
        j += 1
        
    return True

def resolver_n_reinas(tablero, fila, n, soluciones):
    if fila == n:
        soluciones.append(copy.deepcopy(tablero))
        return True
        
    for col in range(n):
        if es_seguro(tablero, fila, col, n):
            tablero[fila][col] = 1 # Colocar reina
            resolver_n_reinas(tablero, fila + 1, n, soluciones)
            tablero[fila][col] = 0 # Retroceder (Backtracking)

def n_reinas(n):
    # Inicializar matriz de n x n con ceros
    tablero = [[0 for _ in range(n)] for _ in range(n)]
    soluciones = []
    resolver_n_reinas(tablero, 0, n, soluciones)
    return soluciones

def visualizar_tablero(solucion, n, num_solucion):
    """
    Usa matplotlib para dibujar el tablero de ajedrez y colocar las reinas.
    """
    # 1. Crear matriz para el patrón de colores del tablero (casillas alternas)
    tablero_visual = np.zeros((n, n))
    tablero_visual[1::2, ::2] = 1
    tablero_visual[::2, 1::2] = 1
    
    fig, ax = plt.subplots(figsize=(6, 6))
    
    # 2. Dibujar el fondo del tablero en escala de grises
    ax.imshow(tablero_visual, cmap='gray_r', interpolation='nearest')
    
    # 3. Superponer el texto (símbolo de la reina) en las casillas correspondientes
    for fila in range(n):
        for col in range(n):
            if solucion[fila][col] == 1:
                # Símbolo unicode de reina roja centrado en la coordenada (col, fila)
                ax.text(col, fila, '♛', fontsize=max(20, 200 // n), 
                        ha='center', va='center', color='red')
                
    ax.set_title(f"Problema de las {n}-Reinas (Solución {num_solucion})")
    ax.set_xticks([])
    ax.set_yticks([])
    plt.show()

if __name__ == "__main__":
    try:
        n = int(input("Introduce el tamaño del tablero (N): "))
        soluciones = n_reinas(n)
        
        if soluciones:
            print(f"Se encontraron {len(soluciones)} soluciones en total.")            
            # Dibujamos solo la primera solución para no saturar la pantalla, 
            # especialmente con valores grandes donde crecen exponencialmente las combinaciones.
            visualizar_tablero(soluciones[0], n, 1)
        else:
            print(f"No existen soluciones posibles para un tablero de {n}x{n}.")
            
    except ValueError:
        print("Por favor, introduce un número entero válido.")