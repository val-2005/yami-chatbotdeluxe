import streamlit as st

st.set_page_config(page_title="VitaBalance - Encuesta de Autocuidado", page_icon="💬", layout="centered")

# Encabezado
st.title("🤖 VitaBalance")
st.markdown("Hola, soy **VitaBalance**, tu asistente de bienestar. Vamos a explorar cómo te estás cuidando últimamente. 😊\n\nResponde cada afirmación según cómo te sientas actualmente, usando esta escala:")

st.markdown("""
- 1: Totalmente en desacuerdo  
- 2: En desacuerdo  
- 3: Ni de acuerdo ni en desacuerdo  
- 4: De acuerdo  
- 5: Totalmente de acuerdo  
""")

preguntas = [
    "Realizo actividad física de manera regular (al menos 3 veces por semana).",
    "Me siento con energía suficiente para cumplir con mis actividades cotidianas.",
    "Identifico cuándo estoy estresado(a) y puedo reconocer las causas.",
    "Utilizo estrategias para calmarme cuando me siento tenso(a).",
    "Me siento emocionalmente estable durante la mayor parte del tiempo.",
    "Tengo metas claras a corto y largo plazo.",
    "Siento que mi vida tiene un propósito que me motiva.",
    "Mantengo contacto frecuente con familiares o amigos.",
    "Me siento apoyado(a) por las personas que me rodean.",
    "Puedo recuperarme emocionalmente después de momentos difíciles.",
    "Confío en mis capacidades para resolver problemas.",
    "Tengo hábitos diarios que me ayudan a sentirme mejor.",
    "Me doy tiempo para mí y mis necesidades personales.",
    "Estoy atenta(o) a cambios en mi cuerpo, mente o emociones.",
    "Hago pausas para reflexionar cómo me siento y qué necesito mejorar."
]

respuestas = []

with st.form("form_chat_vitabalance"):
    for i, pregunta in enumerate(preguntas):
        with st.chat_message("VitaBalance"):
            st.write(f"**{pregunta}**")
        respuesta = st.slider(
            label=f"Tu respuesta a la pregunta {i+1}",
            min_value=1, max_value=5, step=1,
            key=f"respuesta_{i}"
        )
        respuestas.append(respuesta)

    submitted = st.form_submit_button("Enviar respuestas")

# Resultados
if submitted:
    promedio = sum(respuestas) / len(respuestas)
    st.chat_message("VitaBalance").markdown("Gracias por completar la encuesta. Aquí tienes tus resultados:")

    with st.chat_message("VitaBalance"):
        st.write(f"🔎 Tu puntaje promedio de autocuidado es: **{promedio:.2f}** sobre 5.")

        if promedio >= 4:
            st.success("¡Buen trabajo! Tus respuestas reflejan un buen nivel de autocuidado. 🌟")
        elif promedio >= 2.5:
            st.warning("Tienes un nivel medio de autocuidado. Puedes seguir mejorando en algunos aspectos. 💡")
        else:
            st.error("Tu nivel de autocuidado es bajo. Reflexiona sobre posibles cambios que podrías realizar. ❤️‍🩹")

