import json

from flask import Flask, jsonify, url_for

import pyslurm

with open('config.json') as f_config:
    srv_config = json.load(f_config)
app = Flask(__name__)

config = pyslurm.config()
job = pyslurm.job()
node = pyslurm.node()
partition = pyslurm.partition()
statistics = pyslurm.statistics()


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/api')
def get_apis():
    apis = [
        url_for('get_configs'),
        url_for('get_jobs'),
        url_for('get_nodes'),
        url_for('get_partitions'),
        url_for('get_statistics')
    ]
    return jsonify(apis)


@app.route('/api/configs')
def get_configs():
    return jsonify(config.get())


@app.route('/api/jobs')
def get_jobs():
    return jsonify(job.get())


@app.route('/api/nodes')
def get_nodes():
    return jsonify(node.get())


@app.route('/api/partitions')
def get_partitions():
    return jsonify(partition.get())


@app.route('/api/statistics')
def get_statistics():
    return jsonify(statistics.get())


if __name__ == '__main__':
    app.run(host=srv_config['server']['host'], port=srv_config['server']['port'])
