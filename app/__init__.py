from app.model.models import create_app, DB


app = create_app()
DB.init_app(app)
