from app import app
from sql.controllers import generic_query as q


@app.route('/<table>_<row>=<id>')
def get_table(table, row, id):
    query = f'SELECT * FROM {table} where {row} = {id}'
    fetched = q.query_db(query)
    return str(fetched)


@app.route('/')
def si():
    # return 'SI'
    return '<button id="b" style="text-align: center; margin: 50px; padding: 10px;" onclick="alert(\'EL ª-LAN subneteo\');"> Has descubierto el easter egg papu</button>'


#tenerlo al final  para que jale todo :v
app.run(host='0.0.0.0', debug=True, port=80)
