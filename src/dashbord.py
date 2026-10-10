import streamlit as st
from src.main import RandomPasswordGenerator, MemorablePasswordGenerator, PinCodeGenerator

st.image("https://images.ctfassets.net/lzny33ho1g45/password-security-p-img/72f3ab78724796a0990219ee8ed495c7/file.png?fm=webp&q=31&fit=thumb&w=1520&h=760")
st.title("Password Generator :key:")

option = st.radio(
    "Select a password generator method",
    ("Random Password", "Memorable Password", "Pin Code")
)

if option == "Random Password":
    length = st.slider("Select the lenght of the Random Password character", 8, 16)
    include_number = st.toggle("Include Numbers")
    include_symbols = st.toggle("Include Symbole")

    generator = RandomPasswordGenerator(length, include_number, include_symbols)


elif option == "Memorable Password":
    no_of_words = st.slider("Select the numbers of words", 4, 9)
    separator = st.selectbox("Select a Separator", ("/", "_", "-", "*"))
    capitalization = st.toggle("capitalization")

    generator = MemorablePasswordGenerator(no_of_words, separator, capitalization)


elif option == "Pin Code":
    length = st.slider("Select the lenght of the Pin Code", 4, 16)

    generator = PinCodeGenerator(length)


password = generator.generate()
st.write(fr"Pin Code: ``` {password} ``` ")
