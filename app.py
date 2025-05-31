from flask import Flask, redirect, url_for, request, render_template_string

app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
    return f'welcome {name}'

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form.get('nm')
        return redirect(url_for('success', name=user))
    elif request.method == 'GET':
        user = request.args.get('nm')
        if user:
            return redirect(url_for('success', name=user))
        # No name provided → return HTML form
        return '''
        <form action="/login" method="post">
            <p>Enter Name:</p>
            <input type="text" name="nm" required />
            <input type="submit" value="Submit" />
        </form>
        '''

if __name__ == '__main__':
    app.run(debug=True)
