from dotenv import load_dotenv

from x_sandbox.graph.graph import app


load_dotenv()

if __name__ == "__main__":
    print("Hello Sandbox")
    paths = [
        "/Users/victor/myfolder/workspace-ai/x_tender_proposal/temp/tender02.pdf",
    ]
    response = app.invoke(input={"paths": paths})
    print(response["outline"])
