# -*- coding: utf-8 -*-
# Copyright © yqh
# CreateTime: 2019-12-26 11:01:11


from flask import Flask, Blueprint, jsonify, request, render_template
from flask_script import Manager
from run_main import RunMain

users_blueprint = Blueprint('interface', __name__, template_folder='testResult')


class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'CazzEqyQDBjm'


class DevConfig(BaseConfig):
    DEBUG = True


configs = {
    'dev': DevConfig,
}


def create_app():
    api = Flask(__name__)
    api_settings = configs['dev']
    api.config.from_object(api_settings)
    api.register_blueprint(users_blueprint)
    return api


@users_blueprint.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify({'status': 'success', 'message': 'auto-interface testing'})


@users_blueprint.route('/ret', methods=['get'])
def ret():
    return render_template('result.html')


@users_blueprint.route('/run', methods=['POST'])
def run_case():
    r = RunMain()
    run_ret = r.run()
    if run_ret:
        ret_data = {'status': 'success', 'message': '用例成功'}
        code = 200
    else:
        ret_data = {'status': 'failed', 'message': '执行失败'}
        code = 400
    return jsonify(ret_data), code


api = create_app()


if __name__ == '__main__':
    manager = Manager(api)
    manager.run()
