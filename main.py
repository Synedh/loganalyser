#!/sur/bin/env python3

import log_parser
import routes

LOG_DIRECTORY = "apache2/"


def main():
    routes.app.run()

if __name__ == "__main__":
    main()
