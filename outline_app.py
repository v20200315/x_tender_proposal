from dotenv import load_dotenv

from x_outline.graph.graph import app


load_dotenv()

if __name__ == "__main__":
    print("Hello Tender Proposal")
    paths = [
        "/Users/victor/myfolder/workspace-ai/x_tender_proposal/temp/tender0101.pdf",
        "/Users/victor/myfolder/workspace-ai/x_tender_proposal/temp/tender0102.pdf",
    ]
    paths2 = [
        "/Users/victor/myfolder/workspace-ai/x_tender_proposal/temp/tender0201.pdf",
        "/Users/victor/myfolder/workspace-ai/x_tender_proposal/temp/tender0202.pdf",
    ]
    paths3 = [
        "/Users/victor/myfolder/workspace-ai/x_tender_proposal/temp/tender-others.pdf",
    ]
    paths4 = [
        "/Users/victor/myfolder/workspace-ai/x_tender_proposal/temp/not-a-tender.pdf",
    ]
    app.invoke(input={"paths": paths})
    # print(app.invoke(input={"paths": paths}))
