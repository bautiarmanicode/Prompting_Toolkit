import streamlit as st  # Importa Streamlit con el alias estándar 'st'
from streamlit.components.v1 import html 
# import prompting  # Importa 'prompting' sin asignarle un alias

# ... (resto de tu código)

st.title("Contenido incrustado de Taskade")  # Ahora esto debería funcionar correctamente


# URL del iframe que quieres mostrar
iframe_url = "https://www.taskade.com/embed/o9Q2nz2aXmF7WddQ?as=list&share=view&view=R7sHdmVxy5RRGNvX&theme=dark&coverImageType=none"

# Código HTML para incrustar el iframe
iframe_html = f"""
<iframe 
    width="100%" 
    height="600"  # Ajusta la altura según sea necesario
    scrolling="yes" 
    frameborder="0" 
    src="{iframe_url}">
</iframe>
"""

# Muestra el iframe usando st.components.v1.html
st.title("Contenido incrustado de Taskade")
html(iframe_html, height=1200)  # Ajusta la altura según sea necesario