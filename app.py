#! /usr/bin/python
# -*- coding:utf-8 -*

from flask import Flask, request, render_template, redirect, url_for
from tinydb import TinyDB, Query
from slugify import slugify

db = TinyDB('db.json')
app = Flask(__name__)

'''
Projet
'''

@app.route("/")
def test_template():

    context = {
    'first':'Yeehaaa'
    }

    return render_template('test/index.html', context=context)


@app.route('/game/<int:score>')
def game(score):
   return render_template('test/int.html', score = score)

'''
ZotProjet
'''

@app.route('/form', methods = ['POST', 'GET'])
def formulaire():
    if request.method == 'POST':
        
        name = request.form.get('name')
        description = request.form.get('desc')
        slug = slugify(name)

        if name and description :
            Client = Query()
            client = db.search(Client.slug == slug)
            if len(client) == 0 :
                
                db.insert({
                    'slug': slug, 
                    'name': name,
                    'description': description,
                    })

            return redirect(f'/{slug}')

    else :
        return render_template('test/form.html')


@app.route('/<slug>')
def templater(slug):
    Client = Query()
    client = db.search(Client.slug == slug)
    if len(client) > 0 :
        return render_template('test/client.html', client=client[0])
    else :
        return redirect(url_for('formulaire'))


# flask run --reload --host=0.0.0.0