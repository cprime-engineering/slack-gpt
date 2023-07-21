load("@pip//:requirements.bzl", "requirement")

py_binary(
    name = "savings_accounts_upsert",
    srcs = [
        "savings_accounts_upsert.py",
    ],
    data = [
        "source_knowledge/savings_accounts.txt",
    ],
    deps = [
        requirement("langchain"),
        requirement("python-dotenv"),
        requirement("openai"),
        requirement("pinecone-client"),
        requirement("tiktoken"),
    ],
)
