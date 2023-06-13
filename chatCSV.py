import streamlit as st
import openai
import os
from langchain.agents import create_csv_agent
from langchain.llms import AzureOpenAI
from dotenv import load_dotenv

load_dotenv() 

openai.api_type = "azure"
openai.api_base = "https://gpt-poc-vd.openai.azure.com/"
openai.api_version = "2022-12-01"
openai.api_key = os.getenv("OPENAI_API_KEY")

def main():
    st.set_page_config(page_title='Ask your CSV')
    st.header("Ask your CSV")

    user_csv = st.file_uploader("Upload your csv file", type='csv')
    print(user_csv.name)

    if user_csv is not None:
        user_question = st.text_input("Ask a question about your CSV: ")
        llm = AzureOpenAI(deployment_name="text-davinci-003", 
                          model_name="text-davinci-003", temperature=0)

        agent = create_csv_agent(llm, "data.csv", verbose=True)
        print("this is agent ", agent)
        if user_question and user_question != "":
            response = agent.run(user_question)
            st.write(response)


if __name__ == "__main__":
    main()
