class ModelUser():

    def login(self, db, user):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT UsuId, UsuNombre, UsuCedula, UsuClave FROM tblusuario WHERE UsuCedula={} and UsuClave={}".format(user.cedula,user.password)
            cursor.execute(sql)
            row = cursor.fetchone()

            if row > 0:
                user = user(row[0], row[2], row[3])
            else:
                return 0
        except Exception as ex:
            raise Exception(ex)