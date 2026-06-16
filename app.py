import base64
import re
import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="大咖国际销售单",
    page_icon="📋",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
      #MainMenu, footer, header { visibility: hidden; height: 0; }
      .block-container { padding: 0.5rem 1rem 1rem; max-width: 100%; }
      iframe { border: none !important; }
    </style>
    """,
    unsafe_allow_html=True,
)

BASE_DIR = Path(__file__).parent
html_path = BASE_DIR / "index.html"
if not html_path.exists():
    st.error("未找到 index.html，请把 index.html 放在与 app.py 同一目录。")
    st.stop()


def embed_fonts(html: str) -> str:
    font_path = BASE_DIR / "fonts" / "SimSun.ttf"
    if not font_path.exists():
        return html
    b64 = base64.b64encode(font_path.read_bytes()).decode("ascii")
    data_url = f"url('data:font/truetype;base64,{b64}')"
    html = html.replace("url('fonts/SimSun.ttf')", data_url)
    html = re.sub(
        r'<link rel="preload" href="fonts/SimSun\.ttf"[^>]*>\s*',
        "",
        html,
    )
    return html


html_content = embed_fonts(html_path.read_text(encoding="utf-8"))
components.html(html_content, height=1100, scrolling=True)
