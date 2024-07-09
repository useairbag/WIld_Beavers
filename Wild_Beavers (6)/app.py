from flask import Flask, render_template, request, redirect, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, Email

app = Flask(__name__)
app.config["SECRET_KEY"] = "johnny"

users = {}
saved_songs = []
reviews = []

class RegistrationForm(FlaskForm):
    username = StringField("Ім'я", validators=[InputRequired(), Length(min=4, max=20)])
    email = StringField('Пошта', validators=[Email(), Length(min=4, max=50)])
    password = PasswordField('Пароль', validators=[InputRequired(), Length(min=6, max=20)])
    submit = SubmitField('Відправити')

@app.route('/Wild_Beavers')
def index():
    return render_template('main.html')   

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users:
            return render_template('signup.html', message="Це ім'я користувача вже існує. Будь ласка, оберіть інше")
        else:
            users[username] = password
            return redirect('/login')
    return render_template('signup.html', message='')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            return redirect('/Wild_Beavers')
        else:
            return render_template('login.html', message="Неправильне ім'я користувача або пароль")
    return render_template('login.html', message='')

@app.route('/classic')
def classic():
    songs = [
        {"artist": "Ludwig van Beethoven", "title": "Moonlight Sonata", "file": "betkhoven-lunnaja-sonata.mp3"},
        {"artist": "Antonio Vivaldi", "title": "Four Seasons(Autumn)", "file": "vivaldi-vremena-goda-osen.mp3"},
        {"artist": "Pyotr Tchaikovsky", "title": "Swan Lake.Scene", "file": "lebedinoe ozero.mp3"},
        {"artist": "Wolfgang Amadeus Mozart", "title": "Symphony No. 40", "file": "mocart-simfonija-40.mp3"},
        {"artist": "Johann Sebastian Bach", "title": "Air On The G String", "file": "bakh-air.mp3"}
    ]
    query = request.args.get('search')
    if query:
        songs = [song for song in songs if query.lower() in song['artist'].lower() or query.lower() in song['title'].lower()]
    return render_template('classic.html', songs=songs)

@app.route('/hiphop')
def hip_hop():
    songs = [
        {"artist": "Nujabes", "title": "Feather (feat. Cise Star, Akin)", "file": "Nujabes-Feather.mp3"},
        {"artist": "Kanye West", "title": "POWER", "file": "Kanye West Power.mp3"},
        {"artist": "Kendrick Lamar", "title": "Swimming Pools (Drank)", "file": "Kendrick Lamar – Swimming Pools (Drank).mp3"},
        {"artist": "Tyler, The Creator", "title": "See You Again (feat. Kali Uchis)", "file": "Tyler, The Creator-See You Again (Ft. Kali Uchis).mp3"},
        {"artist": "Wu-Tang Clan", "title": "C.R.E.A.M.", "file": "wu-tang_clan_-_cream_(muztune.me).mp3"}
    ]
    query = request.args.get('search')
    if query:
        songs = [song for song in songs if query.lower() in song['artist'].lower() or query.lower() in song['title'].lower()]
    return render_template('hiphop.html', songs=songs)

@app.route('/electronic')
def electronic():
    songs = [
        {"artist": "Aphex Twin", "title": "Windowlicker", "file": "climax_12 Aphex Twin - Windowlicker.mp3"},
        {"artist": "The Prodigy", "title": "Breathe", "file": "The Prodigy - Breathe.mp3"},
        {"artist": "Sweet Trip", "title": "Pro: Lov: Ad", "file": "Sweet Trip Pro_ Lov_ Ad.mp3"},
        {"artist": "Sewerslvt", "title": "Cyberia Lyr1", "file": "Sewerslvt_-_Cyberia_lyr1_(SkySound.cc).mp3"},
        {"artist": "Boards of Canada", "title": "Olson.", "file": "Boards_Of_Canada_-_Olson_(patefon.org).mp3"}
    ]
    query = request.args.get('search')
    if query:
        songs = [song for song in songs if query.lower() in song['artist'].lower() or query.lower() in song['title'].lower()]
    return render_template('electronic.html', songs=songs)

@app.route('/pop')
def pop():
    songs = [
        {"artist": "Inna", "title": "Up (feat. Sean Paul)", "file": "Inna - Up (feat. Sean Paul).mp3"},
        {"artist": "Olivia Addams", "title": "Stranger", "file": "Olivia Addams - Stranger.mp3"},
        {"artist": "Roxen", "title": "Escape", "file": "Roxen - Escape.mp3"},
        {"artist": "wrs", "title": "Llamame", "file": "WRS - Llamame.mp3"},
        {"artist": "Minelli", "title": "Illusion", "file": "Minelli - Illusion.mp3"},
    ]
    query = request.args.get('search')
    if query:
        songs = [song for song in songs if query.lower() in song['artist'].lower() or query.lower() in song['title'].lower()]
    return render_template('pop.html', songs=songs)

@app.route('/rock')
def rock():
    songs = [
        {"artist": "Nirvana", "title": "Smells Like Teen Spirit", "file": "Nirvana - Smells Like Teen Spirit .mp3"},
        {"artist": "Linkin Park", "title": "Numb", "file": "Linkin Park - Numb.mp3"},
        {"artist": "Guns N' Roses", "title": "November Rain", "file": "Guns N Roses - November Rain.mp3"},
        {"artist": "Green Day", "title": "Boulevard Of Broken Dreams", "file": "Green Day - Boulevard Of Broken Dreams.mp3"},
        {"artist": "AC-DC", "title": "Highway To Hell", "file": "AC-DC - Highway To Hell.mp3"},
    ]
    query = request.args.get('search')
    if query:
        songs = [song for song in songs if query.lower() in song['artist'].lower() or query.lower() in song['title'].lower()]
    return render_template('rock.html', songs=songs)

@app.route('/jazz')
def jazz():
    songs = [
        {"artist": "Dave Brubeck", "title": "Take Five", "file": "Dave Brubeck - Take Five.mp3"},
        {"artist": "Frank Sinatra", "title": "Strangers In The Night", "file": "Frank Sinatra - Strangers In The Night.mp3"},
        {"artist": "Louis Armstrong", "title": "What A Wonderful World", "file": "Louis Armstrong - What A Wonderful World.mp3"},
        {"artist": "James Brown", "title": "I Got You (I Feel Good)", "file": "James Brown - I Got You (I Feel Good).mp3"},
        {"artist": "The Platters", "title": "Only You (And You Alone)", "file": "The Platters - Only You (And You Alone).mp3"},
    ]
    query = request.args.get('search')
    if query:
        songs = [song for song in songs if query.lower() in song['artist'].lower() or query.lower() in song['title'].lower()]
    return render_template('jazz.html', songs=songs)

@app.route('/review')
def rev():
    return render_template('reviews.html', reviews=reviews)

@app.route('/submit_review', methods=['POST'])
def submit_reviews():
    name = request.form['name']
    review = request.form['review']
    reviews.append({'name': name, 'review': review})
    return redirect('/review_submitted')

@app.route('/review_submitted')
def reviews_submitted():
    return render_template('submit.html', reviews=reviews)


@app.route('/save_song', methods=['POST'])
def save_song():
    song_data = request.json
    saved_songs.append(song_data)
    return jsonify({"message": "Song added to saved songs!"}), 200

@app.route('/saved_songs')
def show_saved_songs():
    return render_template('saved_songs.html', songs=saved_songs)

if __name__ == "__main__":
    app.run(debug=True)