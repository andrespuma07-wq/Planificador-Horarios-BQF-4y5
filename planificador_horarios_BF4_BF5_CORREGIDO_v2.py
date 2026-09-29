import streamlit as st
import pandas as pd

st.set_page_config(page_title="Planificador BF4 + BF5", page_icon="🧪", layout="wide")

DIAS = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
HORAS = range(7, 19)

# ============================================================
# HORARIOS 2026-2027
# ============================================================
HORARIOS = {
    "BF4": {
        "P01": {
            "Química Orgánica II": [("Lunes",7,9),("Lunes",13,14),("Jueves",11,13),("Viernes",13,15)],
            "Química Analítica II": [("Martes",7,9),("Miércoles",7,10),("Viernes",10,12)],
            "Botánica": [("Lunes",9,11),("Lunes",14,15),("Martes",11,12),("Jueves",7,9)],
            "Bioquímica I": [("Martes",9,11),("Jueves",9,11),("Viernes",8,10)],
            # CORREGIDO: Miércoles 10-12
            "Diseño experimental": [("Lunes",11,12),("Miércoles",10,12),("Jueves",16,17)],
            "Fisicoquímica I": [("Miércoles",16,18),("Jueves",14,16),("Viernes",15,17)],
        },
        "P02": {
            "Botánica": [("Lunes",7,9),("Martes",7,9),("Jueves",11,13)],
            "Química Analítica II": [("Lunes",9,10),("Martes",9,11),("Jueves",7,9),("Viernes",7,9)],
            "Química Orgánica II": [("Lunes",10,12),("Miércoles",9,11),("Jueves",9,11),("Viernes",10,11)],
            # CORREGIDO: se agrega Viernes 09-10
            "Bioquímica I": [("Lunes",12,13),("Martes",11,13),("Miércoles",11,13),("Viernes",9,10)],
            "Fisicoquímica I": [("Martes",14,16),("Miércoles",14,16),("Viernes",11,12),("Viernes",14,15)],
            "Diseño experimental": [("Lunes",16,17),("Martes",16,17),("Jueves",14,16)],
        },
        "P03": {
            "Botánica": [("Miércoles",7,10),("Martes",12,14),("Lunes",13,14)],
            "Bioquímica I": [("Lunes",9,10),("Miércoles",13,15),("Jueves",14,16),("Viernes",10,11)],
            # Lunes 15-17 eliminado de Analítica II: pertenece a Orgánica II
            "Química Orgánica II": [("Martes",9,11),("Lunes",10,12),("Viernes",11,12),("Lunes",15,17)],
            "Diseño experimental": [("Miércoles",12,13),("Martes",14,15),("Viernes",13,15)],
            "Química Analítica II": [("Martes",15,18),("Miércoles",15,17),("Viernes",17,19)],
            # CORREGIDO: se agrega Viernes 07-10
            "Fisicoquímica I": [("Jueves",16,19),("Viernes",7,10)],
        },
        "P04": {
            "Química Analítica II": [("Lunes",17,19),("Martes",18,19),("Miércoles",17,19),("Viernes",15,17)],
        },
        "P05": {
            "Química Analítica II": [("Lunes",10,12),("Martes",11,12),("Jueves",9,11)],
        },
    },

    "BF5": {
        "P01": {
            # CORREGIDO: se agrega Lunes 13-14
            "Farmacognosia": [("Miércoles",8,11),("Lunes",13,14)],
            "Microbiología": [("Lunes",10,13),("Miércoles",14,15),("Jueves",17,19)],
            "Farmacología I": [("Martes",8,9),("Martes",10,12),("Jueves",14,15),("Viernes",10,12)],
            # CORREGIDO: se agrega Viernes 08-09
            "Bioquímica II": [("Martes",12,13),("Miércoles",11,13),("Viernes",8,9)],
            "Toxicología": [("Miércoles",15,18),("Jueves",11,14)],
            "Química Analítica Instrumental": [("Lunes",14,17),("Jueves",15,17),("Viernes",16,17)],
            "Fisicoquímica II": [("Martes",14,16),("Jueves",7,9),("Viernes",14,16)],
        },
        "P02": {
            "Farmacognosia": [("Lunes",7,9),("Miércoles",7,8),("Miércoles",14,15)],
            # CORREGIDO: se agrega Martes 08-09
            "Microbiología": [("Martes",7,10),("Lunes",10,12),("Viernes",12,13)],
            "Fisicoquímica II": [("Miércoles",8,12),("Viernes",16,18)],
            # CORREGIDO: se agrega Viernes 09-11
            "Farmacología I": [("Jueves",8,10),("Lunes",12,13),("Jueves",16,17),("Viernes",9,11)],
            "Química Analítica Instrumental": [("Martes",10,12),("Miércoles",13,14),("Jueves",10,13)],
            # CORREGIDO: se agrega Viernes 11-12
            "Bioquímica II": [("Martes",13,15),("Jueves",15,16),("Viernes",11,12)],
            # CORREGIDO: Viernes 07-08 pasa a 07-09
            "Toxicología": [("Viernes",7,9),("Viernes",14,15),("Lunes",15,17),("Jueves",17,18)],
        },
        "P03": {
            "Farmacognosia": [("Lunes",7,9),("Miércoles",7,8),("Miércoles",14,15)],
            "Microbiología": [("Viernes",7,9),("Lunes",9,12),("Martes",8,9)],
            "Fisicoquímica II": [("Miércoles",8,12),("Viernes",16,18)],
            "Farmacología I": [("Jueves",8,10),("Lunes",12,13),("Viernes",9,11),("Jueves",16,17)],
            "Química Analítica Instrumental": [("Martes",10,12),("Miércoles",13,14),("Jueves",10,13)],
            "Bioquímica II": [("Martes",13,15),("Jueves",15,16),("Viernes",11,12)],
            "Toxicología": [("Martes",9,10),("Martes",15,17),("Jueves",14,15),("Viernes",12,14)],
        },
    },
}

