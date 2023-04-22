from flask import Flask, request, jsonify
import openai
import os
import json

app = Flask(__name__)

openai.api_key = "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"

def generate_text(prompt):
    response = openai.Completion.create(
      engine="davinci",
      prompt=prompt,
      temperature=0.7,
      max_tokens=150,
      n = 1,
      stop=None,
    )

    return response.choices[0].text

@app.route('/chat', methods=['POST'])
def chat():
    content = request.json.get('content')
    if not content:
        return jsonify({'error': '请提供有效的请求参数'}), 400

    text = generate_text(content)

    return jsonify({'response': text})

if __name__ == "__main__":
    app.run(debug=True, port=5000)