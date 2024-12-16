from dotenv import load_dotenv

from x_sandbox_2.graph.graph import app


load_dotenv()

if __name__ == "__main__":
    print("Hello Sandbox 2")
    paths = [
        "/Users/victor/myfolder/workspace-ai/x_tender_proposal/temp/tender03.pdf",
    ]
    response = app.invoke(input={"paths": paths})
