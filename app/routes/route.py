class RouteApp:
    def init_app(self, app):
        from app.resources import home, user, team
        app.register_blueprint(home, url_prefix='/api/v1')
        app.register_blueprint(user, url_prefix='/api/v1')
        app.register_blueprint(team, url_prefix='/api/v1')


    # def init_app(self, app):
    #     from app.resources import home, user, team, role, urt
    #     app.register_blueprint(role, url_prefix='/api/v1')
    #     app.register_blueprint(urt, url_prefix='/api/v1')

