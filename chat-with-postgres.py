from langchain import OpenAI, SQLDatabase, SQLDatabaseChain
import os
from dotenv import load_dotenv

load_dotenv()

# Accessing the OPENAI KEY
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
DBUSER = os.getenv('DBUSER')
DATABASE = os.getenv('DATABASE')
DBPASS = os.getenv('DBPASS')

# Setup database
db = SQLDatabase.from_uri(
    f"postgresql+psycopg2://{DBUSER}:{DBPASS}@localhost:5432/{DATABASE}",
)

# setup llm
llm = OpenAI(temperature=0, openai_api_key=OPENAI_API_KEY)

# Create db chain
QUERY = """
Given an input question, first create a syntactically correct postgresql query to run, then look at the results of the query and return the answer.
Use the following format:

Question: Question here
SQLQuery: SQL Query to run
SQLResult: Result of the SQLQuery
Answer: Final answer here

{question}
"""

# Setup the database chain
db_chain = SQLDatabaseChain(llm=llm, database=db, verbose=True)


def get_prompt():
    print("Type 'exit' to quit")

    while True:
        prompt = input("Enter a prompt: ")

        if prompt.lower() == 'exit':
            print('Exiting...')
            break
        else:
            try:
                question = QUERY.format(question=prompt)
                print(db_chain.run(question))
            except Exception as e:
                print(e)


if __name__ == '__main__':
    get_prompt()