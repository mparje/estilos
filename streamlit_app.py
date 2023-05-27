import streamlit as st
import openai
import os

# Configura tus credenciales de OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

# Categorías de estilos de texto
categorias = {
    'Formal': 'El texto formal tiene un tono serio y profesional.',
    'Informal': 'El texto informal es casual y coloquial.',
    'Académico': 'El texto académico es utilizado en contextos educativos y científicos.',
    'Entusiasta': 'El texto entusiasta es energético y motivador.',
    'Positivo': 'El texto positivo se enfoca en aspectos favorables y optimistas.',
    'Expositivo': 'El texto expositivo presenta información de manera objetiva.',
    'Descriptivo': 'El texto descriptivo detalla características y atributos.',
    'Argumentativo': 'El texto argumentativo presenta opiniones respaldadas por razones.'
}

def cambiar_estilo_texto(texto, estilo):
    prompt = f'Estilo: {estilo}\nTexto: {texto}\n'
    respuesta = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=0.7
    )
    return respuesta.choices[0].text.strip()

# Configuración de la aplicación de Streamlit
st.title('Cambio de Estilo de Textos')

texto = st.text_area('Ingresa tu texto', height=200)
estilo = st.selectbox('Selecciona un estilo', list(categorias.keys()))

if st.button('Generar texto con estilo'):
    if texto:
        nuevo_texto = cambiar_estilo_texto(texto, estilo)
        st.subheader('Texto generado:')
        st.write(nuevo_texto)
    else:
        st.warning('¡Ingresa un texto antes de generar!')

# Información sobre los estilos disponibles
st.subheader('Estilos disponibles:')
for nombre, descripcion in categorias.items():
    st.write(f'**{nombre}:** {descripcion}')
