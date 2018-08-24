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
            'status':'ok',
            '_id': new_question.get_id()
        }), 201
    except:
        return jsonify({
            'message': 'Invalid input data',
            'status': 'fail'
        })

@app.route('/api/v1/questions/<questionId>/answers', methods = ['POST'])
def add_answer(questionId):
    try:
        question = questions[int(questionId) - 1]  # to access a question by its index
    except:
        return jsonify({
            'status': 'FAIL',
            'response_message': 'Question ID not found',
        }), 404
    answer_data = request.get_json()
    try:
        validate({
            "response": answer_data["response"],
            "username": answer_data["username"]}, answer_schema)
        new_answer = Answers(answer_data['response'], answer_data['username'])
        new_answer.post_answer()
        return jsonify({
            'message': 'Question answered',
            'status': 'ok',
            'id': new_answer.get_answer_id()
        }), 201
    except:
        return jsonify({
            'message': 'Invalid input data',
            'status': 'fail'
        })

@app.route('/api/v1/questions', methods = ['GET'])
def get_questions():
    if len(questions) >= 1:
        return jsonify({
            'message': ' Below are the Posted questions',
            'questions': questions
        })
    else:
        return jsonify({
            'message': 'There are no questions posted yet',
            'status': 'fail'
        })
