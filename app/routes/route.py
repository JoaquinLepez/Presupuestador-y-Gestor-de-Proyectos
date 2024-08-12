class RouteApp:
    def init_app(self, app):
        from app.resources import home
        app.register_blueprint(home)


