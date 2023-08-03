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

py_binary(
    name = "safe_reference_upsert",
    srcs = [
        "safe_reference_upsert.py",
    ],
    data = [
        "source_knowledge/safe_reference.txt",
    ],
    deps = [
        requirement("langchain"),
        requirement("python-dotenv"),
        requirement("openai"),
        requirement("pinecone-client"),
        requirement("tiktoken"),
    ],
)

py_binary(
    name = "scrum_guide_upsert",
    srcs = [
        "scrum_guide_upsert.py",
    ],
    data = [
        "source_knowledge/scrum_guide.md",
    ],
    deps = [
        requirement("langchain"),
        requirement("python-dotenv"),
        requirement("openai"),
        requirement("pinecone-client"),
        requirement("tiktoken"),
    ],
)
