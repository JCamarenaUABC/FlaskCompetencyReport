from flask import g, render_template
import sqlite3

DATABASE = "catalog_db"


def get_db():
    db = getattr(g, "_database", None)
    if not db:
        db = g._databse = sqlite3.connect(DATABASE)
    return db


def output_formatter(results: tuple):
    out = {"body": []}
    for result in results:
        res_dict = {}
        res_dict["id"] = result[0]
        res_dict["name"] = result[1]
        res_dict["price"] = result[2]
        res_dict["category"] = result[3]
        out["body"].append(res_dict)
    return out


def scan():
    cursor = get_db().execute("SELECT * FROM product", ())
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)


def scantrue():
    cursor = get_db().execute("SELECT * FROM product where active=TRUE", ())
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)


def scanfalse():
    cursor = get_db().execute("SELECT * FROM product where active=FALSE", ())
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)


def read(prod_id):
    query = """SELECT * FROM product WHERE id = ?"""
    cursor = get_db().execute(query, (prod_id))
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)


def update(prod_id, fields: dict):
    field_string = ", ".join(
        "%s=\%s\"" % (key, val)
        for key, val in fields.items())

    query = """UPDATE product SET %s WHERE id = ?""" % field_string

    cursor = get_db()
    cursor.execute(query, ())
    cursor.commit()
    return True


def softdelete(prod_id, valor):

    if valor == 1:
        query = "UPDATE product SET active=FALSE WHERE id=%s" % prod_id
    else:
        query = "UPDATE product SET active=TRUE WHERE id=%s" % prod_id

    cursor = get_db()
    cursor.execute(query)
    cursor.commit()

    return query


def delete(prod_id):
    query = "DELETE FROM product WHERE id = %s" % prod_id
    cursor = get_db()
    cursor.execute(query, ())
    cursor.commit()
    return True


def create(name, price, category, description):
    value_tuple = (name, price, category, description)
    query = """
            INSERT INTO product(
                name,
                price,
                category,
                description
            ) VALUES(?,?,?,?)
            """

    cursor = get_db()
    last_row_id = cursor.execute(query, value_tuple).lastrowid
    cursor.commit()
    return last_row_id

########## FOR REVIEW
def createreview(idproduct, comment):
    value_tuple = (idproduct, comment)
    query = """
            INSERT INTO Reviews(
                idProduct,
                Comment
            ) VALUES(?,?)
            """

    cursor = get_db()
    last_row_id = cursor.execute(query, value_tuple).lastrowid
    cursor.commit()
    return last_row_id


def readreview(prod_id):
    
    query = "SELECT Comment FROM Reviews WHERE idProduct = %s" % prod_id
    cursor = get_db().execute(query, ())
    results = cursor.fetchall()
    cursor.close()

    return results#output_formatter(results)
