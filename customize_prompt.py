from langchain.prompts.prompt import PromptTemplate

_DEFAULT_TEMPLATE = """Given an input question, first create a syntactically correct dialect query to run, then look at the results of the query and return the answer.
Use the following format:

Question: "Question here"
SQLQuery: "SQL Query to run"
SQLResult: "Result of the SQLQuery"
Answer: "Final answer here"

Only use the following tables:

{name_of_table}
{table_info}

If someone asks for the table foobar, they really mean the employee table.

Question: {input}"""
PROMPT = PromptTemplate(
    input_variables=["input", "table_info", "name_of_table"], template=_DEFAULT_TEMPLATE
)

#Test input variables
PROMPT.format(
    input="hello",
    table_info="about salary",
    name_of_table="ds salary",
)


if __name__ == "__main__":
    print(PROMPT)
    print(type(PROMPT))