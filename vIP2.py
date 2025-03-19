import queue
from collections import deque


fila_normal = queue.Queue() 
fila_vip = deque() 


personas = [
    (1, "normal"),
    (2, "vip"),
    (3, "normal"),
    (4, "normal"),
    (5, "vip"),
    (6, "normal"),
    (7, "vip"),
    (8, "normal"),
    (9, "normal"),
    (10, "vip"),
    (11, "normal"),
    (12, "normal"),
    (13, "vip"),
    (14, "normal"),
    (15, "vip")
]


print("Llegada de personas al antro:")
for persona in personas:  
   
    print(f"Persona {persona[0]} - {persona[1]}")
    if persona[1] == "normal":
        
        fila_normal.put(persona)
    else:
        
        fila_vip.appendleft(persona)


print("\nOrden de ingreso al antro:")

while fila_vip:
   
    p = fila_vip.popleft()  
    print(f"Ingresando persona {p[0]} - {p[1]}")


while not fila_normal.empty():
    
    p = fila_normal.get()  
    print(f"Ingresando persona {p[0]} - {p[1]}")