TRADUCCIONES = {
    "es": {
        "nav.inicio": "Inicio",
        "nav.productos": "Productos",
        "nav.lotes": "Lotes",
        "nav.login": "Iniciar sesión",
        "nav.registro": "Registrarse",
        "nav.salir": "Salir",
        "nav.sobre": "Sobre AgroVía",
        "nav.notificaciones": "Notificaciones",

        "login.titulo": "Iniciar sesión",
        "login.ayuda": "Ingresa con tu correo o número de documento.",
        "login.usuario": "Correo o documento",
        "login.password": "Contraseña",
        "login.boton": "Ingresar",
        "login.sin_cuenta": "¿No tienes una cuenta?",
        "login.olvido": "¿Olvidaste tu contraseña?",

        "reg.titulo": "Crear cuenta",
        "reg.ayuda": "Regístrate como productor o comprador.",
        "reg.nombres": "Nombres",
        "reg.ap_paterno": "Apellido paterno",
        "reg.ap_materno": "Apellido materno",
        "reg.tipo_doc": "Tipo de documento",
        "reg.doc_dni": "DNI",
        "reg.doc_ce": "Carné de extranjería",
        "reg.doc_pas": "Pasaporte",
        "reg.num_doc": "Número de documento",
        "reg.telefono": "Teléfono",
        "reg.correo": "Correo",
        "reg.password": "Contraseña",
        "reg.tipo_usuario": "Tipo de usuario",
        "reg.seleccionar": "Seleccionar",
        "reg.productor": "Productor agrícola",
        "reg.comprador": "Comprador",
        "reg.referido": "Código de referido (opcional)",
        "reg.boton": "Crear cuenta",

        "rec.titulo": "Recuperar contraseña",
        "rec.correo": "Correo de la cuenta",
        "rec.boton": "Enviar enlace",
        "rec.volver": "Volver al inicio de sesión",
    },
    "en": {
        "nav.inicio": "Home",
        "nav.productos": "Products",
        "nav.lotes": "Lots",
        "nav.login": "Log in",
        "nav.registro": "Sign up",
        "nav.salir": "Log out",
        "nav.sobre": "About AgroVía",
        "nav.notificaciones": "Notifications",

        "login.titulo": "Log in",
        "login.ayuda": "Sign in with your email or document number.",
        "login.usuario": "Email or document",
        "login.password": "Password",
        "login.boton": "Sign in",
        "login.sin_cuenta": "Don't have an account?",
        "login.olvido": "Forgot your password?",

        "reg.titulo": "Create account",
        "reg.ayuda": "Sign up as a producer or buyer.",
        "reg.nombres": "First names",
        "reg.ap_paterno": "Paternal surname",
        "reg.ap_materno": "Maternal surname",
        "reg.tipo_doc": "Document type",
        "reg.doc_dni": "National ID (DNI)",
        "reg.doc_ce": "Foreigner ID card",
        "reg.doc_pas": "Passport",
        "reg.num_doc": "Document number",
        "reg.telefono": "Phone",
        "reg.correo": "Email",
        "reg.password": "Password",
        "reg.tipo_usuario": "User type",
        "reg.seleccionar": "Select",
        "reg.productor": "Agricultural producer",
        "reg.comprador": "Buyer",
        "reg.referido": "Referral code (optional)",
        "reg.boton": "Create account",

        "rec.titulo": "Recover password",
        "rec.correo": "Account email",
        "rec.boton": "Send link",
        "rec.volver": "Back to login",
    },
}

IDIOMAS = {"es": "Español", "en": "English"}


def traducir(clave, idioma):
    return (
        TRADUCCIONES.get(idioma, {}).get(clave)
        or TRADUCCIONES["es"].get(clave)
        or clave
    )
