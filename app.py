from flask import Flask, json
from flask.ext.cors import CORS

app = Flask(__name__)
cors = CORS(app)

@app.route('/.well-known/cds-services')
def discovery():
  return json.jsonify({
    'services': [
      {
        'hook': 'patient-view',
        'name': 'Static CDS Service in Python',
        'description': 'An example static CDS service in Python',
        'id': 'static',
        'prefetch': {
          'patient': 'Patient/{{Patient.id}}'
        }
      }
    ]
  })

@app.route('/cds-services/static', methods=['POST'])
def service():
  card1 = card('Success Card', 'success', link('Static CDS Service', 'http://example.com'))
  card1['detail'] = 'This is a test of a static success card.'
  card1['links'].append(link('Google', 'https://google.com'))
  card1['links'].append(link('Github', 'https://github.com'))

  source = link('Static CDS Service')

  card2 = card('Info card', 'info', source)
  card3 = card('Warning card', 'warning', source)
  card4 = card('Hard stop card', 'hard-stop', source)


  return json.jsonify({
    'cards': [card1, card2, card3, card4]
  })

def card(summary, indicator, source):
  return {
    'summary': summary, 'detail': '', 'indicator': indicator,
    'source': source, 'links': []
  }

def link(label, url=None):
  result = { 'label': label }
  if url:
    result['url'] = url

  return result

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
