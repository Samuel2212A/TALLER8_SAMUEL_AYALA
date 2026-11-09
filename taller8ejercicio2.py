curso_A = {"Ana", "Carlos", "Laura", "Pedro", "Sofia", "Andres", "Camila"}
curso_B = {"Laura", "Pedro", "Daniel", "Sofia", "Mateo", "Valentina"}

print("=== 1. ESTUDIANTES INSCRITOS ===")
print("Curso A (Fundamentos de Programación):", curso_A)
print("Curso B (Introducción a Bases de Datos):", curso_B)

todos_estudiantes = curso_A.union(curso_B) 
print("\n=== 2. TOTAL DE ESTUDIANTES DIFERENTES (UNIÓN) ===")
print(
    f"Hay {len(todos_estudiantes)} estudiantes diferentes en total:"
    f" {todos_estudiantes}"
)
ambos_cursos = curso_A.intersection(curso_B)  
print("\n=== 3. ESTUDIANTES EN AMBOS CURSOS (INTERSECCIÓN) ===")
print(ambos_cursos)
solo_A = curso_A.difference(curso_B)  
print("\n=== 4. ESTUDIANTES ÚNICAMENTE EN EL CURSO A ===")
print(solo_A)
solo_B = curso_B.difference(curso_A)  
print("\n=== 5. ESTUDIANTES ÚNICAMENTE EN EL CURSO B ===")
print(solo_B)
exactamente_uno = curso_A.symmetric_difference(
    curso_B
)  
print("\n=== 6. ESTUDIANTES EN EXACTAMENTE UN CURSO (DIFERENCIA SIMÉTRICA) ===")
print(exactamente_uno)
todos_a_en_b = curso_A.issubset(curso_B) 
print("\n=== 7. ¿TODOS LOS ESTUDIANTES DE A ESTÁN EN B? ===")
print(
    "¿Todos los estudiantes del curso A están inscritos en el curso B?",
    todos_a_en_b,
)
print("\n=== 8. AGREGAR NUEVO ESTUDIANTE ===")
print("Agregando al estudiante 'Julian' al Curso A...")
curso_A.add("Julian")  
print("Curso A actualizado:", curso_A)