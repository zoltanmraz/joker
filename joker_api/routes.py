#!/usr/bin/env python3
"""
jokes api routes

@author:
@version: 2025.11
"""

import pyjokes
from typing import Literal

from joker.models import Joke

from .logic import Joker

from flask import Blueprint, abort, jsonify
from werkzeug import Response
from werkzeug.exceptions import NotFound

from flask import current_app

main = Blueprint("main", __name__, url_prefix="/api/v1/jokes")


@main.get("/zoli")
def hello_zoli():
    # languages = current_app.config.get("LANGUAGES")
    # lang_list=list(languages.keys())

    # fullJokeList = []

    # for lang in lang_list:
    #     try:
    #         temp_neutral = pyjokes.get_jokes(language=lang, category="neutral")
    #         temp_chuck = pyjokes.get_jokes(language=lang, category="chuck")
    #         print(f"lang: {lang}, neutral: {len(temp_neutral)}, chuck: {len(temp_chuck)}")
    #         for joke in temp_neutral:
    #             fullJokeList.append(
    #                 Joke(
    #                     language=lang,
    #                     category="neutral",
    #                     text=joke,
    #                 )
    #             )
    #         for joke in temp_chuck:
    #             fullJokeList.append(
    #                 Joke(
    #                     language=lang,
    #                     category="chuck",
    #                     text=joke,
    #                 )
    #             )
    #     except (Exception):
    #         pass


    # fullJokeList = Joker.init_dataset()
    # return jsonify(fullJokeList)

    
    
    # languages = current_app.config.get("LANGUAGES")
    # lang_list=list(languages.keys())
    # return lang_list


    # jokes =pyjokes.get_jokes()
    # return jsonify(jokes)
    
    # joke = pyjokes.get_joke()
    # return jsonify(joke)

    #5.elem
    # jokes = pyjokes.get_jokes(language="en", category="all")
    # return jokes[4]

    return "Hello Zoli!"

# @main.route("/languages")
# def get_languages():
#     languages = current_app.config.get("LANGUAGES")
#     return jsonify(languages)


@main.route("/<string:language>/<string:category>/all")
def get_all_jokes_by_language_and_category(language: str, category: str) -> Response:
    """Get all jokes in the specified language/category combination

    :param language: language of the joke
    :param category: category of the joke
    """
    # TODO: Implement this function
    jokes = Joker.get_jokes(language=language, category=category)
    return jsonify(jokes)

    


@main.route("/<string:language>/<string:category>/<int:number>")
def get_n_jokes_by_language_and_category(language: str, category: str, number: int):
    """Get multiple jokes

    :param language: language of the jokes
    :param category: category of the jokes
    :param number: number of the jokes to return
    """
    # TODO: Implement this function
    jokes = Joker.get_jokes(language=language, category=category, number=number)
    if number > len(jokes):
        return jsonify(jokes)
    else:
        return jsonify(jokes[:number])



@main.route("/<int:joke_id>")
def get_the_joke(joke_id: int):
    """Get a specific joke by id

    :param joke_id: joke id
    """
    # TODO: Implement this function
    # jokes = pyjokes.get_jokes(language="en", category="all")
    # if joke_id < 0 or joke_id >= len(jokes):
    #     # return not_found(NotFound())
    #     abort(404)
    #return jsonify(jokes[joke_id-1])
    joke = Joker.get_the_joke(joke_id)
    if joke is None:
        abort(404)
    return jsonify(joke)


@main.errorhandler(404)
def not_found(error: NotFound) -> tuple[Response, Literal[404]]:
    # TODO: Implement this function
    return jsonify({"error": "not found"}), 404

@main.errorhandler(500)
def server_error(error: Exception) -> tuple[Response, Literal[500]]:
    return jsonify({"error": "internal server error"}), 500



