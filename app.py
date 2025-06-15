from dotenv import load_dotenv
import os
load_dotenv() ##Load environment variables from .env file
import sqlite3
import streamlit as st
import google.generativeai as genai
from collections import deque
# from st_chat_message import message

##Configure the Google Generative AI API key
genai.configure(api_key=os.getenv("GOOGLE_GENERATIVE_AI_API_KEY"))
st.set_page_config(page_title="Retrieving any SQL Query")
 ## Streamlit app
st.title("Retrieving any SQL Query")
st.header("Google Gemini AI to retrieve data from SQL Database")
# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
if 'context' not in st.session_state:
    st.session_state.context = deque(maxlen=10)  ##Initialize the conversation context length to 10
# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
##Function to load Google Gemini AI Model and provide SQL query as response
def get_gemini_response(question, prompt):
    model=genai.GenerativeModel('gemini-1.5-flash-latest')
    context_text = "\n".join(
    [f"User: {entry['question']}\nAssistant: {entry['answer']}" for entry in st.session_state.context]
    )
    response = model.generate_content(f"{prompt}\n{context_text}\nUser: {question}")
    return response.text

##Function to retrieve data based on the SQL query from student.db
def read_sql_query(sql_query,db):
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    cursor.execute(sql_query)
    data = cursor.fetchall()
    connection.commit()
    connection.close()
    return data

##Convert the retrieved data into a readable format
def format_data(data,prompt,question):
    model=genai.GenerativeModel('gemini-1.5-flash-latest')
    formatted_data = model.generate_content(f"{prompt}\n{data}\n{question}")
    return formatted_data.text

def add_to_conversation(question, answer):
    st.session_state.context.append({"question": question, "answer": answer})

##Define the Prompt
prompt1=[
    '''
        You are an assistant that converts English questions into SQL queries. The context parameter is a list of previous questions and answers, which you can use to maintain the conversation context. If the user refers for something present in previous conversation, keep in mind that the most recent entry in the context list is the most recent message added in the list.
        The SQL queries should be compatible with SQLite.
        The database is `student.db` and contains a single table:

        STUDENT(
            NAME       VARCHAR(25),
            CLASS      VARCHAR(25),
            ROLL_NO    INT PRIMARY KEY,
            SECTION    VARCHAR(25),
            MARKS      INT
        );

        When you receive a user request in plain English, output only the SQL query without any additional formatting, explanations, or code block markers. Ensure that the query is syntactically correct and ready for execution in SQLite.

        Examples:

        # 1. Get all columns for every student
        English: "Show me every student record."
        SQL:
        SELECT * FROM STUDENT;

        # 2. Find students in section A
        English: "List the names and roll numbers of students in section A."
        SQL:
        SELECT NAME, ROLL_NO FROM STUDENT WHERE SECTION = 'A';

        # 3. Top scorers
        English: "Which students scored more than 90 marks?"
        SQL:
        SELECT NAME, MARKS FROM STUDENT WHERE MARKS > 90;

        # 4. Count by class
        English: "How many students are there in each class?"
        SQL:
        SELECT CLASS, COUNT(*) AS student_count FROM STUDENT GROUP BY CLASS;

        # 5. Specific student lookup
        English: "Give me all details for the student with roll number 312."
        SQL:
        SELECT * FROM STUDENT WHERE ROLL_NO = 312;

        ---

        Now, translate the following English request into an SQL query:


    '''
]
prompt2=[
    '''
        You are an assistant that transforms genearted SQL results into natural language responses or tables with taking into consideration the question provided by user, so that the formatted answer sounds like the solution of the provided query in a single sentence.
        The SQL result can be a single row, multiple rows, or no rows. Your response should be clear and concise.

        Now, based on the user's question and the SQL query result provided, generate a natural language response:
    '''
]

# Display chat history (older messages stay on screen)
# for i, entry in enumerate(st.session_state.context):
#     message(entry["question"], is_user=True, key=f"user_{i}")
#     message(entry["answer"], is_user=False, key=f"bot_{i}")

def submit_button(question):
    response=get_gemini_response(question, prompt1)
    print("SQL Query:")
    print(response)
    data=read_sql_query(response,"student.db")
    for row in data:
        print(row)
    formatted_data=format_data(data, prompt2, question)
    print(formatted_data)
    add_to_conversation(question, formatted_data)
    print("Conversation Context:")
    for idx, entry in enumerate(st.session_state.context):
        print(f"{idx+1}. User: {entry['question']}")
        print(f"   Assistant: {entry['answer']}")
    return formatted_data

# with st.container():
#     question = st.text_input("Enter your question:", key="input")
#     submit=st.button("Ask the question")
#     if submit and question:
#         submit_button(question)

if question := st.chat_input("Enter your question:"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": question})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(question)
    with st.chat_message("assistant"):
        stream =submit_button(question)  ##Call the function to get the SQL query and retrieve data from the database
        st.write(stream)
    st.session_state.messages.append({"role": "assistant", "content": stream})
    for idx, entry in enumerate(st.session_state.messages):
        print("***")
        print(f"{entry['content']}")