def horas_materia(bloques):
    return [(dia,h) for dia,inicio,fin in bloques for h in range(inicio,fin)]

def horas_totales(bloques):
    return sum(fin-inicio for _,inicio,fin in bloques)

def hora_txt(h):
    return f"{h:02d}:00 - {h+1:02d}:00"

def ofertas(semestre, materia):
    return [(p, HORARIOS[semestre][p][materia]) for p in HORARIOS[semestre] if materia in HORARIOS[semestre][p]]

def conflictos(seleccion):
    ocupacion = {}
    for item in seleccion:
        for clave in horas_materia(item["bloques"]):
            ocupacion.setdefault(clave, []).append(item)

    salida = []
    for (dia,h), items in ocupacion.items():
        # Un cruce solo cuenta entre materias diferentes.
        materias = {}
        for item in items:
            materias.setdefault((item["semestre"],item["paralelo"],item["materia"]), item)
        unicas = list(materias.values())

        if len(unicas) > 1:
            salida.append({
                "Día": dia,
                "Hora": hora_txt(h),
                "Cruce": " ↔ ".join(
                    f'{x["materia"]} ({x["semestre"]}-{x["paralelo"]})'
                    for x in unicas
                )
            })
    return salida

def tabla_horario(seleccion):
    df = pd.DataFrame("", index=[hora_txt(h) for h in HORAS], columns=DIAS)
    celdas = {}

    for item in seleccion:
        for dia,h in horas_materia(item["bloques"]):
            celdas.setdefault((dia,h), []).append(
                f'{item["materia"]}\n{item["semestre"]}-{item["paralelo"]}'
            )

    for (dia,h), valores in celdas.items():
        df.loc[hora_txt(h),dia] = "\n\n".join(valores)
    return df

def buscar_combinaciones(materias, limite=50):
    opciones = {}
    for semestre,materia in materias:
        clave = (semestre,materia)
        opciones[clave] = [
            {"semestre":semestre,"materia":materia,"paralelo":p,"bloques":b}
            for p,b in ofertas(semestre,materia)
        ]

    claves = sorted(opciones, key=lambda x: len(opciones[x]))
    resultados = []

    def backtrack(i,ocupadas,seleccion):
        if len(resultados) >= limite:
            return
        if i == len(claves):
            resultados.append(list(seleccion))
            return

        for oferta in opciones[claves[i]]:
            nuevas = set(horas_materia(oferta["bloques"]))
            if ocupadas.isdisjoint(nuevas):
                seleccion.append(oferta)
                backtrack(i+1,ocupadas|nuevas,seleccion)
                seleccion.pop()

    backtrack(0,set(),[])
    return resultados

# ============================================================
# INTERFAZ
# ============================================================

