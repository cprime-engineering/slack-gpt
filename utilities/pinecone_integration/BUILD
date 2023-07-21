load("@pip//:requirements.bzl", "requirement")

py_binary(
    name = "cprime_case_studies_upsert",
    srcs = [
        "cprime_case_studies_upsert.py",
    ],
    data = [
        "source_knowledge/cprime_case_studies.txt",
    ],
    deps = [
        requirement("langchain"),
        requirement("python-dotenv"),
        requirement("openai"),
        requirement("pinecone-client"),
        requirement("tiktoken"),
    ],
)
