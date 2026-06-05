# Día 2 - Calculadora de Corrientazos
# 1. Cambia estos valores por los tuyos reales
nombre = "Daniel" 
precio_corrientazo = 15000  # ¿Cuánto vale donde almuerzas?
almuerzos_por_semana = 5  # ¿Cuántos días comes por fuera?
semanas_por_mes = 4
Si_cocino = 8000
# 2. Python hace la matemática por ti
gasto_semanal = precio_corrientazo * almuerzos_por_semana
gasto_mensual = gasto_semanal * semanas_por_mes
gasto_anual = gasto_mensual * 12

# Cuanto gasto si cocino
gasto_semanal_si_cocino = Si_cocino * almuerzos_por_semana
gasto_mensual_si_cocino = gasto_semanal_si_cocino * semanas_por_mes
gasto_anual_si_cocino = gasto_mensual_si_cocino *12

# Cuanto ahorro
ahorro_semanal = gasto_semanal - gasto_semanal_si_cocino
ahorro_mensual = gasto_mensual - gasto_semanal_si_cocino
ahorro_anual = gasto_anual - gasto_anual_si_cocino



# 3. Mostramos resultados bonitos con f-strings
print(f"Hola {nombre}!")
print(f"Si almuerzas fuera {almuerzos_por_semana} veces por semana:")
print(f"Gastas ${gasto_semanal:,} a la semana")
print(f"Gastas ${gasto_mensual:,} al mes")
print(f"Gastas ${gasto_anual:,} al año en corrientazos 😱")
print(f"Si almuerzas en casa {almuerzos_por_semana} veces por semana:")
print(f"Gastas ${gasto_semanal_si_cocino:,} a la semana")
print(f"Gastas ${gasto_mensual_si_cocino:,} al mes")
print(f"Gastas ${gasto_anual_si_cocino:,} al año en si cocinas en casa 😱")

# Ahorro
print(f"tu ahorro semanal es de: ${ahorro_semanal:,}")
print(f"tu ahorro semanal es de: ${ahorro_mensual:,}")
print(f"tu ahorro semanal es de: ${ahorro_anual:,}")

# Reto extra: ¿Cuántos meses de Netflix son esos?
netflix_mes = 38900
meses_netflix = gasto_mensual / netflix_mes
print(f"Con eso pagas {meses_netflix:.1f} meses de Netflix")