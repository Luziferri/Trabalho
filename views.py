from flask import render_template

def ranking_page():
    # Esta função diz ao Flask qual é o ficheiro HTML que deve abrir
    return render_template("ranking.html")