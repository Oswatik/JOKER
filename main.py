from typing import List
from fastapi import FastAPI
from langchain_community.llms import Ollama

llm = Ollama(model="llama2")
from langchain.output_parsers import CommaSeparatedListOutputParser
from langchain.prompts import PromptTemplate
from langserve import add_routes
import uvicorn


template = PromptTemplate.from_template("Tell me a joke about {topic}.")

chain = template | llm | CommaSeparatedListOutputParser()

app = FastAPI(title="LangChain")

add_routes(app, chain, path="/chain")

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=9001)