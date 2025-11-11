#!/usr/bin/env python3
"""
jokes api logic

@author:
@version: 2025.11
"""

import pathlib
import random
import tomllib
from functools import cache

import pyjokes
from pyjokes.exc import CategoryNotFoundError, LanguageNotFoundError

from models import Joke
from flask import current_app

CATEGORIES=["neutral", "chuck", "any"]
FULLJOKELIST = []


class Joker:
    """
    A layer to retrieve jokes from the pyjokes package

    :raises ValueError: the dataset has not been initialized
    :raises ValueError: the language is invalid
    :raises ValueError: the category is invalid
    :raises ValueError: the joke id is invalid
    :raises ValueError: requested number of jokes is below 0
    """

    @classmethod
    def init_dataset(cls):
        """
        Initialize the dataset

        Load jokes from the `pyjokes` package into a list of jokes
        """
        # TODO: Implement this method
        languages = current_app.config.get("LANGUAGES")
        lang_list=list(languages.keys())

        #fullJokeList = []

        for lang in lang_list:
            try:
                temp_neutral = pyjokes.get_jokes(language=lang, category="neutral")
                temp_chuck = pyjokes.get_jokes(language=lang, category="chuck")
                print(f"lang: {lang}, neutral: {len(temp_neutral)}, chuck: {len(temp_chuck)}")
                for joke in temp_neutral:
                    FULLJOKELIST.append(
                        Joke(
                            language=lang,
                            category="neutral",
                            text=joke,
                        )
                    )
                for joke in temp_chuck:
                    FULLJOKELIST.append(
                        Joke(
                            language=lang,
                            category="chuck",
                            text=joke,
                        )
                    )
            except (Exception):
                pass


    @classmethod
    def get_jokes(cls, language: str = "any", category: str = "any", number: int = 0) -> list[Joke]:
        """Get all jokes in the specified language/category combination

        :param language: language of the joke
        :param category: category of the joke
        :param number: number of jokes to return, 0 to return all
        """
        # TODO: Implement this method
        if not FULLJOKELIST:
            cls.init_dataset()

        if language != "any":
            languages = current_app.config.get("LANGUAGES")
            if language not in languages:
                raise ValueError("Invalid language")
        if category != "any":
            if category not in CATEGORIES:
                raise ValueError("Invalid category")
        if number < 0:
            raise ValueError("Number of jokes cannot be below 0")
        
        result = FULLJOKELIST
        
        return result

    @classmethod
    def get_the_joke(cls, joke_id: int) -> Joke:
        """Get a specific joke by id

        :param joke_id: joke id
        """
        # TODO: Implement this method
        if not FULLJOKELIST:
            cls.init_dataset()

        if joke_id < 0 or joke_id >= len(FULLJOKELIST):
            return None
        
        return FULLJOKELIST[joke_id-1]
        
