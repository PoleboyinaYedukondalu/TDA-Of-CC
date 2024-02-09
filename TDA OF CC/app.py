from flask import Flask, render_template

app = Flask(__name__)
class index:
    @app.route('/')
    def index():
        return render_template('index.html')

class login:
    @app.route('/login')
    def login():
        return render_template("login.html")

class singup:
    @app.route('/signup', methods=['GET', 'POST'])
    def signup():
        if request.method == 'POST':
            name = request.form.get('name')
            email = request.form.get('email')
            password = request.form.get('password')

            # Example validation: checking if fields are not empty
            if not name or not email or not password:
                return render_template('signup.html', error='All fields are required!')

            # Add more validation as needed
            
            # If validation passes, redirect to another page or perform other actions
            return redirect(url_for('index'))

        return render_template('signup.html')

class about:
    @app.route('/about')
    def about():
        return render_template('about.html')

class prices:
    @app.route('/prices')
    def prices():
        return render_template('prices.html')

if __name__ == '__main__':
    app.run(debug=True)
