ventas = [
    [12, 15, 10, 18],  
    [8, 14, 16, 12],  
    [20, 18, 15, 22],  
]
print("=== 1. MATRIZ COMPLETA DE VENTAS (en millones) ===")
for i in range(len(ventas)):
  print(f"Vendedor {i + 1}:", end=" ")
  for j in range(len(ventas[i])):
    print(f"Semana {j + 1}: ${ventas[i][j]}M", end=" | ")
  print() 
print("\n=== 2. TOTAL DE VENTAS POR VENDEDOR ===")
totales_vendedores = []
for i in range(len(ventas)):
  suma_vendedor = 0
  for j in range(len(ventas[i])):
    suma_vendedor += ventas[i][j]  
  totales_vendedores.append(suma_vendedor)
  print(f"Vendedor {i + 1}: ${suma_vendedor} millones")

print("\n=== 3. TOTAL DE VENTAS POR SEMANA ===")
num_semanas = len(ventas[0])
totales_semanas = [0] * num_semanas
for j in range(num_semanas):
  suma_semana = 0
  for i in range(len(ventas)):
    suma_semana += ventas[i][j]  
  totales_semanas[j] = suma_semana
  print(f"Semana {j + 1}: ${suma_semana} millones")

print("\n=== 4. VENDEDOR CON MAYOR TOTAL DE VENTAS ===")
max_ventas_vendedor = totales_vendedores[0]
mejor_vendedor = 1
for i in range(1, len(totales_vendedores)):
  if totales_vendedores[i] > max_ventas_vendedor:
    max_ventas_vendedor = totales_vendedores[i]
    mejor_vendedor = i + 1
print(
    f"El vendedor con mayor venta total fue el Vendedor {mejor_vendedor} con"
    f" ${max_ventas_vendedor} millones."
)
print("\n=== 5. SEMANA CON MAYOR VOLUMEN DE VENTAS ===")
max_ventas_semana = totales_semanas[0]
mejor_semana = 1
for j in range(1, len(totales_semanas)):
  if totales_semanas[j] > max_ventas_semana:
    max_ventas_semana = totales_semanas[j]
    mejor_semana = j + 1
print(
    f"La semana con mayor volumen de ventas fue la Semana {mejor_semana} con"
    f" ${max_ventas_semana} millones."
)
print("\n=== 6. PROMEDIO GENERAL DE VENTAS ===")
total_general = 0
contador_elementos = 0
for fila in ventas:
  for valor in fila:
    total_general += valor
    contador_elementos += 1
promedio_general = total_general / contador_elementos
print(f"El promedio general de ventas es: ${promedio_general:.2f} millones")
print("\n=== 7. MODIFICAR UN VALOR DE LA MATRIZ ===")
print("Modificando las ventas del Vendedor 1 en la Semana 2 a 25...")
ventas[0][1] = 25

print("Matriz actualizada:")
for i in range(len(ventas)):
  print(f"Vendedor {i + 1}: {ventas[i]}")