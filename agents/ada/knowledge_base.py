import pandas as pd

client_data = pd.read_json('agents/ada/source_knowledge/legends_of_computer_science.json')


def get_data():
    return client_data