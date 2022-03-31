from os import error
from connect_db import connect

RESPONSE_BODY = {"current_zone": "Occidente", "current_category": "Todas"}

def getZonesNames():
    clean_response_body({"zones":[], "current_zone":RESPONSE_BODY["current_zone"], "current_category":RESPONSE_BODY["current_category"]})
    sql = "SELECT N_NOMBRE_ZONA FROM ZONA"
    conexion = connect()
    for zone in conexion.sentenciaCompuesta(sql):
        RESPONSE_BODY["zones"] += zone
    conexion.close()
    return RESPONSE_BODY


def getCategoriesNames():
    clean_response_body({"categories":[], "current_zone":RESPONSE_BODY["current_zone"], "current_category":RESPONSE_BODY["current_category"]})
    sql = "SELECT N_NOMCATEGORIA FROM CATEGORIA"
    conexion = connect()
    for category in conexion.sentenciaCompuesta(sql):
        RESPONSE_BODY["categories"] += category
    conexion.close()
    return RESPONSE_BODY


def getProductsWhitPrice():
    clean_response_body({"products":[], "current_zone":RESPONSE_BODY["current_zone"], "current_category":RESPONSE_BODY["current_category"]})
    sql1 = "SELECT PR.N_NOMPRODUCTO, I.V_PRECIO_UNIDAD, I.Q_ENEXISTENCIA FROM ZONA Z, PRODUCTO PR, INVENTARIO I "
    sql2 = "WHERE UPPER(Z.N_NOMBRE_ZONA)=\'" + RESPONSE_BODY["current_zone"].upper() + "\' AND I.K_ZONA=Z.K_ZONA AND I.K_PRODUCTO=PR.K_PRODUCTO"
    print(sql1+sql2)
    conexion = connect()
    for name, price, unit in conexion.sentenciaCompuesta(sql1 + sql2):
        RESPONSE_BODY["products"] += {"name": name, "price": price, "unit": unit}
    conexion.close()
    return RESPONSE_BODY


def getProductsWhitPriceOfOneCategory(category_name):
    clean_response_body({"products":[], "current_zone":RESPONSE_BODY["current_zone"], "current_category":category_name})
    sql1 = "SELECT PR.N_NOMPRODUCTO, I.V_PRECIO_UNIDAD, I.Q_ENEXISTENCIA FROM ZONA Z, PRODUCTO PR, INVENTARIO I, CATEGORIA C WHERE "
    sql2 = "UPPER(Z.N_NOMBRE_ZONA)= \'" + RESPONSE_BODY["current_zone"].upper() + "\' AND I.K_ZONA=Z.K_ZONA AND I.K_PRODUCTO=PR.K_PRODUCTO"
    sql3 = "AND UPPER(C.N_NOMCATEGORIA) = \'" + category_name.upper() + "\' AND PR.K_CATEGORIA = C.K_CATEGORIA"
    conexion = connect()
    for name, price, quantity in conexion.sentenciaCompuesta(sql1 + sql2 + sql3):
        RESPONSE_BODY["products"] += {"name": name, "price": price, "unit": quantity}
    conexion.close()
    return RESPONSE_BODY


def getProductByID(id_product):
    clean_response_body({"categories":[], "current_zone":RESPONSE_BODY["current_zone"]})
    conexion = connect()
    sql1 = "SELECT pr.k_producto, pr.n_nomproducto, i.v_precio_unidad FROM PAIS p, REGION r, PRODUCTO pr, INVENTARIO i WHERE UPPER(p.n_nombre_pais) "
    sql2 = "=\'COLOMBIA\' AND p.k_pais=r.K_pais AND UPPER(r.n_nombre_region)= \'" + RESPONSE_BODY[
        "current_region"].upper() + "\' AND i.k_pais=r.K_pais AND i.k_region=r.k_region"
    sql3 = " AND i.k_producto=pr.k_producto AND pr.k_producto=" + str(id_product)
    for id, name, price in conexion.sentenciaCompuesta(sql1 + sql2 + sql3):
        RESPONSE_BODY["message"] = "SUCCESFULL"
        RESPONSE_BODY["data"] += {"id": id, "name": name, "price": price},
    conexion.close()
    return RESPONSE_BODY


