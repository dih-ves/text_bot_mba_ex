from fastapi import FastAPI
from controller import tradutorCtrl


app = FastAPI(
    swagger_ui_parameters={
        "dom_id": "#swagger-ui",
        "layout": "BaseLayout",
        "deepLinking": True,
        "showCommonExtensions": True,
        "syntaxHighlight.theme": "obsidian"
    },
    title = "api_traduz_gera_audio",
    description = "Traduz um texto e gera o audio em ingles."
)

app.memory_data = {"running": False}
app.update_info = {"status": False, "date": []}
app.include_router(tradutorCtrl.router)
