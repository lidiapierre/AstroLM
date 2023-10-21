import streamlit as st
from langchain.llms import OpenAI
from langchain.memory import ConversationBufferWindowMemory
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv

load_dotenv()

ft_model = 'davinci:ft-personal-2023-10-21-08-49-58'

llm = OpenAI(
    temperature=0.5,
    # model_name=ft_model
)

template = "Today for {sign}"
prompt = PromptTemplate(template=template, input_variables=["sign"])
llm_chain = LLMChain(prompt=prompt, llm=llm)

memory = ConversationBufferWindowMemory(
    memory_key="chat_history",
    k=5,
    return_messages=True,
    output_key="output"
)


def hide_streamlit_header_footer():
    hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            #root > div:nth-child(1) > div > div > div > div > section > div {padding-top: 0rem;}
            </style>
            """
    st.markdown(hide_st_style, unsafe_allow_html=True)


def add_bg():
    st.markdown(
        f"""
    <style>
    .stApp {{
        background-image: linear-gradient(rgba(234, 212, 251, 0.8), white);
        background-size: cover
    }}
    </style>
    """,
        unsafe_allow_html=True
    )


def main():
    hide_streamlit_header_footer()
    add_bg()
    st.markdown("<h1 style='text-align: center;'>AstroLM 🔮</h1>", unsafe_allow_html=True)

    sign = ""

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("Aries ♈️"):
            sign = "Aries"
    with col2:
        if st.button("Taurus ♉️"):
            sign = "Taurus"
    with col3:
        if st.button("Gemini ♊️"):
            sign = "Gemini"
    with col4:
        if st.button("Cancer ♋️"):
            sign = "Cancer"

    col5, col6, col7, col8 = st.columns(4)
    with col5:
        if st.button("Leo ♌️"):
            sign = "Leo"
    with col6:
        if st.button("Virgo ♍️️"):
            sign = "Virgo"
    with col7:
        if st.button("Libra ♎️"):
            sign = "Libra"
    with col8:
        if st.button("Scorpio     ♏️"):
            sign = "Scorpio"

    col9, col10, col11, col12 = st.columns(4)
    with col9:
        if st.button("Sagittarius ♐️"):
            sign = "Sagittarius"
    with col10:
        if st.button("Capricorn ♑️️"):
            sign = "Capricorn"
    with col11:
        if st.button("Aquarius ♒️"):
            sign = "Aquarius"
    with col12:
        if st.button("Pisces ♓️"):
            sign = "Pisces"

    if sign:
        res = llm_chain.run(sign)
        st.markdown(f"## {res}")


if __name__ == "__main__":
    main()
