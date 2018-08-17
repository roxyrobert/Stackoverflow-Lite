from flask import Flask, jsonify, request
from jsonschema import validate
from .models import Questions, Answers, questions, answers
from .validators import question_schema, answer_schema
from api import app

@app.route('/api/v1/questions', methods = ['POST'])
def add_question():
    question_data = request.get_json()
    try:
        validate({
            "body": question_data["body"],
            "poster": question_data["poster"]}, question_schema)
        new_question = Questions(question_data['body'], question_data['poster'])
        new_question.post_question()
        return jsonify({
            'message':'Posted question successfully',
            'status':'success'
        }), 201
    except:
        return jsonify({
            'message': 'Invalid input data',
            'status': 'fail'
        })