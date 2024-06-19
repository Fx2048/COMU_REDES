
## 5. Copias de seguridad y recuperación en Amazon RDS

Amazon RDS proporciona varios mecanismos para respaldo y recuperación de bases de datos:

1. **Copias de seguridad automatizadas**:
   - Amazon RDS crea copias de seguridad diarias completas de tus datos y registros de transacciones.
   - Puedes configurar un período de retención de hasta 35 días para las copias de seguridad automatizadas.
   - Estas copias de seguridad permiten la recuperación en un momento dado (PITR) de tu instancia de base de datos.

2. **Instantáneas de base de datos (DB snapshots)**:
   - Puedes crear manualmente instantáneas de bases de datos en cualquier momento.
   - Estas instantáneas se conservan hasta que las elimines explícitamente.
   - Proporcionan una forma de restaurar la instancia de base de datos a un estado conocido.

## 6.  Alta disponibilidad con Multi-AZ

La arquitectura Multi-AZ en Amazon RDS ofrece alta disponibilidad y durabilidad:

- **Funcionamiento**:
  - Amazon RDS crea una instancia primaria y sincrónicamente replica los datos en una instancia secundaria en una zona de disponibilidad diferente (AZ).
  - Si se detecta una falla en la instancia primaria, Amazon RDS realiza un failover automático a la instancia secundaria sin intervención manual.

- **Beneficios**:
  - **Recuperación rápida**: El failover se completa en segundos (normalmente, menos de 35 segundos) con cero pérdida de datos.
  - **Mayor disponibilidad**: En caso de falla de AZ o instancia, la instancia secundaria toma el control automáticamente.
  - **Mejora de latencia de transacciones**: Multi-AZ con dos instancias secundarias permite una latencia de confirmación de transacciones más rápida.

- **Escenario crítico**:
  - Imagina una aplicación de comercio electrónico durante una venta masiva. La alta disponibilidad es crucial para evitar interrupciones del servicio y pérdida de ventas. Multi-AZ garantiza que la base de datos esté siempre disponible incluso si una AZ completa falla.
