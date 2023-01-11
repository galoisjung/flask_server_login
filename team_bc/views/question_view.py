from flask import render_template, Blueprint, url_for, redirect
from flask import request
import json
from flask import Response
from flask_login import login_required

from team_bc.models.question import Question

bp = Blueprint('question', __name__, url_prefix='/board')


@bp.route('/list', methods=('GET',))
@login_required
def _list():
    question_list = Question.query.order_by(Question.create_date.desc())
    result = {}
    for i in question_list:
        dic = i.__dict__
        dic.pop('_sa_instance_state')
        dic.pop('create_date')
        result[dic["id"]] = dic

    return result


@bp.route('/create', methods=('POST',))
def create():
    dic_data = json.loads(request.data)
    subject = dic_data["subject"]
    content = dic_data["content"]
    from datetime import datetime
    q = Question(subject=subject, content=content, create_date=datetime.now())
    from team_bc import db
    db.session.add(q)
    db.session.commit()
    return Response("{'status':'200'}", status=200, mimetype='application/json')


# @bp.route('/modify', methods=('POST',))
# def modify():
#     dic_data = json.loads(request.data)
#     subject = dic_data["subject"]
#     content = dic_data["content"]
#     question_id = dic_data["id"]
#     question = Question.query.get(question_id)
#     question.subject = subject
#     question.content = content

#     from team_bc import db
#     db.session.commit()
#     return Response("{'status':'200'}", status=200, mimetype='application/json')


# @bp.route('/delete', methods=('POST',))
# def delete():
#     dic_data = json.loads(request.data)
#     question_id = dic_data["id"]
#     question = Question.query.get(question_id)
#     from team_bc import db
#     db.session.delete(question)
#     db.session.commit()
#     return Response("{'status':'200'}", status=200, mimetype='application/json')
