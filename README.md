Whisper Map - QGIS Plugin
Whisper Map is an experimental GeoAI research plugin for QGIS that serves as a spatial-textual bridge for ethnographic fieldwork. By enabling the local transcription and geolocating of community oral histories, this tool allows researchers to map intangible cultural heritage directly within their GIS environment.

🌟 Features
Audio-to-Point Engine: Automatically processes audio files into text using local transcription models.

Spatial Anchoring: Allows users to anchor audio excerpts to specific map coordinates, creating a permanent geo-referenced record of oral history.

Semantic Search: Enables querying of interview libraries by keyword to uncover hidden heritage values.

Local-First Sovereignty: All processing—from transcription via Whisper to analysis via Llama 3 (Ollama)—runs entirely on your local hardware. No data, audio, or transcripts ever leave your machine.

📥 How to Install
Click the green Code button and select Download ZIP.

Open QGIS.

Go to Plugins > Manage and Install Plugins > Install from ZIP.

Select the downloaded file and click Install.

🛠 Development Workflow
Step 1: Local Environment Configuration
Transcription: Install the local library: pip install openai-whisper.

Intelligence: Download Ollama and pull a model (e.g., ollama pull llama3) to serve as the local analytical brain.

Step 2: Plugin Logic
The plugin functions as a local orchestrator between QGIS and your machine's computing power:

Transcription: The plugin invokes model.transcribe(audio_path) locally via the openai-whisper library.

Spatial Mapping: Uses QgsMapToolEmitPoint to capture user coordinates on the map canvas.

Integration: Transcripts are saved as attribute fields in a local GeoPackage or memory layer.

AI Analysis: Optional analysis is performed by sending text to the local Ollama API at http://localhost:11434/api/generate.

🔬 Research Context
This plugin was developed to move beyond visual-only mapping by integrating intangible heritage. By transforming oral testimonies into searchable spatial data, Whisper Map enables a sovereign, bottom-up approach to urban heritage management, ensuring community voices remain under the researcher's complete control.

Resources
License: GPL-2.0

Tools: QGIS Python API, Whisper (Local STT), Ollama (Local Llama 3).
