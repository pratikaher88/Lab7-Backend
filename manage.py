        
from celery.result import AsyncResult
from flask import render_template, Blueprint, jsonify, request, Flask

from proj.tasks import create_task, count_words_and_sleep, create_task_text

app = Flask(__name__)

@app.route('/count', methods=['POST'])
def count():
    text = request.json['text']
    task = count_words_and_sleep.delay(text)
    return jsonify({'job_id': task.id}), 202

@app.route('/status/<id>', methods=['GET'])
def status(id):
    result = AsyncResult(str(id))

    if result.ready():
        return jsonify({'result': result.get()}), 202
    else:
        return jsonify({'status': 'pending'}), 202
    

if __name__ == "__main__":
    app.run(debug=True,  host='0.0.0.0', port=5000)