def getOrdersOfCliente(type_id, id_client):
    clean_response_body({"orders":[], "current_user": ""})
    sql = "SELECT C.N_NOMBRE, C.N_APELLIDO, P.K_PEDIDO, P.F_LLEGADA, P.I_ESTADO, Q_VALORT from PEDIDO P, CLIENTE C where P.Q_IDENTIFICACION_CLI = "
    sql2 = str(id_client) + " AND P.I_TIPOID_CLI = " + str(type_id) + "AND P.I_TIPOID_CLI = C.K_TIPOID AND C.K_IDENTIFICACION = P.Q_IDENTIFICACION_CLI"
    conexion = connect()
    for nombre, appellido, pedido, fecha, estado, valor in conexion.sentenciaCompuesta(sql + sql2):
        RESPONSE_BODY["current_user"] = nombre + " " + appellido
        RESPONSE_BODY["orders"] += {"id": pedido, "date": fecha, "status": estado, "price": valor}
    conexion.close()
    return RESPONSE_BODY


def getProductsOfAllCategory():
    RESPONSE_BODY["current_category"] = "TODAS"
    getAllCategoriesNames()
    getProductsWhitPrice()
    return RESPONSE_BODY


def getProductsOfDeterminateCategory(category_name):
    RESPONSE_BODY["current_category"] = category_name.upper()
    getAllCategoriesNames()
    getProductsWhitPriceOfOneCategory(category_name)
    return RESPONSE_BODY


def clean_response_body(information):
    global RESPONSE_BODY
    RESPONSE_BODY = information
    return RESPONSE_BODY


def carrito():
    conexion = connect()
    consulta1 = []
    consulta2 = []
    consulta3 = []
    # SELECT pr.n_nomproducto, i.v_precio_unidad FROM PAIS p, REGION r, PRODUCTO pr, INVENTARIO i WHERE UPPER(p.n_nombre_pais)='COLOMBIA' AND p.k_pais=r.K_pais AND UPPER(r.n_nombre_region)='CARIBE' AND i.k_pais=r.K_pais AND i.k_region=r.k_region AND i.k_producto=pr.k_producto
    for datos in conexion.sentenciaCompuesta(
            " SELECT  pr.n_nomproducto, i.v_precio_unidad, i.K_PRODUCTO FROM PAIS p, REGION r, PRODUCTO pr, INVENTARIO i WHERE UPPER(p.n_nombre_pais)='COLOMBIA' AND p.k_pais=r.K_pais AND UPPER(r.n_nombre_region)='CARIBE' AND i.k_pais=r.K_pais AND i.k_region=r.k_region AND i.k_producto=pr.k_producto order by pr.n_nomproducto asc"):
        consulta1.append(datos[0])
        consulta2.append(datos[1])
        consulta3.append(datos[2])
    # print (consulta1)
    categoria = {'nombre': consulta1, 'precio': consulta2, 'id': consulta3}
    # precio= consulta["precio"]
    # print (categoria)
    return categoria


def compra_1(request):
    # conexion = connect()
    producto = []
    cantidad = []

    compra = {'producto': producto, 'cantidad': cantidad}

    if request.method == 'POST':
        dat = request.form
        for key, value in dat.items():
            # print(key," : ", value)
            if value != '0':
                producto.append(key)
                cantidad.append(value)
    return compra


# print(compra)
def categoria_1(compra):
    conexion = connect()
    longitud_1 = []
    consulta1_1 = []
    consulta2_1 = []
    consulta3_1 = []

    for i in range(len(compra["producto"])):
        for datos in conexion.sentenciaCompuesta(
                " SELECT  pr.n_nomproducto, i.v_precio_unidad, i.K_PRODUCTO FROM PAIS p, REGION r, PRODUCTO pr, INVENTARIO i WHERE UPPER(p.n_nombre_pais)='COLOMBIA' AND p.k_pais=r.K_pais AND UPPER(r.n_nombre_region)='CARIBE' AND i.k_pais=r.K_pais AND i.k_region=r.k_region AND i.k_producto=pr.k_producto AND i.k_producto='" + str(
                        compra['producto'][i]) + "' order by pr.n_nomproducto asc"):
            consulta1_1.append(datos[0])
            consulta2_1.append(datos[1])
            consulta3_1.append(datos[2])
    # print(consulta1_1)
    # categoria_1= {'nombre':consulta1_1,'precio':consulta2_1, 'id':consulta3_1}

    # return categoria_1

    # def longitud_1(compra,categoria_1):
    consulta4_1 = []
    for i in range(len(compra["producto"])):
        longitud_1.append(i)
        consulta4_1.append(int(compra['cantidad'][i]) * int(consulta2_1[i]))

    # categoria_1= {'nombre':categoria_1['nombre'],'precio':categoria_1['precio'], 'id':categoria_1['id'],'total':consulta4_1}
    categoria_1 = {'nombre': consulta1_1, 'precio': consulta2_1, 'id': consulta3_1, 'total': consulta4_1}
    var = {'categoria_1': categoria_1, 'longitud_1': longitud_1}
    return var
