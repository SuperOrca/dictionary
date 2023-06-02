from flask import render_template
import aiohttp

from app import app


@app.route("/")
async def index():
    return render_template("index.html")


@app.route("/<word>")
async def define(word: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}") as response:
            data = await response.json()
    if isinstance(data, list):
        return render_template("definition.html", word=word, data=data)
    else:
        return render_template("word_not_found.html", word=word)


@app.errorhandler(404)
def page_not_found(_):
    return render_template('404.html'), 404
