from flask import Flask, Response,request, jsonify, stream_with_context, request
import os
os.environ["TOGETHER_API_KEY"] = "621*ce36aadcb06*35436e7d6*bbc18b354d8140*6e805db485d70ecff*481d0"

app = Flask(__name__)
from langchain_together import ChatTogether

chat = ChatTogether(
    # together_api_key="YOUR_API_KEY",
    model="meta-llama/Llama-3-70b-chat-hf",)

def ans_ans(query):  
    for m in chat.stream(query):
        print(m.content)
        yield m.content

# query endpoint
@app.route("/hi", methods=["POST"])
def hi():
    query = request.json.get("query")
    return Response(ans_ans(query), mimetype='text/event-stream')


# Run the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("3012"), debug=True)
