from flask import Flask, jsonify, request

questions = []

class Questions:

    def __init__(self, body, poster):
        '''questions class'''
        self._id = 0
        self.body = body
        self.poster = poster
    
    def get_poster(self):
        return self.poster
    
    def get_id(self):
        return self._id
    

    def post_question(self):
        '''post a question'''

        _id = len(questions)
        self._id = _id + 1

        new_question = {
            '_id' : self._id,
            'body' : self.body,
            'poster' : self.poster
        }

        questions.append(new_question)
        return new_question
    
    @staticmethod
    def get_a_specific_question(_id):

        _id = int(_id)
        if _id > 0 and _id <= len(questions):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
            question_data = {
                '_id': questions[_id-1]['_id'],
                'body': questions[_id-1]['body'],
                'poster': questions[_id-1]['poster']
            }
            return question_data
        else:
            return jsonify({
                'status': 'FAIL',
                'response_message': 'Question ID not found',
            }), 404

answers = []

class Answers:

    def __init__(self, response, username):
        self.answer_id = 0
        self.response = response
        self.username = username
    
    def get_answer_id(self):
        return self.answer_id
    
    def get_username(self):
        return self.username
    
    def post_answer(self):
        '''post an answer to a question'''

        answer_id = len(answers)
        self.answer_id = answer_id + 1

        answer = {
            'answer_id' : self.answer_id,
            'response' : self.response,
            'username' : self.username
        }

        answers.append(answer)
        return answer