import streamlit as st
import pandas as pd

# Load the Excel file
df = pd.read_excel('MATNR.xlsx')
matnr = df['MATNR'].to_list()

# App Title
st.title("盤點")
st.write("請填入以下內容:")

# Form for Survey
with st.form("survey_form"):
    # Create a dictionary to store responses
    responses = []

    for m in matnr:
        # Each item's input fields
        place = st.text_input(f"{m}在哪個儲位？", key=f"place_{m}")
        num = st.number_input(f"{m}有多少量?", min_value=1, max_value=120, key=f"num_{m}")
        
        # Append responses as a dictionary (optional until submission)
        responses.append({"MATNR": m, "Place": place, "Quantity": num})
    
    # Submit button
    submitted = st.form_submit_button("確認")

    if submitted:
        # On submit, display all collected responses
        st.success("謝謝!")
        # st.write("### Your Responses")
        # for response in responses:
        #     st.write(f"**{response['MATNR']}**: 儲位在 {response['Place']}, 數量為 {response['Quantity']}")
        
        # 回傳結果
        responses_df = pd.DataFrame(responses)
        st.write("### Responses Table")
        st.dataframe(responses_df)
