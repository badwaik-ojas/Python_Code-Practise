from dotenv import load_dotenv

load_dotenv()

from graph.graph import app

if __name__ == "__main__":
    print("Hello Advanced RAG")
    print(app.invoke(input={"question": "agent system"}))


# from dotenv import load_dotenv

# load_dotenv()
# from graph.nodes.retrieve import retrieve

# dummy_state = {
#     "question": "What is agent memory??",
#     "documents": [],
#     "generation": "",
#     "web_search": False
# }

# print(retrieve(dummy_state))