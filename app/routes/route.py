class RouteApp:
    def init_app(self, app):
        from app.resources import home, user
        app.register_blueprint(home)
        app.register_blueprint(user)

