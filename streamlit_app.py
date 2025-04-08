import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Criterios de Calidad de Software")
st.write(
    "Los criterios de calidad de software son un conjunto de características y atributos que se utilizan para evaluar la calidad de un software. Estos criterios son fundamentales para garantizar que el software cumpla con las expectativas y necesidades de los usuarios. A continuación, se presentan algunos de los criterios más comunes:"
)

st.write("# ISO 25010")
st.write(
    "El modelo ISO 25010 es un estándar internacional que define un marco para evaluar la calidad del software. Este modelo se basa en ocho características principales, cada una de las cuales se divide en subcaracterísticas."
)

st.write("## Criterios medidos en el proyecto")
st.write("### Efectividad")

st.write("#### Tareas con errores")
st.write("Proporción de tareas donde los errores fueron realizados por el usuario")
st.latex(r"""
\text{Proporción de errores} = \frac{\text{Número de tareas con errores}}{\text{Número total de tareas}}
""")
tareas = ["Iniciar sesión", "Elegir carrera", "Elegir asignatura", "Generar excel"]
errores_usuario = [0.5, 0.2, 0.2, 0.1]

fig, ax = plt.subplots(figsize=(10, 5))
bars1 = ax.bar(tareas, errores_usuario, label='Errores del usuario', color='#F07C1B')

for bar in bars1:
    yval = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        yval,
        f"{yval:.0%}",
        ha='center',
        va='bottom',
        fontsize=10,
        color='black'
    )

ax.set_title("Origen de los Errores en Tareas", pad=20)
ax.set_ylabel("Proporción de errores")
ax.legend(loc='upper right')
ax.set_ylim(0, 1.1)
st.pyplot(fig)

col1, col2 = st.columns(2)
with col1:
    st.metric("Tasa promedio errores usuario", f"{np.mean(errores_usuario)*100:.1f}%")

st.write("#### Intensidad de error en la tarea")
st.write("Proporción de usuarios que cometen un error al realizar una tarea")
st.latex(r"""
\text{Intensidad de error} = \text{Cantidad total de errores cometidos por los usuarios en una tarea}
""")
intensidad_error = [2, 1, 3, 0]  # cantidad de errores
fig, ax = plt.subplots(figsize=(10, 5))
bars2 = ax.bar(tareas, intensidad_error, label='Intensidad de error', color='#E74C3C')
for bar in bars2:
    yval = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        yval,
        f"{yval:.0f}",
        ha='center',
        va='bottom',
        fontsize=10,
        color='black'
    )
ax.set_title("Intensidad de Error por Tarea", pad=20)
ax.set_ylabel("Cantidad de errores")
ax.legend(loc='upper right')
ax.set_ylim(0, max(intensidad_error) + 1)
st.pyplot(fig)
col1, col2 = st.columns(2)
with col1:
    st.metric("Promedio de errores por tarea", f"{np.mean(intensidad_error):.1f} errores")
with col2:
    st.metric("Tarea con más errores", f"{max(intensidad_error)} errores")


st.write("### Eficiencia")

st.write("#### Tiempo de tarea")
st.write("Tiempo promedio que un usuario tarda en completar una tarea")
st.latex(r"""
\text{Tiempo promedio} = \frac{\sum_{i=1}^n \text{Tiempo}_i}{n}
""")

tiempos_tarea = [12.5, 8.2, 15.3, 6.7]  # en segundos

fig, ax = plt.subplots(figsize=(10, 5))
bars = ax.bar(tareas, tiempos_tarea, color='#2E86C1')

for bar in bars:
    yval = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        yval,
        f"{yval:.1f}s",
        ha='center',
        va='bottom',
        fontsize=10,
        color='black'
    )

ax.set_title("Tiempo Promedio por Tarea", pad=20)
ax.set_ylabel("Segundos")
st.pyplot(fig)

col1, col2 = st.columns(2)
with col1:
    st.metric("Tiempo promedio total", f"{np.mean(tiempos_tarea):.1f} segundos")
