from flask_restful import Resource,Api, reqparse
from flask_jwt import JWT, jwt_required
from flask import Flask,request

import sqlite3


items =[]

class Item(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float,required=True,help='Kindly enter the price field')
    
    @jwt_required()
    def get(self,name):
        item = self.find_by_item_name(name)

        if item:
            return item
        return {'message':"item not found"},404
    

    @classmethod
    def find_by_item_name(cls,name):
        connection = sqlite3.connect("data.db")

        cursor = connection.cursor()

        select_Query ="Select * from items where name=?"
        result = cursor.execute(select_Query,(name,))
        row = result.fetchone()

        connection.close()
        if row:
            return {"item":{
                "name":row[1],"price":row[2]
            }}

    
    def post(self,name):

        if self.find_by_item_name(name):
            return {"message":"Item with name '{}' already exists.".format(name)},400

        data = Item.parser.parse_args()
        item = {"name":name,"price":data["price"]}

        try:
            self.insert(item)
        except:
            return {"message":"Error occured on inserting the item"},500
        return item,201
    
    @classmethod
    def insert(Self,item):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        insert_Query ="INSERT into items values (null,?,?)"
        cursor.execute(insert_Query,(item['name'],item['price'],))
        connection.commit()
        connection.close()
    
    @classmethod
    def update(Self,item):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        update_Query ="UPDATE items SET PRICE =? WHERE NAME=?"
        cursor.execute(update_Query,(item['price'],item['name'],))
        connection.commit()
        connection.close()
    
    def delete(self,name):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        delete_Query ="DELETE FROM ITEMS WHERE NAME=?"
        cursor.execute(delete_Query,(name,))
        connection.commit()
        connection.close()
        return {'message':'Item Deleted'}

    def put(self,name):
        data = Item.parser.parse_args()
        item =self.find_by_item_name(name)

        updated_item = {'name':name,'price':data['price']}
        if item is None:
            self.insert(updated_item)
        else:
            self.update(updated_item)
        return updated_item


class ItemList(Resource):

    def get(self):
        items = self.get_all_items()
        if items:
            return items
        return {'message': "No Items Found"},404
    
    @classmethod
    def get_all_items(cls):
        items = []
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        select_Query ="Select * from items"
        result = cursor.execute(select_Query)
        for row in result:
            item = {"name":row[1],"price":row[2]}
            items.append(item)
        connection.close()
        return {'items':items}
