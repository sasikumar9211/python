import sqlite3
from flask_restful import Resource,Api, reqparse

class User:

    def __init__(self,_id,username,password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls,username):
        connection = sqlite3.connect("data.db")

        cursor = connection.cursor()

        select_Query ="Select * from users where username=?"
        result = cursor.execute(select_Query,(username,))
        row = result.fetchone()

        if row:
            user = cls(*row)
        else:
            user =None
        
        connection.close()
        return user

    

    @classmethod
    def find_by_id(cls,_id):
        connection = sqlite3.connect("data.db")

        cursor = connection.cursor()

        select_Query ="Select * from users where id=?"
        result = cursor.execute(select_Query,(_id,))
        row = result.fetchone()

        if row:
            user = cls(*row)
        else:
            user =None
        
        connection.close()
        return user

class UserRegister(Resource):

    
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str,required=True,help='Kindly enter the username field')
    parser.add_argument('password', type=str,required=True,help='Kindly enter the password field')

    def post(Self):
        data = UserRegister.parser.parse_args()

        if User.find_by_username(data['username']):
            return {"message":"User already exists with the same name"},400
        
        connection = sqlite3.connect("data.db")

        cursor = connection.cursor()
        QUERY = "INSERT INTO users values(null,?,?)"
        cursor.execute(QUERY,(data['username'],data['password']))

        connection.commit()
        connection.close()
        return {"message":"User Created Successfully"},201