st.title("🧪 Planificador interactivo de horarios — BF4 + BF5")
st.write("Selecciona materias, prueba paralelos y verifica automáticamente los cruces.")

st.info(
    "Versión actualizada con las correcciones indicadas. "
    "Los horarios oficiales deben verificarse antes de matricularse."
)

tab1,tab2,tab3 = st.tabs(["✏️ Elegir paralelos","🔎 Buscar combinaciones","📚 Ver oferta"])

with tab1:
    st.subheader("Elegir un paralelo para cada materia")
    seleccion = []

    for semestre in ["BF4","BF5"]:
        st.markdown(f"### {semestre}")
        materias = sorted({m for p in HORARIOS[semestre].values() for m in p})

        for materia in materias:
            opciones = ["No cursar"] + [
                f"{p} — {horas_totales(b):g} h/semana" for p,b in ofertas(semestre,materia)
            ]
            elegido = st.selectbox(materia,opciones,key=f"{semestre}_{materia}")

            if elegido != "No cursar":
                paralelo = elegido.split(" — ")[0]
                seleccion.append({
                    "semestre":semestre,
                    "paralelo":paralelo,
                    "materia":materia,
                    "bloques":HORARIOS[semestre][paralelo][materia]
                })

    if seleccion:
        cr = conflictos(seleccion)
        c1,c2,c3 = st.columns(3)
        c1.metric("Materias",len(seleccion))
        c2.metric("Horas/semana",sum(horas_totales(x["bloques"]) for x in seleccion))
        c3.metric("Cruces",len(cr))

        if cr:
            st.error("⚠️ Hay cruces de horario.")
            st.dataframe(pd.DataFrame(cr),use_container_width=True,hide_index=True)
        else:
            st.success("✅ No hay cruces entre las materias seleccionadas.")

        st.subheader("Horario resultante")
        st.dataframe(tabla_horario(seleccion),use_container_width=True,height=620)
    else:
        st.warning("Selecciona al menos una materia.")

with tab2:
    st.subheader("Buscar automáticamente combinaciones sin cruces")

    m4 = sorted({m for p in HORARIOS["BF4"].values() for m in p})
    m5 = sorted({m for p in HORARIOS["BF5"].values() for m in p})

    c1,c2 = st.columns(2)
    with c1:
        sel4 = st.multiselect("Materias BF4",m4)
    with c2:
        sel5 = st.multiselect("Materias BF5",m5)

    limite = st.slider("Máximo de combinaciones",1,100,20)

    if st.button("🔎 Buscar combinaciones sin cruces",type="primary"):
        materias = [("BF4",m) for m in sel4] + [("BF5",m) for m in sel5]

        if not materias:
            st.warning("Selecciona al menos una materia.")
        else:
            resultados = buscar_combinaciones(materias,limite)
            if not resultados:
                st.error("No se encontró una combinación sin cruces para todas las materias seleccionadas.")
            else:
                st.success(f"Se encontraron {len(resultados)} combinación(es) compatibles.")

                for i,comb in enumerate(resultados,1):
                    titulo = " + ".join(f'{x["materia"]} ({x["semestre"]}-{x["paralelo"]})' for x in comb)
                    with st.expander(f"Combinación {i}: {titulo}",expanded=(i==1)):
                        st.dataframe(
                            pd.DataFrame([{
                                "Semestre":x["semestre"],
                                "Materia":x["materia"],
                                "Paralelo":x["paralelo"],
                                "Horas/semana":horas_totales(x["bloques"])
                            } for x in comb]),
                            use_container_width=True,hide_index=True
                        )
                        st.dataframe(tabla_horario(comb),use_container_width=True,height=620)

with tab3:
    st.subheader("Oferta completa")

    for semestre in ["BF4","BF5"]:
        st.markdown(f"### {semestre}")
        for paralelo,cursos in HORARIOS[semestre].items():
            filas=[]
            for materia,bloques in cursos.items():
                filas.append({
                    "Materia":materia,
                    "Horas/semana":horas_totales(bloques),
                    "Horario":" | ".join(f"{d} {i:02d}:00-{f:02d}:00" for d,i,f in bloques)
                })
            st.markdown(f"**{semestre}-{paralelo}**")
            st.dataframe(pd.DataFrame(filas),use_container_width=True,hide_index=True)

st.divider()
st.caption("Planificador académico. Verifica siempre la versión oficial de los horarios antes de matricularte.")
