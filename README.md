# BLE Color Controller (Controlador de Color BLE)

Esta es una aplicación web simple que te permite seleccionar un color y enviarlo a un dispositivo Bluetooth Low Energy (BLE) que utilice el servicio UART. El valor del color se envía en formato CSV (ej. "255,0,128").

## ✨ Características

* **Selector de Color Interactivo:** Elige cualquier color de una paleta visual.
* **Conexión BLE Sencilla:** Conéctate a dispositivos BLE que anuncien el servicio UART con un solo clic.
* **Envío de Datos en Tiempo Real:** El valor RGB se envía instantáneamente a tu dispositivo a medida que cambias el color.
* **Indicador de Estado:** Muestra visualmente si la aplicación está conectada, desconectada o en proceso de conexión.
* **Diseño Responsivo:** Funciona en navegadores de escritorio y móviles (Android).
* **Interfaz Moderna:** Creada con Tailwind CSS para una apariencia limpia y agradable.

## 🚀 Cómo Usar

1.  **Prepara tu Ideaboard:**
    * Instalar el codigo "color_picker.py"

2.  **Abre la Aplicación Web:**
    * Usando un navegador Chrome conecta con el siguiente link.

3.  **Conéctate al Dispositivo:**
    * Haz clic en el botón **"Conectar a Dispositivo"**.
    * Aparecerá una ventana emergente del navegador mostrando los dispositivos BLE cercanos.
    * Selecciona tu dispositivo de la lista y haz clic en "Emparejar" (Pair).
    * El indicador de estado cambiará a verde y el texto mostrará "Conectado".

4.  **Controla el Color:**
    * Haz clic en el círculo de color grande para abrir el selector de color de tu sistema.
    * A medida que elijas un nuevo color, el valor RGB se enviará en tiempo real a tu dispositivo.

5.  **Desconéctate:**
    * Cuando hayas terminado, haz clic en el botón **"Desconectar"**.

## 📋 Requisitos

* **Hardware:** Un dispositivo BLE (microcontrolador) con un LED RGB (o similar) y firmware que implemente el servicio BLE UART.
* **Navegador:** Un navegador web que soporte la API de Web Bluetooth:
    * **Chrome** en Windows 10, macOS, Linux y Android.
    * **Edge** en Windows 10.
    * **Opera** en Windows 10, macOS.

## 🛠️ Tecnologías Utilizadas

* **HTML5**
* **Tailwind CSS** para el diseño de la interfaz.
* **JavaScript (ES6+)** para la lógica de la aplicación.
* **Web Bluetooth API** para la comunicación inalámbrica.