with col2:
    st.metric("Tarea más rápida", f"{min(tiempos_tarea):.1f} segundos")

st.write("#### Relación de tiempo productivo")
st.write("Proporción de tiempo productivo en relación al tiempo total de la tarea")
st.latex(r"""
\text{Proporción de tiempo productivo} = \frac{\text{Tiempo productivo}}{\text{Tiempo total de la tarea}}
""")

tiempo_productivo = [0.85, 0.92, 0.78, 0.95]  # proporción

fig, ax = plt.subplots(figsize=(10, 5))
bars = ax.bar(tareas, tiempo_productivo, color='#28B463')

for bar in bars:
    yval = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        yval,
        f"{yval:.0%}",
        ha='center',
        va='bottom',
        fontsize=10,
        color='black'
    )

ax.set_title("Proporción de Tiempo Productivo por Tarea", pad=20)
ax.set_ylabel("Proporción")
ax.set_ylim(0, 1.1)
st.pyplot(fig)

st.metric("Promedio tiempo productivo", f"{np.mean(tiempo_productivo)*100:.1f}%")

st.write("#### Acciones innecesarias")
st.write("Proporción de las acciones realizadas por el usuario que no son necesarias para lograr los objetivos de la tarea")
st.latex(r"""
\text{Porcentaje innecesarias} = \frac{\sum \text{Acciones innecesarias}}{\sum \text{Acciones totales}} \times 100
""")

acciones_totales = [15, 12, 18, 8]
acciones_innecesarias = [0, 0, 5, 0]

fig, ax = plt.subplots(figsize=(10, 5))
width = 0.35
x = np.arange(len(tareas))

bars1 = ax.bar(x - width/2, acciones_totales, width, label='Acciones totales', color='#3498DB')
bars2 = ax.bar(x + width/2, acciones_innecesarias, width, label='Acciones innecesarias', color='#E74C3C')

ax.set_title("Acciones por Tarea", pad=20)
ax.set_ylabel("Cantidad de acciones")
ax.set_xticks(x)
ax.set_xticklabels(tareas)
ax.legend()

st.pyplot(fig)

col1, col2 = st.columns(2)
with col1:
    st.metric("Total acciones innecesarias", sum(acciones_innecesarias))
with col2:
    st.metric("Porcentaje promedio", f"{(sum(acciones_innecesarias)/sum(acciones_totales))*100:.1f}%")

st.write("## Resumen de Métricas de Calidad")

metricas = {
    "Efectividad": {
        "Tasa errores usuario": f"{np.mean(errores_usuario)*100:.1f}%",
        "Intensidad error": "3.2/10"
    },
    "Eficiencia": {
        "Tiempo promedio": f"{np.mean(tiempos_tarea):.1f} seg",
        "Tiempo productivo": f"{np.mean(tiempo_productivo)*100:.1f}%",
        "Acciones innecesarias": f"{(sum(acciones_innecesarias)/sum(acciones_totales))*100:.1f}%"
    },
}

for categoria, datos in metricas.items():
    st.write(f"### {categoria}")
    cols = st.columns(len(datos))
    for col, (nombre, valor) in zip(cols, datos.items()):
        with col:
            st.metric(nombre, valor)

st.write("## Conclusiones y Recomendaciones")

st.write("""
1. **Efectividad**: La tasa de errores es aceptable pero podría mejorarse, especialmente en las tareas de 'Iniciar sesión' y 'Elegir asignatura'.
2. **Eficiencia**: Los tiempos de tarea son razonables, pero se observan oportunidades para reducir acciones innecesarias.
3. **Satisfacción**: La satisfacción general es buena, pero la tarea 'Elegir asignatura' tiene la puntuación más baja.

**Recomendaciones**:
- Simplificar el proceso de inicio de sesión
- Mejorar la interfaz para selección de asignaturas
- Optimizar el flujo de trabajo para reducir acciones redundantes
""")
