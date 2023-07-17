import pandas as pd
import tiktoken
from langchain.text_splitter import RecursiveCharacterTextSplitter

tokenizer = tiktoken.get_encoding('p50k_base')

def tiktoken_len(text):
    tokens = tokenizer.encode(
        text,
        disallowed_special=()
        )
    return len(tokens)

legend_data = pd.read_json('agents/ada/source_knowledge/legends_of_computer_science.json')

def get_data():
    return legend_data


text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=400,
    chunk_overlap=20,
    length_function=tiktoken_len,
    separators=["\n\n", "\n", " ", ""]
    )

data_frame = pd.DataFrame(get_data())

chunks = text_splitter.split_text(data_frame.iloc[0][0]['description'])[:3]

def get_chunks():
    return chunks

