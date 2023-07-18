load("@pip//:requirements.bzl", "requirement")

py_binary(
    name = "pinecone_vector_store",
    srcs = [
        "pinecone_vector_store.py",
    ],
    data = [
        "source_knowledge/savings_accounts.txt",
    ],
    deps = [
        "//domain:domain",
        requirement("python-dotenv"),
        requirement("langchain"),
        requirement("openai"),
        requirement("pinecone-client"),
        requirement("tiktoken"),
    ],
)
