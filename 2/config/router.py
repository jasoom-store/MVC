class Router:
    def run(app):
        print(f'< { "=" * 5 } [ RUN ] { "=" * 5 } >')

        from controllers.home import home
        from controllers.posts import posts

        app.register_blueprint(posts, url_prefix='/Posts')
        app.register_blueprint(home)

        # Dashboard

        from controllers.dashboard.home import dashboard_home
        from controllers.dashboard.posts import dashboard_posts

        # Domian:port [/Dashboard] [/Posts] [/]
        # Domian:port [/Dashboard] [/Posts] [/New_Post]

        dashboard_home.register_blueprint(dashboard_posts, url_prefix='/Posts')
        app.register_blueprint(dashboard_home, url_prefix='/Dashboard')
