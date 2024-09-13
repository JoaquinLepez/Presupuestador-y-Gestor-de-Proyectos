class RouteApp:
    def init_app(self, app):
        from app.resources import home, user, team, project, task
        app.register_blueprint(home, url_prefix='/api/v1')
        app.register_blueprint(user, url_prefix='/api/v1')
        app.register_blueprint(team, url_prefix='/api/v1')
        app.register_blueprint(project, url_prefix='/api/v1')
        app.register_blueprint(task, url_prefix='/api/v1')


