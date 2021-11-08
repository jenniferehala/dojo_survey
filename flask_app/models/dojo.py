from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__(self,data):
        self.id = data["id"]
        self.name =  data["name"]
        self.location = data["location"]
        self.language = data["language"]
        self.comment = data["comment"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def save(cls,data):
        query="INSERT INTO dojos (name,location,language,comment) VALUES (%(name)s, %(location)s, %(language)s, %(comment)s);"
        return connectToMySQL("dojo_survey_schema").query_db(query,data)

    @staticmethod
    def validate_dojo(dojo):
        is_valid = True
        if len(dojo["name"]) < 1:
            flash("We need name")
            is_valid = False
        if len(dojo["location"]) < 1:
            flash("We need location")
            is_valid = False
        if len(dojo["language"]) < 1:
            flash("We need language preferred")
            is_valid = False
        if len(dojo["comment"]) < 1:
            flash("We need your comment")
            is_valid = False
        if "checkbox" not in dojo:
            flash("We need your agreemet")
            is_valid = False
        return is_valid
    
    @classmethod
    def results(cls,data):
        query="SELECT * FROM dojos WHERE id = %(id)s"
        survey = connectToMySQL("dojo_survey_schema").query_db(query,data)
        return cls(survey[0])
        
    
