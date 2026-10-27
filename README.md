# Agrovia - Sistema Web conectado a MariaDB/phpMyAdmin

## 1. Crear la base de datos
En phpMyAdmin:
1. Crear la base de datos `agrovia_v01` con cotejamiento `utf8mb4_unicode_ci`.
2. Importar `sql/agrovia_v01.sql`.

Si la base `agrovia_v01` ya existía y ya ejecutaste `sql/migracion_contenidos_educativos.sql`, selecciona esa base en phpMyAdmin e importa una sola vez `sql/migracion_video_contenidos_educativos.sql`.

Para enlazar el comprobante fiscal seleccionado con cada pago en una base existente, importa una sola vez `sql/migracion_pago_facturacion.sql` después de crear `datos_facturacion`.

## 2. Configurar conexión
Copiar `.env.example` como `.env` y revisar:
- DB_HOST
- DB_PORT
- DB_NAME
- DB_USER
- DB_PASSWORD
- SECRET_KEY

Genera una clave aleatoria para `SECRET_KEY` con `python -c "import secrets; print(secrets.token_hex(32))"` y no la compartas ni la guardes en el repositorio. En producción define además `APP_ENV=production`, configura el servicio detrás de HTTPS y usa `SESSION_COOKIE_SECURE=true`; la aplicación rechaza iniciar en producción sin una clave de al menos 32 caracteres. El modo de depuración está desactivado.

Los formularios POST incluyen protección CSRF automáticamente. Las cookies de sesión usan `HttpOnly` y `SameSite=Lax`. Mantén la clave secreta privada y reiníciala si se filtra.

Para Gmail, configurar en `.env` `SMTP_HOST=smtp.gmail.com`, `SMTP_PORT=587`, `SMTP_USE_TLS=true` y `SMTP_USE_SSL=false`. En `SMTP_USER` y `SMTP_FROM` usar la dirección de Gmail; en `SMTP_PASSWORD`, una contraseña de aplicación de Google (requiere tener activada la verificación en dos pasos). Crea la contraseña de aplicación desde la seguridad de tu cuenta de Google y escríbela directamente en `.env`, sin compartirla ni guardarla en el repositorio. Reinicia la aplicación después del cambio. Para otro servidor, usar sus parámetros SMTP; el puerto 587 requiere STARTTLS (`SMTP_USE_TLS=true`, `SMTP_USE_SSL=false`) y el 465 TLS implícito (`SMTP_USE_TLS=false`, `SMTP_USE_SSL=true`). `APP_BASE_URL` debe ser la URL pública de la aplicación. El enlace expira en 30 minutos y cada cuenta puede solicitar hasta 3 enlaces por cada ventana de 15 minutos.

La aplicación invalida los enlaces de recuperación utilizados al cambiar la contraseña. La cuenta de MySQL configurada debe tener acceso a `usuarios` y `tokens_seguridad`; la estructura de esta última se define en `sql/agrovia_v01.sql`. Los errores de base de datos se registran y se informa al usuario para que el fallo no aparezca como una página 500. Configura SMTP con credenciales válidas y prueba el envío con una cuenta controlada; los errores SMTP se registran en el log de la aplicación.

Para XAMPP/MariaDB local normalmente:
DB_HOST=127.0.0.1
DB_PORT=3306
DB_USER=root
DB_PASSWORD=

Estos valores son solo para desarrollo local con XAMPP. En producción no usar `root` ni una contraseña vacía; crear un usuario MariaDB dedicado con los permisos mínimos requeridos por la aplicación.

## 3. Instalar dependencias
Windows:
```bash
py -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## 4. Crear usuario administrador
```bash
python crear_admin.py
```

## 5. Ejecutar
```bash
python app.py
```
Abrir: http://127.0.0.1:5000

## 6. Recuperación de cuenta
El enlace de recuperación solo se envía cuando SMTP está configurado. Los tokens se almacenan como hash, expiran a los 30 minutos y se invalidan al cambiar la contraseña.

## Módulos incluidos
- Inicio / marketplace
- Inicio de sesión
- Dashboard
- Catálogo de productos
- Predios, direcciones de entrega y direcciones fiscales con selección de ubigeo
- Lotes publicados
- Usuarios y roles
- Operaciones con historial de estados visible para productor y comprador participantes; 5 puntos por participante cuando la operación está completada y ambos la calificaron
- Dashboard administrativo con métricas de lotes disponibles, operaciones activas, pagos por revisar, cosechas en proceso, entregas pendientes e incidencias abiertas
- Mi cuenta
- Referencias calculadas de precios, cosecha y logística a través de vistas SQL

El módulo de Cosechas muestra los parámetros y costos referenciales activos de `vw_parametros_cosecha_demo`, incluyendo calidad y fuente del dato. Las rutas con permisos operativos validan las asignaciones activas en `usuarios_roles`, `roles`, `roles_permisos` y `permisos`; los cambios de rol o permiso se aplican sin depender de los datos guardados al iniciar sesión.

Los compradores deben registrar una dirección de entrega con ubigeo antes de cotizar. Al aceptar una cotización, administración confirma los kilómetros por carretera, la carga en kg, el tipo de vehículo y los peajes. El costo base, el precio al cliente y el detalle de distancia, carga y tipo de vehículo se conservan en `cotizaciones_operacion` y `cotizaciones_logisticas`. Al asignar el transporte, el sistema exige un vehículo activo, disponible, perteneciente al transportista elegido y con capacidad suficiente para la carga registrada; la asignación actualiza vehículo, operación y lote en una transacción. El rango de producción verificado se propone como carga inicial cuando existe; administración debe confirmarlo. La distancia es manual porque el sistema no tiene un proveedor de rutas conectado.

La aplicación consulta directamente las tablas de la BD `agrovia_v01`; no crea una base de datos paralela.

## Notificaciones y seguimiento
Las solicitudes de lote y los cambios de verificación se registran en el historial y se notifican al productor y al personal con el permiso de revisión. Los cambios de operación notifican al productor y al comprador participantes; los pagos pendientes también notifican al personal autorizado. Las incidencias pueden pasar por atención, resolución y cierre; cada cambio queda registrado y se notifica a ambos participantes. Los usuarios consultan sus avisos en **Notificaciones**, productores pueden revisar estados e historial en **Mis solicitudes**, y comprador/productor ven incidencias e historial en **Mis operaciones**. Al abrir la bandeja, las notificaciones se marcan como leídas.

## Reportes descargables
Usuarios con el permiso `REPORTES_VER` pueden abrir **Reportes** desde el panel y descargar operaciones, pagos, productos, productores o entregas en Excel (`.xlsx`) o PDF. Los filtros de fechas son opcionales y el estado solo admite los valores del reporte elegido. Las fechas se aplican a la operación, pago, publicación de lotes, actividad de productores o entrega/asignación de transporte, según el reporte. Los archivos incluyen hasta 50 000 filas; para consultas mayores, delimita el periodo o el estado.
