# Interactuando con la API de Spotify

Spotify se puede utilizar como fuente de datos para varios proyectos de ciencia de datos. En este ejercicio, aprenderemos a interactuar con la API de esta red social. `Spotipy` es una librería de código abierto y para Python que permite hacer un uso a alto nivel de la API de Spotify.

## Paso 1: Crear una cuenta de desarrollador de Spotify

Antes de comenzar a programar, necesitas acceso a las credenciales de desarrollador de Spotify. Visita [developer.spotify.com](https://developer.spotify.com/documentation/web-api).

- Inicia sesión con tu cuenta de Spotify (o crea una si aún no tienes una).

- Ve a Dashboard y haz clic en Create an App. Completa los campos requeridos. En Redirect URI, escribe: `http://localhost/`


![Spotify create app](https://github.com/4GeeksAcademy/interacting-with-api-python-project-tutorial/blob/main/assets/spotify_1.PNG?raw=true)


Una vez creada la app, dirígete a la sección **Settings** para copiar tu `Client ID` y `Client Secret`. Los usarás más adelante para autenticarte ante la API.

## Paso 2: Configuración inicial

- Abre la terminal y asegúrate de tener instalada la librería `Spotipy`, que es la que usaremos para conectarnos con la API de Spotify:

    ```bash
    pip install spotipy
    ```

## Paso 3: Variables de entorno

Ya tienes el archivo `.env` en la raíz del proyecto. Asegúrate de que contenga las siguientes variables con tus credenciales de Spotify (reemplaza el contenido con tus propios datos):

```env
CLIENT_ID=your_client_id
CLIENT_SECRET=your_client_secret
```

> ⚠️ Es importante que coloques tus datos en las variables de entorno para evitar exponer tus credenciales si subes el proyecto a un repositorio.

Ahora, en el archivo `app.py`, agrega el siguiente código para leer las variables de entorno:

```python
import os
import pandas as pd
import seaborn as sns
from dotenv import load_dotenv

# load the .env file variables
load_dotenv()

# Get credential values
client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")
```

Con esto, tus credenciales estarán listas para ser utilizadas en la autenticación con la API de Spotify.


## Paso 4: Inicializar la biblioteca Spotipy

- Importar Spotipy.
- Realizar la conexión con la API. Para ello, puedes utilizar la función `spotipy.Spotify()`.

```python
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
spotify = spotipy.Spotify(auth_manager=auth_manager)
```

> 💡 NOTA: Utiliza la siguiente documentación como guía sobre los parámetros: https://spotipy.readthedocs.io/en/2.22.1

## Paso 5: Realizar solicitudes a la API

- Comienza a interactuar con la API de Spotify: Obtén de tu artista favorito, el top 10 de sus canciones. Para ello, tendrás que buscar el `ID` del artista para usarlo en la librería. Este identificador es la dirección web que tiene el artista en Spotify:

![Buscar el identificador del artista en Spotify](https://github.com/4GeeksAcademy/interacting-with-api-python-project-tutorial/blob/main/assets/spotify_2.png?raw=true)

- Una vez tengas la respuesta de la API, quédate con el elemento `tracks`, que contendrá las canciones con más reproducciones del artista, quédate con el nombre de la canción, la popularidad y la duración (en minutos).

> ⚠️ **NOTA** sobre posibles mensajes al ejecutar el código. Es posible que al finalizar la ejecución del script aparezca un mensaje como:

```
 Exception ignored in: <function Spotify.__del__ ...>
 TypeError: isinstance() arg 2 must be a type, a tuple of types, or a union
```

Este mensaje proviene de la librería `spotipy` y **no afecta la funcionalidad de tu código ni los resultados de la API**. Puedes ignorarlo de forma segura; se trata de un detalle interno de limpieza de objetos (**garbage collection**) que no interrumpe tu análisis.


## Paso 6: Transformar a Pandas DataFrame

Puesto que el resultado obtenido en estos pasos es susceptible de tener formato de tabla, conviértelo en un DataFrame importando los datos en su formato de diccionario. A continuación, ordena las canciones por popularidad creciente y muestra el top 3 resultante.

## Paso 7: Analizar relación estadística

¿Tiene relación la duración con la popularidad? ¿Podríamos decir que una canción que dure poco tiempo puede ser más popular que otra que dure más? Analízalo graficando un `scatter plot` y argumenta tu respuesta.


## ¿Te sientes con ganas de profundizar? 😎  
**Exploración avanzada de atributos musicales - Análisis extendido con enfoque interpretativo**

Si ya lograste conectarte a la API de Spotify, extraer información de tu artista favorito y representar datos básicos como popularidad y duración, te invitamos a realizar esta versión extendida del proyecto. Esta actividad opcional te permitirá incorporar nuevas variables musicales, aplicar pensamiento analítico y redactar conclusiones claras y bien fundamentadas a partir de los datos.

---

### Propuesta 🚀  
Aprovecha que ya tienes acceso a los datos del artista para profundizar en el análisis incluyendo nuevas métricas que ofrece la API. El objetivo es detectar patrones o características interesantes y expresarlas en un lenguaje comprensible para cualquier lector.

#### Variables recomendadas para explorar:

- **Danceability**: Qué tan fácil es bailar la canción.
- **Valence**: Qué tan positiva o feliz suena.
- **Energy**: Intensidad o fuerza general.
- **Tempo**: Velocidad (en BPM).

---

1. **Recupera los atributos adicionales:** Utiliza el método `audio_features()` para obtener los atributos musicales de las canciones de tu artista:

    ```python
    track_ids = [track["id"] for track in results["tracks"]]
    features = sp.audio_features(track_ids)
    ```

2. **Crea un nuevo DataFrame con la información completa:** Combina los datos obtenidos anteriormente (`nombre, popularidad, duración`) con las nuevas métricas.

3. **Realiza un análisis sencillo:** Explora los valores promedio, busca extremos, identifica correlaciones visuales o estadísticamente.

    - ¿Qué valores destacan en este artista?

    - ¿Existe alguna tendencia entre popularidad y otro atributo?

    - ¿Hay algo que no esperabas encontrar?

    Crea una gráfica sencilla que complemente tu conclusión.

4. **Haz visible tu trabajo:** Con base en el análisis, redacta una o dos frases que sinteticen lo que descubriste y publicalo en LinkedIn. El objetivo es comunicar tu hallazgo de forma objetiva, breve y con respaldo en los datos.

    > **Ejemplo:**
    >
    > "Las canciones más populares del artista analizado tienen un nivel de “danceability” promedio de > 0.82, lo que sugiere una clara orientación hacia lo bailable. 🕺💃 #SpotifySecrets"


