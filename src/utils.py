def validar_id_usuario(id_usuario:str):
    """
    Valida que id_usuarios sea convertible a int
    Retorna True:False
    """
    # Completar
    return True

def validar_nombre(nombre:str):
    """
    Valida que nombre sea no nulo y que solo caracteres"""
    # Completar
    return True

def validar_email(email: str):
    patron_mail = r"[\w.+-]+@[\w-]+\.[a-zA-Z.]{2,}"
    return bool(re.fullmatch(patron_mail, email.strip()))
