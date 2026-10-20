import re

def validar_id_usuario(id_usuario:str):
    """
    Valida que id_usuarios sea convertible a int
    Retorna True:False
    """
    patron_id = r"[1-9][0-9]*"
    return bool(re.fullmatch(patron_id, id_usuario))

def validar_nombre(nombre:str):
    patron_nombre = r"[a-zA-Záéíóú ]*\d*"
    if not nombre or not nombre.strip():
        return False
    return bool(re.fullmatch(patron_nombre, nombre.strip()))
    """
    Valida que nombre sea no nulo y que solo caracteres"""
    # Completar
    # return True

def validar_email(email:str):
    """
    Valida que email sea un correo válido"""
    patron = r"[A-Za-z0-9]+(?:[._%+-][A-Za-z0-9]+)*@(?:[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?\.)+com"
    return re.fullmatch(patron, email, re.IGNORECASE) is not None