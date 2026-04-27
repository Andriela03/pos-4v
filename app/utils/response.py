def success_response(data, status=200):
    return {
        "success": True,
        "data": data,
    }, status


def error_response(message, status=400):
    return {
        "success": False,
        "message": message,
    }, status

def success_response_service(data, status=200):
    return {
        "success": True,
        "data": {
            "id": id,
            "nome": nome,
            "descricao": descricao,
            "preco_base": preco_base
        },
    }, status

def error_response_service(message, status=400):
    return {
        "success": False,
        "message": message,
    }, status

def success_response_serviceorder(data, status=200):
    return {
        "success": True,
        "data": {
            "id": id,
            "descricao": descricao,
            "status": "aberta",
            "service_id": service_id
        },
    }, status

def error_response_serviceorder(message, status=400):
    return {
        "success": False,
        "message": message,
    }, status

