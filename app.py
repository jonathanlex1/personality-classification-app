import streamlit as st 
from processing import processing_data
from data import input_data, response_map, personalities

st.logo('asset/puzzle.png')
st.title('🔎 Personalities Classification')

def process_results():
    st.session_state['submitted'] = True
    st.session_state['responses'] = responses

def reset_session() : 
    st.session_state['submitted'] = False

if 'submitted' not in st.session_state:
    st.session_state['submitted'] = False

responses = {}

if not st.session_state['submitted'] :
    for question, response in input_data.items() : 
        st.subheader(question)
        
        response = st.radio(
            label="Select your response:",
            options=[3, 2, 1, 0, -1, -2, -3],
            format_func=lambda x: response_map[x],
            horizontal=True,
            key=f"radio_{question}"
        )

        responses[question] = response

    st.button('Result', type='primary', on_click=process_results) 
else :
    personality = processing_data(st.session_state['responses'])

    st.balloons() 
    st.header(f'Personaliti kamu adalah {personality}')
    st.subheader('Deskripsi')
    st.write(personalities[personality]['deskripsi'])
    st.subheader('Karakteristik')
    for char in personalities[personality]['karakteristik'] :
        st.markdown(f'- {char}') 

    st.button('Check Again', on_click=reset_session)
    




